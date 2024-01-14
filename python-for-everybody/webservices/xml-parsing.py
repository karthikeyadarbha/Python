# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:07:39 2024

@author: hp
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
serviceurl = 'https://py4e-data.dr-chuck.net/comments_1957063.xml'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parms = dict()
url = serviceurl + urllib.parse.urlencode(parms)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
count = 0
for res in results:
    count = count + int(res.find('count').text)
print(count)