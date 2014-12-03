#!/usr/bcontentn/env python
#
# -*- coding: utf-8 -*-

from random import shuffle

from question import Question



# Constantes:
RIGHT = 'r'
WRONG = 'w'
EMPTY = 'e'
NAME = 'name'
NQUESTIONS = 'nq'

msg = {RIGHT: "Respuesta isCorrectAnswer", WRONG: "Respuesta incorrecta", EMPTY: "Respuesta sin contestar"}
marks = {9.0: "Matricula", 8.0: "Sobresaliente", 7.0: "Notable", 6.0: "Aprobado", 5.0: "Suficiente", -1.0: "Suspenso"}
info_header = [NAME, NQUESTIONS, RIGHT, WRONG, EMPTY]


class Test:
    """
	Implementation fo multiple choice option:
    Attributes:
        info = Test information dictionary
        questions = list of instances of Question
	"""

    def __init__(self, info, content):
        """
		Initialized an instance of Test with parameters
		:param info: information of test
		:param content: lista of questions of test
		"""
        info = [info[i] if not i > 0 else ((int)(info[i]) if not i > 1 else (float)(info[i])) for i in range(len(info))]
        self.info = dict(zip(info_header, info))
        self.content = [Question(i[0], i[1], i[3:], i[2]) for i in content]
        shuffle(self.content)
        self.counter = {RIGHT: 0, WRONG: 0, EMPTY: 0}

    def getInfo(self):
        """
        :return: information of the test
        """
        return self.info

    def getName(self):
        """
        :return: name of the test
        """
        return self.info[NAME]


    def setName(self, name):
        """
        :param name: new name of test
        """
        self.info[NAME] = name


    def getNumQuestions(self):
        """
        :return: number of question by test
        """
        return self.info[NQUESTIONS]


    def setNumQuestions(self, numquestions):
        """
        :param numquestions: new number of question by test
        """
        self.info[NQUESTIONS] = numquestions

    def getCorrectPoints(self):
        """
        :return: value of points by correct answer
        """
        return self.info[RIGHT]

    def setCorrectPoints(self, point):
        """
        :param point: new value of points by correct answer
        """
        self.info[RIGHT] = point

    def getWrongPoitns(self):
        """
        :return: value of points by wrong answer
        """
        return self.info[WRONG]

    def setWrongPoints(self, point):
        """
        :param point: new value of points by wrong answer
        """
        self.info[WRONG] = point

    def getEmptyPoints(self):
        """
        :return: value of points by empty answer
        """
        return self.info[EMPTY]

    def setEmptyPoints(self, point):
        """
        :param point: new value of points by empty answer
        """
        self.info[EMPTY] = point

    def getQuestion(self, key):
        """
        :param key: question id
        :return: question identified by key
        """
        return self.content[key]

    def setNewQuestion(self, question):
        """
        :param question: new questions
        """
        self.content.append(
            question if isinstance(question, Question) else Question(question[0], question[1], question[3:],
                                                                     question[2]))

    def getQuestions(self):
        """
        :return: all posible questions of content
        """
        return self.content

    def getLenQuestions(self):
        """
        :return: number of all posible questions
        """
        return len(self.content)

    def getQResult(self, key, answer):
        """
        From question id an user answer returns the correspondent message
        :param key: question id
        :param answer: user answer
        :return: str with question result
        """
        result = 0
        if (answer == str(0)):
            result = EMPTY
        elif (self.content[key].isCorrectAnswer(answer)):
            result = RIGHT
        else:
            result = WRONG
        self.counter[result] += 1
        # print 'result:', result
        return msg[result] + ' : ' + (self.content[key].correctAnswerToStr() if result == WRONG else '')


    def finalResult(self):
        """
        :return: str with de final result of the test
        """
        return """--------------------------------------------------------
    Respuestas correctas: 		{}
    Respuestas incorrectas: 	{}
    Respuestas sin contestar: 	{}
    Nota final:			{}
    Resultado:			{}
            """.format(self.counter[RIGHT], self.counter[WRONG], self.counter[EMPTY], self.nummark(),
                       self.abcmark(self.nummark()))


    def nummark(self):
        """
        :return: numeric mark of the test's result
        """
        return (self.counter[RIGHT] * self.info[RIGHT] - self.counter[WRONG] * self.info[WRONG] - self.counter[EMPTY] *
                self.info[EMPTY]) // self.getNumQuestions() * 10


    def abcmark(self, nmark):
        """
        :return: test's qualification express an alphabetical expression
        """
        for key in marks.keys():
            if nmark > key:
                return marks[key]
        else:
            return marks[-1]



	


