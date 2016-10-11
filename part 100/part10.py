# -*- coding: UTF-8 -*-
#http://www.runoob.com/python/python-exercise-example12.html
f1 = 1
f2 = 1
for i in range(1,21):
    print '%12d %12d' %(f1,f2),
    if (i % 3)==0:
        print ''
    f1 = f1 +f2
    f2 = f1+ f2