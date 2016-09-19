# -*- coding: utf-8 -*-

#__init__方法
#person('swaroop').sayHi()
class Person:
	def __init__(self,name):
		self.name = name
	def sayHi(self):
		print 'hello,my name is',self.name

p = Person('swaroop')
p.sayHi()

#对象的方法
'''
class Person:
	def sayHi(self):
		print "hello,how are you"
		
p = Person()
p.sayHi()
'''
# 类

'''
class Person:
	pass
p = Person()

print p
'''