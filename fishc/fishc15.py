# -*- coding: UTF-8 -*-
# urllib 代理

import urllib.request
import random

url = 'http://www.ip.cn/'
iplist = ['67.205.148.148:80', '111.23.6.143:80', '121.32.251.44:80']
proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
