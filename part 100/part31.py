# -*- coding: UTF-8 -*-
# home edit 2017年3月8日 21:58:27
letter1 = str(input('input:'))
letter = letter1.upper()
# 将输入的小写内容转换为大写
# print(letter)
if letter == 'S':
    print('you need input second letter:')
    letter = input('input:')
    if letter == 'a':
        print('saturday')
    elif letter == 'u':
        print('sunday')
    else:
        print('error')
elif letter == 'F':
    print('friday')
elif letter == 'M':
    print('monday')

elif letter == 'T':
    print('you need input second letter:')
    letter = input('input:')

    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('error')
elif letter == 'W':
    print('Wednesday')
else:
    print('error')
