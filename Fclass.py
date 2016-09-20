# -*- coding: UTF-8 -*- 
#关于继承
class Dad(object):
	def __init__(self,surname):
		self.surname = surname
	
class Son_1(Dad):#重写父类__init__方法,增加name属性
	def __init__(self,surname,name):
		Dad.__init__(self,surname)
		self.name =name

class Son_2(Dad):
	def __init__(self,surname):
		Dad.__init__(self,surname)
		self.name = 'Si'
		
		
if __name__ =='__main__':
	son_1 = Son_1('li','gouhai')
	print son_1.surname,son_1.name
	son_2 = Son_2('li')
	print son_2.surname,son_2.name