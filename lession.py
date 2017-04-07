# -*- coding: UTF-8 -*-
'''
下载网易 音乐,爬虫
'''
import requests
import urllib.request

r = requests.get("http://music.163.com/api/playlist/detail?id=378658225")
arr = r.json()['result']['tracks']
print (arr)
for i in range(2):
    name = str(i + 1) + ' ' + arr[i]['name'] + '.mp3'
    link = arr[i]['mp3Url']
    urllib.request.urlretrieve(link, "/music" + name)
    print(name + '  down')
