# -*- coding: UTF-8 -*-

'''
python 中 __name,属于私有变量,
是不能在外部进行修改的
class 类
__init__() 方法

'''
class Student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print '%s: %s' % (self.__name, self.__score)

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('bart simpson', 59)
lisa = Student('lisa simpson', 88)

bart.print_score()
print bart.get_grade()

