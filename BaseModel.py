# -*- coding: UTF-8 -*- 
#关于父类,子类,继承,重写的例子
class BaseClass:
	def __init__(self,name,age):
		self.name =name
		self.age = age 
		print"baseclass is inited"
	def speak(self,name):
		print"base class is speak:%s"%name
#if(__name__=="__main__"):
#	b=BaseClass()
	
class Subclass(BaseClass):
	def __init__(self,name,age,salary):#重写__init__方法
		BaseClass.__init__(self,name,age)
		self.salary=salary
		print "subclass is inited and the salary is :%s"%self.salary
	def talk(self,sth):
		print"%s talking %s"%(self.name,sth)
		BaseClass.speak(self,sth)
if(__name__=="__main__"):
	s = Subclass("joan",1,800)
	s.talk("a story")