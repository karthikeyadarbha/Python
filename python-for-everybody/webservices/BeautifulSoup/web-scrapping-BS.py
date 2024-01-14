# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 19:24:19 2024

@author: hp
"""

import urllib.request as ureq
from bs4 import BeautifulSoup

current_repeat_count = 0
url = 'https://py4e-data.dr-chuck.net/known_by_Elena.html'
repeat_count = int(input('Enter count: '))
position = int(input('Enter position: '))


def parse_html(url):
    html = ureq.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while current_repeat_count < repeat_count:
    print('Retrieving: ', url)
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    current_repeat_count += 1
print('Last Url: ', url)