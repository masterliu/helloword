# -*- coding: UTF-8 -*-
# 质数定义为在大于1的自然数中，
# 除了1和它本身以外不再有其他因数的数称为质数(素数)
lower = int(input("min number:"))
upper = int(input("max number:"))

for num in range(lower, upper + 1):
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				break

		else:
			print (num)
