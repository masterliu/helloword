# -*- coding: UTF-8 -*-
# python2.7接收输入用raw_input()
# python3.0接收输入用input()
import random

times = 3
secret = random.randint(1, 10)
guess = 0
print('input a num:')
while (guess != secret) and (times > 0):
	temp = input()
	while not temp.isdigit():
		temp = input('you need input again:')
	guess = int(temp)
	time2 = times - 1
	if guess == secret:
		print('you win')

	else:
		if guess > secret:
			print("big")
		else:
			print('min')
	if time2 > 0:
		print('again')
	else:
		print('is over')

print('game is over!')
