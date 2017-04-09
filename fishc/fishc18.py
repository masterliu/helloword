# -*- coding: UTF-8 -*-
import urllib.request
import re


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/57.0.2987.110 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    return html


#  ip地址的正则表达式

def get_img(html):
    p = r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))"'
    iplist = re.findall(p, html)

    print (iplist)
    for each in iplist:
        print(each)


if __name__ == '__main__':
    url = 'http://cn-proxy.com'
    get_img(url_open(url))
