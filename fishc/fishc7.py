# -*- coding: UTF-8 -*-
count = 3
password = 'hhh'
while count:
	passwd = input('input password:')
	if passwd == password:
		print('welcome')
		break
	elif '*' in passwd:
		print('不能有*,还有', count, '次机会\n')
		continue
	else:
		print('密码错误,还有', count, '次机会\n')
	count -= 1
