# -*- coding: UTF-8 -*-

a = int(input('input a number:\n'))

x = str(a)
# 把int值转换为 str类型
flag = True

for i in range(len(x) / 2):
	if x[i] != x[-i - 1]:
		print (x[i], x[-i-1])
		flag = False
		break
if flag:
	print ('%d is' % a)

else:
	print ('%d is not' % a)
