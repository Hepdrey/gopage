# encoding: utf-8
import random
import requests
from gopage import util
from gopage import parser
from pprint import pprint


class Proxy:
    PROXIES = []

    @classmethod
    def add_proxies(cls):
        # url = 'http://erwx.daili666.com/ip/?tid=558045424788230&num=20&foreign=only'
        url = 'http://dev.kuaidaili.com/api/getproxy/?orderid=969077660455841&num=100&area=%E5%9B%BD%E5%A4%96&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=2&method=2&an_an=1&an_ha=1&sep=2'
        proxies = requests.get(url).text.splitlines()
        pprint(proxies)
        cls.PROXIES = [p.strip() for p in proxies]

    @classmethod
    def pop_proxy(cls, proxy_ip):
        if cls.PROXIES and proxy_ip in cls.PROXIES:
            cls.PROXIES.remove(proxy_ip)

    @classmethod
    def choose_proxy(cls):
        if not cls.PROXIES:
            cls.add_proxies()
        return random.choice(cls.PROXIES)


def download_page(url, useproxy=False, verbose=True, maxtry=2, timeout=5, checkpage=False):

    def retry():
        if verbose:
            print('[FAIL-{}] {} -> {}'.format(maxtry, proxy_ip, url))
        return download_page(url, useproxy, verbose, maxtry - 1, timeout)

    if maxtry <= 0:
        return None
    try:
        proxy = None
        proxy_ip = 'localhost'
        if useproxy:
            proxy_ip = Proxy.choose_proxy()
            proxy = {
                'http': proxy_ip,
                'https': proxy_ip
            }
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1 WOW64 rv:23.0) Gecko/20130406 Firefox/23.0'
        }
        # proxy_ip = '177.114.74.104:8080'
        content = requests.get(url, proxies=proxy, headers=header).text
        if checkpage:
            try:
                snippets = parser.parse(content)
                if not snippets:
                    raise Exception
            except:
                raise Exception
        if verbose:
            print('[OK] {} -> {}'.format(proxy_ip, url))
        return content

    except Exception as e:
        if useproxy:
            Proxy.pop_proxy(proxy_ip)
        return retry()


@util.cache('text')
def download_page_cache(url, useproxy=False, verbose=True, maxtry=2, timeout=5, checkpage=False):
    return download_page(url, useproxy=useproxy, verbose=verbose, maxtry=maxtry, timeout=timeout, checkpage=checkpage)


@util.cache('text')
def search(query, useproxy=True, verbose=True, maxtry=5, timeout=5, stype='page'):
    query = query.replace(' ', '+')
    stype2url = {
        'page': 'https://www.google.com/search?hl=en&safe=off&q=',
        'image': 'https://www.google.com/search?tbm=isch&source=hp&btnG=Search+Images&biw=1920&bih=1075&q='
    }
    url = '{}{}'.format(stype2url[stype], query)
    page = download_page(url, useproxy, verbose, maxtry, timeout)
    return page


@util.cache('text')
def search_image(query, useproxy=True, verbose=True, maxtry=5, timeout=5):
    query = query.replace(' ', '+')
    url = 'https://www.google.com/search?hl=en&safe=off&q={}'.format(query)
    page = download_page(url, useproxy, verbose, maxtry, timeout)
    return page


if __name__ == '__main__':
    names = [
        'jie tang',
        'jiawei han',
        'thorsten joachims'
    ]
    # for name in names:
    #     with open('{}.html'.format(name), 'w', encoding='utf-8') as wf:
    #         page = search(name, usecache=False,
    #                       cache='{}.html'.format(name.replace(' ', '')))
    #         wf.write(page)
    #         # page = requests.get('http://baidu.com')
    page = download_page_cache(
        'http://baidu.com', usecache=True, cache='baidu.html')
