#!/usr/bin/env python
#
# -*- coding: utf-8 -*-



from random import shuffle
from string import lowercase


class Pregunta:
    """
       Implementacion de una Pregunta:
           Atributos:
               enunciado
               correct - respuesta correct
               respuestas - lista de posibles respuestas
               multiple - True: si es pregunta de multiples respuestas
                          False: en caso contrario
    """

    def __init__(self, enunciado, correcta, respuestas, multiple):
        """
        Inicializa una instancia de Pregunta (respuesta simple por defecto)
        :param enunciado:
        :param correcta: respuesta correcta
        :param respuestas: arraylist de respuestas
        :param multiple: flag de respuesta multiple
        """
        self.enunciado = enunciado
        self.correct = correcta
        self.respuestas = respuestas
        self.respuestas = map(lambda x: x.split(')', 1), self.respuestas)
        shuffle(self.respuestas)
        self.respuestas = dict(zip(lowercase[:len(self.respuestas)], self.respuestas))
        self.multiple = (bool)((int)(multiple))

    def getPregunta(self):
        """
        :return: enunciado de la pregunta
        """
        return self.enunciado

    def getRespuestas(self):
        """
        :return: diccionario de respuestas posibles
        """
        return self.respuestas

    def getMultiple(self):
        """
        :return: flag de respuesta multiple
        """
        return self.multiple

    def getRespuestaCorrecta(self):
        """
        :return: respuesta correcta de la pregunta
        """
        return self.correct


    def getTextRespuestaCorrecta(self):
        """
        :return: respuesta(s) correcta(s) en formato de texto
        """
        return ','.join(self.correct.split('-'))

    def __str__(self):
        """
        :return: instancia de pregunta en formato de texto
        """
        return """Enunciado: {}
		Multiple:{}
Respuestas:
{}
Respuesta correcta: {}
""".format(self.enunciado, self.multiple,
           '\n'.join([(str)(respuesta[0]) + ')' + (str)(respuesta[1]) for respuesta in self.respuestas.values()]),
           self.correct)

    def correcta(self, respuesta):
        """
        :param respuesta: id de la respuesta introducida
        :return: True si la(s) respuesta(s) es/son correctas, False en caso contrario
        """
        if not self.multiple:
            return self.respuestas[respuesta][0] == self.correct
        else:
            for answer in respuesta.split('-'):
                if (answer not in self.correct.split('-')):
                    return False
            return True

    def respuesta_valida(self, respuesta):
        """
        :param respuesta: respuesta dada
        :return: True si la respuesta esta dentro del rango de las posibles respuestas, False en caso contrario.
        """
        if not self.multiple:
            return respuesta in self.getRespuestas().keys()
        else:
            for answer in respuesta.split(','):
                if answer not in self.getRespuestas().keys() and answer != '' and answer != (str)(0):
                    print answer, 'Respuesta valida?:', False
                    return False
            return True
		
		

