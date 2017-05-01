# -*- coding: UTF-8 -*-
# TKUI框架

from tkinter import *

root = Tk()

textLable = Label(root, text="18禁哦,\n长大了再来看吧",
                  justify=LEFT,
                  padx=10)
textLable.pack()

photo = PhotoImage(file="18.png")
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)

mainloop()
