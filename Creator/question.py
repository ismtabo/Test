#!/usr/bin/env python
#
# -*- coding: utf-8 -*-



class Question:
    """
    Implementation of a test question with multiple choice:
       Attributes:
           wording
           correct - correct answer
           answers - dictionary of possible answers
           multiple - True(1): if question has multiple answers
                      False(0): in another case
    """

    def __init__(self, wording, correct, answers, multiple):
        """
        Initialization of instance of Question
        :type wording: str
        :param wording:
        :type correct: str
        :param correct: correct answer
        :type answers: list
        :param answers: list of possible answers
        :type multiple: int
        :param multiple: binary flag of multiple answers property
        """
        self.wording = wording
        self.correct = correct
        self.answers = answers
        header = map(lambda x: x.split(')', 1), answers)
        header = map(lambda x: x[0], header)
        self.answers = dict(zip(header, answers))
        self.multiple = (bool)((int)(multiple))

    def getWording(self):
        """
        :return: wording of question
        """
        return self.wording

    def setWording(self, wording):
        """
        :param wording: new value for wording
        """
        self.wording = wording

    def getAnswers(self):
        """
        :return: dictionary of possible answers
        """
        return self.answers

    def setAnswers(self, answers):
        """
        :type answers: list
        :param answers: 
        :return:
        """
        tuple_answers = map(lambda x: x.split(')'), sorted(answers))
        self.answers = sorted(answers)

    def getMultiple(self):
        """
        :return: binary flag of multiple answers property
        """
        return self.multiple

    def getCorrectAnswers(self):
        """
        :return: correct answer/s of question
        """
        return self.correct


    def correctAnswerToStr(self):
        """
        :return: correct answer/s of question in str expression
        """
        return ','.join(self.correct.split('-'))

    def __str__(self):
        """
        :return: instance in str expression
        """
        return """Enunciado: {}
		Multiple:{}
Respuestas:
{}
Respuesta correcta: {}
""".format(self.wording, self.multiple,
           '\n'.join([(str)(respuesta[0]) + ')' + (str)(respuesta[1]) for respuesta in self.answers.values()]),
           self.correct)

    def isCorrectAnswer(self, id):
        """
        :param id: id/s of introduced answer/s
        :return: True if introduced answer/s are correct, False in another case
        """
        if not self.multiple:
            return self.answers[id][0] == self.correct
        else:
            for answer in id.split('-'):
                if (answer not in self.correct.split('-')):
                    return False
            return True

    def isValidAnswer(self, answer):
        """
        :param answer: given answer
        :return: True if answer is valid according to the multiple attribute and the range of possible answers
        """
        if not self.multiple:
            return answer in self.getAnswers().keys()
        else:
            for answer in answer.split(','):
                if answer not in self.getAnswers().keys() and answer != '' and answer != (str)(0):
                    print answer, 'Respuesta valida?:', False
                    return False
            return True
		
		

