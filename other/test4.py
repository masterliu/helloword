class MyObject(object):
    def __init__(self):
        self.__x = None

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x


if __name__ == '__main__':
    c = MyObject()
    c.x = 100
    y = c.x
    print('set & get y: %d' % y)

    del c.x
    print('del c.x & y: %d' % y)
