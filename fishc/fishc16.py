# -*- coding: UTF-8 -*-

import urllib.request
import os
import shutil


# 打开URL获取HTML
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/57.0.2987.110 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html


# 得到当前网站的页数
def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    return html[a:b]


# 查找所有图片地址
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_adds = []
    getimg_add = []

    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_adds.append(html[a + 9:b + 4])
        else:
            b = a + 9
        a = html.find('img src=', b)

    for each in img_adds:
        head = ['http:' + each]

        # print(each)
        img_adds = head
    print (img_adds)
    return img_adds


# 保存图片到磁盘
def save_imgs(folder, img_adds):
    for each in img_adds:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_mm(folder='OOXX', pages=25):
    if os.path.exists(r'F:\python\helloword\fishc\OOXX'):
        shutil.rmtree(folder)
    else:
    # shutil.rmtree(folder)
        os.mkdir(folder)
        os.chdir(folder)

    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))
    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_adds = find_imgs(page_url)
        save_imgs(folder, img_adds)


if __name__ == '__main__':
    download_mm()
