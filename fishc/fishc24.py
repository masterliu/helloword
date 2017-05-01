# -*- coding: UTF-8 -*-
# indicatoron属性控制显示的样式是默认圆或可点击状态.
# pack(fill=X)控制显示按钮的大小样式均匀
from tkinter import *

root = Tk()
# 带框架的界面
group = LabelFrame(root, text='最好的脚本语言是?', padx=5, pady=5)
group.pack(padx=10, pady=10)

LANGS = [
    ('python', 1),
    ('Perl', 2),
    ('Ruby', 3),
    ('lua', 4)]

v = IntVar()
# v.set(1)

for lang, num in LANGS:
    # 使用带框架的选择界面.
    b = Radiobutton(group, text=lang, variable=v, value=num, indicatoron=True)
    # b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=True)
    # b.pack(fill=X)
    b.pack(anchor=W)
mainloop()
