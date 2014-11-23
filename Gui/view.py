#!/usr/bin/python
# 
# -*- coding: utf-8 -*-
import logging
import os

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
    def __init__(self):
        # Crear interfaz de usuario
        self.builder = gtk.Builder()
        self.builder.add_from_file("view.glade")
        # Almacenar referencias a los controles
        # a los que se necesita acceder en el codigo
        self.name_test = self.builder.get_object("name_entry")
        self.num_questions = self.builder.get_object("nquests_info")
        self.quests_list = self.builder.get_object("quests_list")
        self.quest_label = self.builder.get_object("quest_label")
        self.wording = self.builder.get_object("wording_entry")
        self.answers_list = self.builder.get_object("answers_list")
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
        self.builder.connect_signals(eventos)

        self.num_questions.set_text(str(0))
        self.correct_answers.set_text("")

        logging.info('eventos conectados')

        
    def none(self,widget,data=None):
        os.system("notify-send \"Evento en\" \"{}\"".format(widget))
        pass

    def main(self):
        print 'ejecutando main() '
        gtk.main()
        print "fin"


if __name__ == "__main__":
    window = GTKWindow()
    window.main()
