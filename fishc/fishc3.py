# -*- coding: UTF-8 -*-
temp = input('input a num:')
number = int(temp)
# i = 1
# while number:
# 	print(i)
# 	i += 1
# 	number -= 1
while number:
	i = number-1
	while i:
		print(' ', end='')
		i -= 1
	j = number
	while j:
		print("*", end='')
		j -= 1
	print()
	number -= 1
