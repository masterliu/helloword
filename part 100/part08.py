# -*- coding: UTF-8 -*-
import time
for i in range(1,10):
    for j in range(1,10):
        rest=i * j
        print('%d * %d=% -3d'%(i,j,rest))
    print ' '

print time.ctime()
time.sleep(1)
print time.ctime()
