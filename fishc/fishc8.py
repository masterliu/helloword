# -*- coding: UTF-8 -*-
for i in range(153, 1000):
	sumer = 0
	temp = i
	while temp:
		# temp%10 求整数 的最后一位 **3 如 123 %10 得 3**3
		sumer += (temp % 10) ** 3
		# sumer = sumer +(temp%10)**3
		# 整数//10,去掉整数最后一位如123//10 得 12
		temp //= 10

	if sumer == i:
		print(i)
