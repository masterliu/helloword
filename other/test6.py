# -*- coding: UTF-8 -*-
'''

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'student object (name: %s)' % self.name

print Student('michael')

'''

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return  self

    def next(self):
        self.a,self.b,self.a+self.b
        if self.a >10000:
            raise StopIteration();
        return self.a
