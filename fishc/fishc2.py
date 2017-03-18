# -*- coding: UTF-8 -*-

Year = input('input a Year:')

# 判断输入是否是int类型,不是重新输入.
while not isinstance(Year, int):
	Year = int(input('input a Year:'))
# 定义变量判断是否是闰年
is_leap = False
# 能被400和100整除 能被4整除,不能被100整除,满足一个条件叫做闰年
if Year % 400 == 0 and Year % 100 == 0:
	is_leap = True
elif Year % 100 != 0 and Year % 4 == 0:
	is_leap = True
if is_leap:
	print ('%d is run' % Year)
else:
	print ('%d is not ' % Year)
