# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 18:50:40 2024

@author: hp
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('http://py4e-data.dr-chuck.net/comments_1957061.html')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
print('soup',soup)

# Retrieve all of the anchor tags
tags = soup('tr')