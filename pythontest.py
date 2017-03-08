# -*- coding: utf-8 -*-
#pythontest.py

print ('-------------------------------------')
#字符串内容

name ='swaroop'

if name.startswith('swa'):
	print'yes.the string startswith"swa"'
if 'a'in name:
		print 'yes,it contains the string "a"'
if name.find('war') != -1:
	print 'yes,it contains the string "war"'
	
delimiter = '_*_'
mylist =['Brazil','Russia','India','China']
print delimiter.join(mylist)

movies =["the holy grail","the life of brian","the meaning of life"]
movies.insert(1,1987)
movies.insert(3,1986)
movies.append(1988)
print (movies)

movies1=["the holy grail",1987,
		 "the life of brian",1988,
		 "the meaning of life",1981]
for i in movies1:
	print (i)

print ('-------------------------------------')
movies2 =["the holy grail",1987,"terry jones & Terry gilliam",91,
			["graham chapman",["michael palin","john cleese",
			"terry gilliam","Eric idle","Terry Jones"]]]
for each_item in movies2:
	if isinstance(each_item, list):
		for nested in each_item:
			if isinstance(nested,list):
				for deeper in nested:
					print (deeper)
			else:
				print(nested)
	else:
		print(each_item)

print ('--------------def-----------------------')		

# def 个函数
from nester import print_lol

print_lol(movies2)


#对象引用
'''
print 'Simple as signment'
shoplist =['apple','mango','carrot','banana']
mylist = shoplist

del shoplist[0]

print '1,shoplist is',shoplist
print '1,my list is',mylist

print'copy by making a full slice'
mylist=shoplist[:]
del mylist[0]

print 'shoplist is',shoplist
print 'my list is',mylist

'''
#数据结构
#序列
'''
shoplist =['apple','mango','carrot','banana']

print 'item 0 is',shoplist[0]
print 'item 1 is',shoplist[1]
print 'item 2 is',shoplist[2]
print 'item 3 is',shoplist[3]
print 'item -1 is',shoplist[-1]
print 'item -2 is',shoplist[-2]
##list切片
print 'item 1 to 3 is',shoplist[1:3]
print 'item 2 to end is',shoplist[2:]
print 'item 1 to -1 is',shoplist[1:-1]
print 'item start to end is',shoplist[:]
##字符串 切片
name ='swaroop'
print 'string 1 to 3 is ',name[1:3]
print 'string 2 to end is ',name[2:]
print 'string 1 to -1 is ',name[1:-1]
print 'string start to end is ',name[:]
'''
#字典
'''
ab = {'swaroop':'swaroopch@byteo.info','larry':'larry@ll.org'}

print "swaroop's address is %s" %ab['swaroop']
ab['guido'] = 'guido@python.org' # add  字典中值

del ab['larry'] #删除 字典中larry的内容 

print 'ab len is %d'%len(ab)
for name ,address in ab.items():
	print 'contact%s at %s'%(name,address)
	
if 'guido'in ab:
	print 'guido address is %s'% ab['guido']
'''
#元组,打印
'''
age = 22
name ='swaroop'

print '%s is %d years old '%(name,age)
print 'why is %s playing with that python?'%name
'''
#元组
'''
zoo = ('wolf','elephant','penguin')
print 'number of anim als in the zoo is ',len(zoo)

new_zoo =('monkey','dolphin',zoo)
print 'number of anim als in the new zoo is',len(new_zoo)
print 'allan im als in new zoo are',new_zoo
print 'anim als brought from old zoo are',new_zoo[2]
print 'lass an im albrought from old zoo is',new_zoo[2][0]#定位输入内容
'''
#list
'''
shoplist =['apple','mango','canot','banana']
print 'i have',len(shoplist),'items to purchase.'

print'these item sare:'
for item in shoplist:
	print item,
	
print'\n i also have to buy rice.'
shoplist.append('rice')
print 'my shoping list is now',shoplist

print 'i will sort my list now'
shoplist.sort()#排序
print 'sorted shopping list is',shoplist

print 'the first item i will buy is',shoplist[0]
olditem = shoplist[0]
del shoplist[0] #删除 列表中第[0]个数据
print 'i bought the,',olditem

print 'my shoping list is now',shoplist
'''

#dir()函数


#创建模块,供mymoduledemo.py 引用
'''
def sayhi():
	print 'hi,this is m module speaking.'
	
version ='0.1'
'''

##模块的__name__
'''
if __name__ == '__main__':
	print 'this program is being run by itself'
else:
	print 'iam being imported from anothermodule'
	
'''
#字节编译的.pyc文件

###模块,import 导入sys模块
'''
import sys

print 'the command line arguments are:'
for i in sys.argv:
	print i
print '\n\nthe pythonpath is',sys.path,'\n'
'''
###DocString  文档字符串,可以从函数恢复文档字符串
###使用__doc__调用printmax函数的文档字符串属性.
'''
def printMax(x,y):
	##prints the maximum of two number.
	#The two values must be integers.#
	x = int(x)
	y = int(y)
	
	if x > y:
		print x,'is maximum'
	else:
		print y,'is maximum'
	
printMax(2,50)
print printMax.__doc__
'''
###return 语句,没有返回值的return语句等价于return none
'''
def maximum(x,y):
	if x > y:
		return x
	else:
		return y
print maximum(2,3)

'''
###关键参数,通过命名为这些参数赋值,使用名字给函数指定实参
###不必担心参数顺序.可以指给想要的参数赋值
'''
def func(a,b=5,c=10):
	print 'a is ',a,'and b is ',b,'and c is ',c
	
func(3,7)
func(25,c=24)
func(c=50,a=100)
'''
###默认参数值,某些参数是可选的在函数定义形参名后加入复制(=)和默认值,给形参指定默认参数值
###默认参数值是不可变的,只能在形参末尾的参数可以有默认参数值
'''
def say(message,times =1):
	print message*times
	
say('hello')
say('World ',5)

'''
###global 语句,避免使用,global 声明x是全局的.会改变x 在主块中的值
'''
def func():
	global x
	print 'x is ',x
	x = 2
	print 'Changed local x to',x

x = 50
func()
print 'Value of x is ',x
'''

###局部变量,在函数定义内声明变量的时候,与函数外具有相同名称的其他变量没有任何关系.变量的作用域
'''
def func(x):
	print 'x is ',x
	x = 2
	print 'Changed local x to ',x

x = 50
func(x)
print 'x in still',x
'''

###函数形参,a,b 两个形参
'''
def printMax(a,b):
	if a > b:
		print a,'is max'
	else:
		print b,'is max'
		
printMax(3,5)
x = 5
y = 7
printMax(x,y)

'''
###定义函数
'''
def sayHello():
	print 'Hello World!'

sayHello()

'''

### continue,跳过当前循环块的剩余语句.然后继续进行.
'''
while True:
	s = raw_input('enter something:')
	if s == 'quit':
		break
	if len(s)<3:
		continue
	print 'input is of sufficien length'

'''
### break 语句 跳出循环
'''
while True:
	s = raw_input('enter something:')
	if s == 'quit':
		break
	print 'length is ',len(s)

print 'Done'

'''


### for in 循环
'''
for i in range(1,5):
	print i
else:
	print 'the for loop is over'
'''

###while 循环,不达到条件不退出循环
'''
number = 23
running = True

while running:
	guess = int(raw_input('enter an integer:'))

	if guess == number:
		print 'right'
		running =False
	elif guess < number:
		print'you input min'
	else:
		print'you input max'

else:
	print 'the while loop is over.'
	
print 'Done'

'''

###
'''表达式
length = 5
breadth = 2
area = length*breadth
print 'Area is',area
print 'Perimeter is',2*(length+breadth)
'''


#####
'''控制流
number=23
guess =int(raw_input('Enteran integer:'))

if guess == number:
	print'Congratulations,you guessed it.'
	print"(but you do not win any prizes!)"
elif guess < number:
	print 'No,input number is min'

else:
	print 'you is max'
	
	
print 'Done'
'''

###



