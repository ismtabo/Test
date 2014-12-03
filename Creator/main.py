#!/usr/bin/env python
#
# -*- encoding: utf-8 -*-

import string

from libio import IOFile
from test import Test
from question import Question


MAIN_OPTIONS = """
Elija una de las siguientes opciones:
o .Abrir test
n .Crear test
{}
--------------------
c .Cerrar test
q .Salir
--------------------
{}

Su opcion: """

SAVE_OPTIONS = """s .Guardar
ss .Guardar como..."""

EDIT_OPTIONS = """i .Mostrar informacion del test
ie .Editar informacion
--------------------
l .Listar preguntas
qn .Nueva pregunta
qe .Editar pregunta
qs .Mostrar pregunta
--------------------"""

EDIT_QUESTION_OPTIONS = """--------------------
i .Mostrar pregunta
w .Mostrar enunciado
we .Editar enunciado
--------------------
a .Mostrar respuestas posibles
aa .A""" + u'\u00F1' + """adir respuestas posibles
ra .Eliminar respuesta
--------------------
c .Mostrar respuestas correctas
ec .Editar respuestas correctas
--------------------
m .Mostrar respuesta multiple
e .Editar respuesta multiple
"""


class TestMng:
    """
    Implementation of test manager to edit an existing one or create a new one.
    Attributes:
        test: current test
        quest: current question of the test
        io_mng: Input/output manager
        modified: flag that indicates if test has been modified
    """

    def __init__(self):
        """
        Inicialize an instance without arguments
        """
        self.test = None
        self.quest = None
        self.io_mng = None
        self.modified = False
        self.functions = {'o': self.open, 'n': self.new, 's': self.save, 'ss': self.save_as, 'c': self.close,
                          'i': self.show_info, 'ie': self.edit_info, 'l': self.list_quest, 'qn': self.new_question,
                          'qe': self.edit_question, 'qs': self.show_question}

    def run(self):
        """
        Main loop of the mng
        TODO: Bucle infinito que te permita elegir otro test(o el mismo) al acabar el presente
        """
        answer = raw_input(
            MAIN_OPTIONS.format(SAVE_OPTIONS if self.modified else '', EDIT_OPTIONS if self.answer is not None else ''))
        while (answer != 'q'):
            if answer in self.functions.keys():
                function = self.functions[answer]
                function()
            else:
                answer = raw_input('ERROR:Eleccion no existente\n. Introduzcalo de nuevo:')

    def open(self):
        """
        Open test file
        """
        path = raw_input('Introduzca la ruta del fichero: ')
        self.io_mng = IOFile(path)
        info, content = self.io_mng.getContent()
        self.test = Test(info, content)

    def new(self):
        """
        Create new test file
        """
        name = raw_input('Introduzca nombre de test: ')
        number = raw_input('Intoduzca numero de preguntas: ')
        correct_pnt = TestMng.validate_input(int, 'Introduzca los puntos por respuesta isCorrectAnswer: ')
        wrong_pnt = TestMng.validate_input(int, 'Introduzca los puntos por respuesta incorrecta: ')
        empty_pnt = TestMng.validate_input(int, 'Introduzca los puntos por respuesta no contestada: ')
        self.test = Test([name, number, correct_pnt, wrong_pnt, empty_pnt], [])
        self.modified = False
        self.question = None

    def save(self):
        """
        Save the current test in the source file
        """
        if self.test.getLenQuestions() > self.test.getNumQuestions():
            print 'Numero de posibles preguntas insuficientes para el test.'
            return
        if self.io_mng == None:
            self.io_mng = IOFile(self.test.getName() + '.csv')
        self.io_mng.setContent(self.test)

    def save_as(self):
        """
        Save the current test in another file
        """
        name = raw_input('Introduzca nuevo nombre del fichero: ')
        path = raw_input('Introduzca ruta del fichero (directiorio HOME por omision): ')
        self.io_mng = IOFile('/'.join([path, name]))
        self.save()

    def close(self):
        """
        Close current test
        """
        if self.modified:
            save = raw_input('Se ha realizado cambios en el test, desea guardarlos?(y/N): ')
            if save == 'y':
                self.save()
        self.test = None
        self.io_mng = None

    def show_info(self):
        """
        Editing test information
        """
        print """Nombre: {}
Preguntas por test: {}
Puntos por respuesta...
    Correcta: {}
    Incorrecta: {}
    No contestada: {}
    """.format(self.test.getName(), self.test.getNumQuestions(), self.test.getCorrectPoints(),
               self.test.getWrongPoitns(), self.test.getEmptyPoints())

    def edit_info(self):
        """
        Editing test infromation
        """
        new_name = raw_input(
            'Nombre anterior: {}\nNuevo nombre(no cambia en caso de omision):\n'.format(self.test.getName()))
        if new_name != '':
            self.test.setName(new_name)
        new_nquestions = TestMng.validate_input(int,
                                                'Numero de preguntas anterior: {}\nNuevo numero de preguntas(no cambia en caso de omision):\n'.format(
                                                    self.test.getNumQuestions()))
        if new_nquestions != '':
            self.test.setName(new_nquestions)
        new_c_point = TestMng.validate_input(float,
                                             'Puntos pregunta isCorrectAnswer anterior: {}\nNuevos puntos pregunta isCorrectAnswer(no cambia en caso de omision):\n'.format(
                                                 self.test.getCorrectPoints()))
        if new_c_point != '':
            self.test.setName(new_c_point)
        new_w_punt = TestMng.validate_input(float,
                                            'Puntos pregunta incorrecta anterior: {}\nNuevo puntos pregunta incorrecta(no cambia en caso de omision):\n'.format(
                                                self.test.getWrongPoitns()))
        if new_w_punt != '':
            self.test.setName(new_w_punt)
        new_e_punt = TestMng.validate_input(float,
                                            'Puntos pregunta no contestada anterior: {}\nNuevo puntos pregunta no contestada(no cambia en caso de omision):\n'.format(
                                                self.test.getEmptyPoints()))
        if new_e_punt != '':
            self.test.setName(new_e_punt)

    def list_quest(self):
        """
        List all the questions of the current test
        """
        with self.test.getQuestions() as questions:
            for i in range(1, len(questions)):
                print '---------------'
                print '#' + str(i) + '.\n', questions[i]

    def new_question(self):
        """
        Inser new question in current test
        """
        self.question = Question_Mng()
        self.test.setNewQuestion(self.question.getQuestion())

    def edit_question(self):
        """
        Edit question identified by number of the current test
        """
        index = TestMng.validate_input(int, 'Introduzca numero de pregunta: ')
        self.question = Question_Mng(self.test.getQuestion(index))
        # TODO: anyadir pregunta a test

    def show_question(self):
        """
        Show question identified by number of the current test
        """
        index = TestMng.validate_input(int, 'Introduzca numero de pregunta: ')
        print self.test.getQuestion(index)

    @staticmethod
    def validate_input(conversion, msg='', notblank=False):
        """
        Validate user input by raw_input printing msg

        :param type: type to validate the input
        :param msg: message to show

        :return: validate input
        """
        valid = False
        input = ''
        while not valid:
            try:
                input = raw_input(msg)
                if input != '':
                    input = conversion(input)
                    valid = True
            except ValueError:
                pass
        return input


class Question_Mng:
    """
    Implementation of question manager to edit an existing one or create a new one.
    """

    def __init__(self, *question):
        """
        Initialization of class instance with parameter
        :type question: Question
        :param question: current question to manage
        """
        self.question = question
        if self.question is None:
            self.new_question()
        self.abc_list = string.ascii_lowercase
        self.functions = {}

    def getQuestion(self):
        """
        :return: current question
        """
        return self.question

    def new_question(self):
        """
        Create new instance of Question in attribute question
        """
        wording = raw_input('Introduzca enunciado de la pregunta:\n')
        multiple = raw_input('Es de respuesta multiple?(s/N):')
        multiple = 1 if multiple == 'y' else 0
        answers = []
        self.add_questions(answers)
        if multiple:
            msg = ' las letras de las respuestas correctas separadas por comas(ej: a,b): '
        else:
            msg = 'la letra de la respuesta isCorrectAnswer (ej:a): '
        correct = raw_input('Introduzca {}'.format(msg))
        self.question = Question(wording, correct, answers, multiple)

    def set_quetion(self, question):
        """
        :type question: Question
        :param question: new current question
        """
        self.question = question

    def edit_question(self):
        """
        Loop in which user is able to edit attributes of current question
        """
        # TODO terminar metodo


    def add_questions(self, answer_list):
        """
        Loop in which user is able to add possible answer to the current question
        :type answer_list: list
        :return answers: list of possible answers
        """
        last = False
        abc_index = len(answer_list)
        print 'Introduzca las respuestas por orden introduciendo una respuesta vacia para terminar:'
        while (not last):
            answer = raw_input('{}) '.format(self.abc_list[abc_index]))
            if answer != '':
                answer_list.append(self.abc_list[abc_index] + ')' + answer)
            else:
                last = True

    def show_wording(self):
        """
        Show wording of current question
        """
        print self.question.getWording()

    def edit_wording(self):
        """
        Edit wording of current question
        """
        # self.question.
        # TODO: Pensar caso en el que se borre una de las posibles respuestas que no se a la ultima(necesaria reordenacion)


if __name__ == '__main__':
    mng = TestMng()
    mng.run()

