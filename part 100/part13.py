# -*- coding: UTF-8 -*-
# 打印出所有的"水仙花数"
# 利用for循环控制100-999个数，每个数分解出个位，十位，百位
for n in range(100, 1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print n
