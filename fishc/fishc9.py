# -*- coding: UTF-8 -*-
# 红3,黄3,绿6
print('red\tyellow\tbule')
for red in range(0, 4):  # 红色3个球
	for yellow in range(0, 4):  # 黄球3个
		for green in range(2, 7):  # 绿球6[2,3,4,5,6]
			if red + yellow + green == 8:
				print(red, '\t', yellow, '\t', green)
