#!/usr/bin/env python
#  
# -*- coding: utf-8 -*-

from random import shuffle
from pregunta import Pregunta


#Constantes:
RIGHT = 'r'
WRONG = 'w'
EMPTY = 'e'
NAME = 'name'
NQUESTIONS = 'nq'

msg = {RIGHT: "Respuesta correcta", WRONG: "Respuesta incorrecta", EMPTY: "Respuesta sin contestar"}
marks = {9.0:"Matricula", 8.0: "Sobresaliente", 7.0:"Notable", 6.0:"Aprobado", 5.0:"Suficiente", -1.0:"Suspenso"}
info_cabecera = ['name', 'nq', RIGHT, WRONG, EMPTY]

class Test:
	"""
		Implementacion de un Test con preguntas de seleccion unica:
			Atributos:
				info = diccionario de la informacion del Test
				preguntas = list<Preguntas> 
	"""

	def __init__(self,info,content):
		"""
			Inicializa una instancia de Test
		"""
		info = [info[i] if not i > 0 else ((int)(info[i]) if not i > 1 else (float)(info[i])) for i in range(len(info))]
		self.info = dict(zip(info_cabecera,info))
		self.content = [Pregunta(i[0],i[1],i[3:],i[2]) for i in content]
		shuffle(self.content)
		self.content = dict(zip(range(1,len(self.content)+1),self.content))
		self.counter = {RIGHT:0,WRONG:0,EMPTY:0}
		
	
	def getQuestions(self,key):
		"""
			Getter de la instancia de Pregunta correspondiente
			param: key - indice de la pregunta
		"""
		return self.content[key]

	def getNumQuestions(self):
		"""
			Getter del numero de preguntas del test
		"""
		return self.info[NQUESTIONS]
	
	def getQResult(self,key,answer):
		"""
			Dada la respuesta del usuario y la id de la pregunta incrementa el correspondiente
		"""
		result = 0
		if(answer==str(0)):
			result = EMPTY
		elif (self.content[key].correcta(answer)):
			result = RIGHT
		else:
			result = WRONG
		self.counter[result] += 1
		print 'result:',result
		return msg[result],':',(self.content[key].getRespuestaCorrecta() if result==WRONG else '')
	
	def finalResult(self):
		"""
			Devuelve el resultado final de los contadores de las respuestas y 
		"""
		return """--------------------------------------------------------
Respuestas correctas: 		{}
Respuestas incorrectas: 	{}
Respuestas sin contestar: 	{}
Nota final:			{}
Resultado:			{}
		""".format(self.counter[RIGHT],self.counter[WRONG],self.counter[EMPTY],self.nummark(),self.abcmark(self.nummark()))

	def nummark(self):
		"""
			Devuelve la nota numerica del examen de 0 a 10
		"""
		return (self.counter[RIGHT]*self.info[RIGHT]-self.counter[WRONG]*self.info[WRONG]-self.counter[EMPTY]*self.info[EMPTY])//self.getNumQuestions()*10
		
	def abcmark(self,nmark):
		"""
			Devuelve un resultado en expresion linguistica de la nota del examen
		"""
		for key in marks.keys():
			if nmark > key:
				return marks[key] 
		else:
			return marks[-1]
	


