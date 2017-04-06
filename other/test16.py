# -*- coding: UTF-8 -*-

try:
    x = int(input('input a num:'))
    y = int(input('input b num:'))
    print(x / y)
except ZeroDivisionError as reason:
    print('b can\'t be zero' + str(reason))
except TypeError as reason:
    print('type is error ' + str(reason))
except ValueError as reason:
    print('value is error' + str(reason))
finally:
    print('我会执行')