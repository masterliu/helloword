# -*- coding: UTF-8 -*-
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum += (temp % 10) ** 3
        # sum = sum + (temp % 10) ** 3
        temp //= 10

    if sum == i:
        print(i)
