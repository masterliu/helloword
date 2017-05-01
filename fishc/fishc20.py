# -*- coding: UTF-8 -*-

from tkinter import *


def callback():
    var.set("不信18周岁不让看")


root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("18周岁不让看的内容")
textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="18.png")
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text="已满18周岁", command=callback)
theButton.pack()
frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()
