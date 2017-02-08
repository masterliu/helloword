# -*- coding: UTF-8 -*-

Sn = 100.0
Hn = Sn / 2

Sn += 2 * 2
print Sn

for n in range(2, 11):
    Sn += 2 * Hn
    Hn /= 2

print 'total of road is %f' % Sn
print 'the tenth is %f meter' % Hn
