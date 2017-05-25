# -*- coding: utf-8 -*-

# __init__����
# person('swaroop').sayHi()
class Person:
	def __init__(self, name):
		self.name = name

	def sayHi(self):
		print
		('hello,my name is', self.name)


p = Person('swaroop')
p.sayHi()

# ����ķ���
'''
class Person:
	def sayHi(self):
		print "hello,how are you"
		
p = Person()
p.sayHi()
'''
# ��

'''
class Person:
	pass
p = Person()

print p
'''
