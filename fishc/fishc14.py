# -*- coding: UTF-8 -*-
# 爬虫 有道翻译
# urllib 修改header,两种方法
import urllib.request
import urllib.parse
import json
import time
while True:
    content = input('input some thing("q!,quit"):')
    if content == 'q!':
        break
    # 第一种方法
    head = {}
    head[
        'User_Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data, head)
    # req = urllib.request.Request(url, data)
    # 第二种方法
    # req.add_header('User_Agent',
    #                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36')

    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print((target['translateResult'][0][0]['tgt']))
    time.sleep(3)