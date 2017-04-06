# -*- coding: UTF-8 -*-
class C:
    def __getattribute__(self, item):
        print('getattribute')
        return super().__getattribute__(name)

    def __getattr__(self, item):
        print('getattr')

    def __setattr__(self, key, value):
        print('setattr')
        super().__setattr__(name, value)

    def __delattr__(self, item):
        print('delattr')
        super().__delattr__(name)
