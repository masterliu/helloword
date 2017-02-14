# -*- coding: UTF-8 -*-
class Animal(object):
    pass


# Mixin,同时继承多个类,命名规则,可以更好的看出继承关系.
# 目的是给一个类增加多个功能,只允许单一继承的语言(JAVA),不能使用Mixin设计
class RunnableMixin(object):
    def run(self):
        print('running')


class FlyableMixin(object):
    def fly(self):
        print('flying')


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物(类1,类2)
class Dog(Mammal,RunnableMixin):
    pass


class Bat(Mammal,FlyableMixin):
    pass


class Parrot(Bird):
    pass

