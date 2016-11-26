# -*- coding: UTF-8 -*-
n = int(raw_input('input a number:'))

if n >=90:
    jb = 'A'
elif n >= 60:
    jb = 'B'
else:
    jb= 'C'

print '%d jb is %s' %(n,jb)
