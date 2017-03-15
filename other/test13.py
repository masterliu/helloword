# -*- coding: UTF-8 -*-
# 非递归版本
'''

def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

'''


# 递归版本


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input('input a num:\n'))
result = factorial(num)
print("%d is :%d" % (num, result))
