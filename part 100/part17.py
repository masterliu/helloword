# -*- coding: UTF-8 -*-
# http://www.runoob.com/python/python-exercise-example18.html
import string

s = input('input a string:')
zm = 0
kg = 0
no = 0
ot = 0

for i in s:
    if i.isalpha():#是否字母
        zm += 1
    elif i.isspace():#是否空格
        kg += 1
    elif i.isdigit():#是否数字
        no += 1
    else:
        ot += 1

print('字母 = %d,空格 = %d,数字 = %d,其他 = %d' % (zm, kg, no, ot))
