# -*- coding: utf-8 -*-
#hello.py

#
#1,	print '100 + 200 =', 100+200
#
''' 2,'''
#name = raw_input(u" 输入你的名字:")
##name = raw_input("输入你的名字:".decode('utf-8').encode('gbk'))
#print 'you in put name is :',name

print 'I\'m \"ok\"'
print '''line1
line2
line3'''

#print u'中文'

#集合 list
classmates = ['michael','bob','tracy']

for name in classmates:
	print name

#for...in 循环
	
#range() 函数生成数
sum = 0
for x in range(11):
	 sum = sum + x
print sum	
#while循环
n = 99
while n>0:
	n = n -2
print n

#dist字典
d1 = {'michael':95,'bob':75}

d = {
	'michael':95,
	'bob':75,
	'tracy':85
}
print ('d[\'michael\']=',d['michael'])
print('d.get(\'thomas\',-1)=',d.get('thomas',-1))

#函数参数,可以计算任意数的N次方.可以则更加默认参数.n =2 
#def power(x,n=2)
def power(x,n):
	s = 1
	while n>0:
		n= n-1
		s = s * x
	return s
	

