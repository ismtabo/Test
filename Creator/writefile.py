#!/usr/bin/env python
#
# -*- coding: utf-8 -*-

class Write:
    """
    Implementacion de la entrada y salida del programa.
    """
    def __init__(self, path, rwa='r', coding='utf-8'):
        if path.split('/')[-1].split('.')[-1] == 'csv':
            self.path = path
            self.rwa = rwa
            self.format = format
        else:
            self.path = ''
            self.rwa = ''
            raise IOError('File path is not a csv file')


    def setContent(self, test):
        """
		Escribe en el fichero de la clase y separa las lineas y los elementos de cada linea del csv
		con el separador ';;'
		"""
        testfile = open(self.path, self.rwa)
        infor = ';;'.join(test.getInfo())
        testfile.write(infor)
        for key in test.getQuestions().keys():
            with test.getQuestions()[key] as question:
                testfile.write("""{};;{};;{};;{}""".format(question.getPregunta(), question.getRespuestaCorrecta(),
                               question.getMultiple(),
                               ';;'.join([')'.join(question[key]) for key in question.getRespuestas().keys()])))
        testfile.close()


