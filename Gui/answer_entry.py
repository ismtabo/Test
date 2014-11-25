#!/usr/bin/python
# 
# -*- coding: utf-8 -*-


import pygtk
pygtk.require('2.0')
import gtk

class AnswerWidget(gtk.HBox):
    def __init__(self,parent):
        self.par = parent
        super(AnswerWidget,self).__init__()
        self.container = gtk.HBox()
        self.check = gtk.CheckButton()
        self.answer_entry = gtk.Entry()

        self.container.pack_start(self.check,expand=False,fill=False)
        self.container.pack_end(self.answer_entry)
        self.container.set_visible(True)

