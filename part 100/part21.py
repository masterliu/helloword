# -*- coding:utf-8 -*-

tour = []
height = []

hei = 100.0
# 起始高度
tim = 10
# 次数
for i in range(1,tim + 1):
    tour.append(hei)
    hei /= 2
    height.append(hei)

print ('high: tour = {0}'.format(sum(tour)))

print ('10,high:height = {0}'.format(height[-1]))

