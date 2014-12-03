#!/usr/bin/env python
#
# -*- coding: utf-8 -*-


class IOFile:
    """
    Implementacion de la entrada y salida del programa.
    """

    def __init__(self, path, rwa='r', coding='utf-8'):
        """
        Inicializa una instancia de la clase
        :param path: directorio del fichero de test
        :param rwa: flag de formato de apertura del fichero
        :param coding: formato de codificacion del fichero
        """

        if path.split('/')[-1].split('.')[-1] == 'csv':
            self.path = path
            self.rwa = rwa
            self.format = format
        else:
            raise IOError('File path is not a csv file')

    def getContent(self):
        """
        Lee el fichero y separa las lineas y los elementos de cada linea del csv
        con el separador ';;'
        """
        testfile = open(self.path, self.rwa)
        lines = testfile.readlines()
        lines = [line.rstrip('\n') for line in lines]
        for line in range(len(lines)):
            lines[line] = lines[line].replace('\\n', '\n')
            lines[line] = lines[line].replace('\\t', '\t')
        infor = lines[0].split(';;')
        questions = map(lambda x: x.split(';;'), lines[1:])
        testfile.close()
        return infor, questions

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
                testfile.write("""{};;{};;{};;{}""".format(question.getWording(), question.getCorrectAnswers(),
                                                           question.getMultiple(),
                                                           ';;'.join([')'.join(question[key]) for key in
                                                                      question.getAnswers().keys()])))
        testfile.close()

