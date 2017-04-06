# -*- coding: UTF-8 -*-
# x起始,Y是借用,z是目的
# 汉诺塔 游戏


def hanoi(n, x, y, z):
    if n == 1:
        print(x, '---->', z)
    else:
        # 将n-1个盘子从X移动到Y
        hanoi(n - 1, x, z, y)
        # 将最底下的最后一个盘子从X移动到z
        print((x, '--->', z))
        # 将y上的N-1个盘子移动到z
        hanoi(n - 1, y, x, z)


n = int(input('input num:'))
hanoi(n, 'x', 'y', 'z')
