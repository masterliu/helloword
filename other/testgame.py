# -*- coding: UTF-8 -*-
import random

secret = random.randint(1, 10)

guess = int(input('input a num:'))
while guess != secret:
    guess = int(input('you worng angen:'))
    if guess == secret:
        print('you win')

    else:
        if guess > secret:
            print('big')
        else:
            print('min')
print('is over')
