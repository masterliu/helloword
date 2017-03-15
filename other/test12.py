# -*- coding: UTF-8 -*-
# 内嵌函数/闭包 的使用 nonlocal 使用
# nonlocal 在函数或其他作用域调用外层非全局变量使用
# global 声明全局变量


def fun1():
    x = 2

    def fun2():
        nonlocal x
        x *= x
        return x

    return fun2()


print(fun1())
