# -*- coding:UTF-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name= name
        self.score= score

    def print_score(self):
        print '%s:%s' %(self.name,self,score)

bart = Student('bart is',59)
bart.print_score()        