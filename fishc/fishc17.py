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


def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imgelist = re.findall(p, html)

    for each in imgelist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/3563409202'
    get_img(url_open(url))
