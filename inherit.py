# -*- coding: UTF-8 -*- 
class Schoolmember: #父类
	'''Represent sany schoolmember.'''
	def __init__(self,name,age):
		self.name =name
		self.age =age
		print '(Initialized schoolmember:%s)'% self.name
		
	def tell(self):
		'''tell my details.'''
		print 'Name:"%s"''Age:"%s"'%(self.name,self.age)
		
class Teacher(Schoolmember):#继承父类
	'''represents a teacher'''
	def __init__(self,name,age,salary):#调用父类__init__方法
		Schoolmember.__init__(self,name,age)
		self.salary =salary
		print '(Initialized Teacher:%s)'% self.name
		
	def tell(self):#覆盖父类的tell方法
		Schoolmember.tell(self)
		print 'Salary:"%d"'%self.salary

class Student(Schoolmember):
	'''represents a student'''
	def __init__(self,name,age,marks):
		Schoolmember.__init__(self,name,age)
		self.marks =marks
		print '(Initialized student:%s)'% self.name
		
	def tell(self):
		Schoolmember.tell(self)
		print 'Marks:"%d"'%self.marks
		
		
t = Teacher('Mrs.shrividya',40,30000)
s = Student('Swaroop',22,75)
print 
members =[t,s]
for member in members:
	member.tell()