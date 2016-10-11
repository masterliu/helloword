# -*- coding: UTF-8 -*-
import math

for i in range(100):
    x = int(math.sqrt(i + 100))  # sqrt 计算平方根
    y = int(math.sqrt(i + 268))  # sqrt 计算平方根
    if (x * x == i + 100) and (y * y == i + 268):
        print i
