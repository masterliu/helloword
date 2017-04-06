# -*- coding: UTF-8 -*-
import easygui as g
import sys

while 1:
    g.msgbox('hi,welcom play first game')

    msg = "你要学什么知识?"
    title = "mini game play"
    choices = ["love", "programe", "ooxx", 'qin']

    choice = g.choicebox(msg, title, choices)

    g.msgbox('you choud'+ str(choice),'jieguo')
    msg= "you want angin?"
    title ="please choud"

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)