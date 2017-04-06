# -*- coding: UTF-8 -*- 
class Person:
    '''represents a person,'''
    population = 0

    def __init__(self, name):
        '''initializes the person's data'''
        self.name = name
        print
        '(initia lizing %s)' % self.name
        Person.population += 1

    def __del__(self):
        '''i am dying.'''
        print
        '%s says bye' % self.name

        Person.population -= 1

        if Person.population == 0:
            print
            'i am the last one'
        else:
            print
            'there are still %d people left.' % Person.population

    def sayHi(self):
        '''Greeting by the person.
         Really,that's all it does.'''
        print
        'hi,my name is %s.' % self.name

    def howMany(self):
        '''Prints the curren tpopulation.'''
        if Person.population == 1:
            print
            'iam the only person here'
        else:
            print
            'we have %d persons here' % Person.population


swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('abdulKalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()
