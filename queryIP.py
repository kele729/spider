#/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from pyquery import PyQuery as pg

ipaddr = raw_input("Enter IP:")
content=requests.get('http://www.ip138.com/ips1388.asp?ip=%s&action=2' % ipaddr)
print(content.url)
doc = pg(content.content)
li = doc('li')
print li.text()
