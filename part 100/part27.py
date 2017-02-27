# -*- coding: UTF-8 -*-
# 利用递归函数,将输入的字符,以相反的顺序打印出来.
def output(s, l):
    if l == 0:
        return
    print (s[l-1])
    output(s, l-1)

s = str(raw_input('input a string:'))
# 3.0的python,raw_input取消,由input()替换
l = len(s)
output(s, l)