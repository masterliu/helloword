# -*- coding: UTF-8 -*-
def fib(n):
    if n==1:
        return [1]
    if n ==2:
        return [1,1]
    fibs=[1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
#输出前10个斐波那契数列
print fib(10)

#输出第10个斐波那契数列
def fib1(m):
    if m ==1 or m ==2:
        return 1
    return fib1(m-1)+fib1(m-2)

print fib1(10)