# gopage

## Overview

Gopage is a Google search page crawler. It provides concise APIs to download Google search results, and parse them into readable data structures.



## Installation

```
pip install git+https://github.com/xgeric/gopage
```



## APIs

***Crawler*** is responsible for crawling Google search page, given a query sentence. ***Parser*** aims at parsing the html content of a Google search page into a Python list, in which each element is a dict consisting of 'title' and 'content' of the corresponding Google snippet. 

Quick start:

```python
from gopage import crawler
from gopage import parser

gpage = crawler.search('Jie Tang') # My undergraduate advisor
snippets = parser.parse(gpage)
```

It should look like this:

```python
>>> from pprint import pprint
>>> pprint(snippets)
[{'content': 'Jie Tang (Tang, Jie). Associate Professor, IEEE Senior Member, '
             'ACM Professional Member, CCF Distinguished Member. Knowledge '
             'Engineering Lab (Group)',
  'title': "Jie Tang (Tang, Jie) 's Homepage"},
 {'content': 'Arnetminer: extraction and mining of academic social networks. J '
             'Tang, J Zhang, L Yao, J Li, L Zhang, Z Su. Proceedings of the '
             '14th ACM SIGKDD international\xa0...',
  'title': 'Tang Jie - Google Scholar Citations'},
 {'content': 'Jie Tang is an associate professor at Department of Computer '
             'Science of Tsinghua University. He is known for the academic '
             'social network search system\xa0...',
  'title': 'Jie Tang - Wikipedia'},
 {'content': 'Jie Tang, Yongqiang Sun, Shishu Yang, Yiyue Sun: Revisit the '
             'Information Adoption Model by Exploring the Moderating Role of '
             'Tie strength: a Perspective from\xa0...',
  'title': 'dblp: Jie Tang'},
 {'content': 'Jan 21, 2011 - Research. I am currently a third year computer '
             'science Ph.D. student at UC Berkeley. My advisor is Pieter '
             'Abbeel. I am interested in machine\xa0...',
  'title': 'Jie Tang - University of California, Berkeley'},
 {'content': 'TANG, Jie. Group Leader, Advanced Low-Dimensional Nanomaterials '
             'Group, C4GR, National Institute for Materials Science. Email: '
             'TANG.Jie nims.go.jp.',
  'title': 'TANG, Jie | NIMS'},
 {'content': 'Online shopping from a great selection at Books Store.',
  'title': 'Amazon.com: LIU JIA JIE TANG REN WANG YI MING: Books'},
 {'content': 'I obtained my Ph.D. degree from Tsinghua University in 2016, '
             'advised by Jie Tang and Juanzi Li. During my Ph.D. career, I '
             'have been visiting Cornell University\xa0...',
  'title': 'Yang Yang - Zhejiang University'},
 {'content': 'email email icon. Jie Tang Associate Professor of Medicine '
             '(Clinical). Brown Affiliations. Medicine. Background. scroll to '
             'property group menus. Background\xa0...',
  'title': 'Tang, Jie - Researchers @ Brown - Brown University'},
 {'content': 'Jie Tang. Tsinghua University. Beijing 100084, China '
             'jietang@tsinghua.edu.cn. 1. Please share with us your view on '
             'the history and important milestones of the\xa0...',
  'title': 'A conversation with Professors Deyi Li and Jie Tang'}]
```

I also added a simple email address filter to parser. It helps findout all snippets containing email addresses, and normalize various email address formats.

```python
esnippets = parser.filt_email(snippets)

>>> pprint(esnippets)
[{'content': 'Jie Tang. Tsinghua University. Beijing 100084, China '
             'jietang@tsinghua.edu.cn. 1. Please share with us your view on '
             'the history and important milestones of the\xa0...',
  'emails': ['jietang@tsinghua.edu.cn'],
  'title': 'A conversation with Professors Deyi Li and Jie Tang'}]
```



## Signatures

***crawler.search(query, useproxy=True, verbose=True, maxtry=5, timeout=5)***

* query [str]: The query keywords. I'm only testing on English queries for now.
* useproxy [bool]: Whether to use a proxy pool to prevent being blocked.
* verbose [bool]:  Whether to show current information, including proxy ip, target url, success or not and retry times.
* maxtry [int]: Max retry times.
* timeout [int]: Max waiting time, in seconds.
* @return gpage [str]

***parser.parse(gpage)***

* gpage [str]: The html content of a Google search page.
* @return snippets [list]

***parser.filt_email(snippets)***

* snippets [list]: Snippets extracted by parser.parse.
* @return snippets [list]





## Contact

Please feel free to let me know if you have any questions or suggestions. Have fun!

Author: Xiaotao Gu

Email: guxt1994@gmail.com