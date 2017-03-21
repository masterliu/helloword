# -*- coding: UTF-8 -*-
fens = int(input('input you 分数:'))

if fens > 90:
	print('nice A')
elif 80 < fens <= 90:
	print('good B')
elif 60 < fens <= 80:
	print('ok C')
elif 60 > fens >= 0:
	print('D')
else:
	print('error')
