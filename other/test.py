# -*- coding: UTF-8 -*-

'''
python 中 __name,属于私有变量,
是不能在外部进行修改的
'''
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s: %s' % (self.name, self.score)

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('bart simpson', 59)
lisa = Student('lisa simpson', 88)

bart.print_score()
lisa.get_grade()

