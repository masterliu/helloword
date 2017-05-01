# -*- coding: UTF-8 -*-
# 选择框是否被勾选
from tkinter import *

root = Tk()

v = IntVar()
c = Checkbutton(root, text="test", variable=v)
c.pack()

l = Label(root, textvariable=v)
l.pack()

mainloop()
