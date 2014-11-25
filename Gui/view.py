#!/usr/bin/python
# 
# -*- coding: utf-8 -*-""

import logging
import os
from answer_entry import AnswerWidget

import sys
try:
    import pygtk
    pygtk.require("2.0")
    print 'pygtk importado'
except:
    pass
try:
    import gtk
    import gtk.glade
    print 'gtk importado'
except:
    sys.exit(1)

class GTKWindow:
    """
    Editor's windows implementation. Dedicated to the interaction with the user.
    """
    def __init__(self):
        """
        Initialize editor windows without parameters
        """
        # Crear interfaz de usuario
        self.builder = gtk.Builder()
        self.builder.add_from_file("view.glade")
        # Almacenar referencias a los controles
        # a los que se necesita acceder en el codigo
        self.name_test = self.builder.get_object("name_entry")
        self.num_questions = self.builder.get_object("nquests_info")
        self.quests_list = self.builder.get_object("quests_store")
        self.quest_label = self.builder.get_object("quest_label")
        self.wording = self.builder.get_object("wording_entry")
        self.answers_list = gtk.ListStore(self.builder.get_object("answers_store"))
        self.correct_answers = self.builder.get_object("correct_answer_label")
        self.point_correct = self.builder.get_object("correct_spin")
        self.point_wrong = self.builder.get_object("wrong_spin")
        self.point_na = self.builder.get_object("na_spin")
        print 'variables de la vista acopladas'

        # Enlazar eventos con los manejadores de eventos
        # TODO enlazar eventos con funciones del programa
        eventos = {
        "on_view_delete_event": gtk.main_quit,
        "on_new_activate" : self.none ,
        "on_open_activate" : self.none ,
        "on_save_activate" : self.none ,
        "on_save_as_activate" : self.none ,
        "on_quit_activate" : gtk.main_quit ,
        "on_quit_select" : gtk.main_quit ,
        "on_quest_add_clicked" : self.none ,
        "on_quest_rm_clicked" : self.none ,
        "on_quests_list_select_cursor_row" : self.none ,
        "on_answer_add_clicked" : self.none ,
        "on_answer_rm_clicked" : self.none
        }
        self.answers_list.append(self.create_answer_container())
        self.builder.connect_signals(eventos)

        self.num_questions.set_text(str(0))
        self.correct_answers.set_text("")

        logging.info('eventos conectados')

        
    def none(self,widget,data=None):
        """
        Sample event method in which by an OS's notifications it show which widget has the event
        :param widget:
        :param data:
        """
        os.system("notify-send \"Evento en\" \"{}\"".format(widget))
        pass

    def main(self):
        """
        Run the main loop of the aplication
        """
        print 'ejecutando main() '
        gtk.main()
        print "fin"

    def create_answer_container(self):
        box = gtk.HBox()
        check = gtk.CheckButton()
        answer_entry = gtk.Entry()
        box.pack_start(check,expand=False,fill=False)
        box.pack_end(answer_entry)
        return tuple([box])


if __name__ == "__main__":
    window = GTKWindow()
    window.main()
