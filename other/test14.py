# -*- coding: UTF-8 -*-
# 递归方式实现


def fab(n):
    if n < 1:
        print('error')
        return -1

    if n == 1 or n == 2:
        return 1

    else:
        return fab(n - 1) + fab(n - 2)


result = fab(30)
if result != -1:
    print(result)
