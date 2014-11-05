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
	
	def __init__(self,enunciado,correcta,respuestas,multiple):
		"""
			Inicializa una instancia de Pregunta (respuesta simple por defecto)
		"""
		self.enunciado = enunciado
		self.correct = correcta
		self.respuestas = respuestas
		self.respuestas = map(lambda x: x.split(')',1), self.respuestas)
		shuffle(self.respuestas)
		self.respuestas = dict(zip(lowercase[:len(self.respuestas)],self.respuestas))
		self.multiple = (bool)((int)(multiple))
		
	def getPregunta(self):
		"""
			Getter del enunciado de la pregunta
		"""
		return self.enunciado

	def getRespuestas(self):
		"""
			Getter del diccionario de respuestas posibles
		"""
		return self.respuestas
	
	def getMultiple(self):
		"""
			Getter del atributo respuesta multiple de la pregunta
		"""
		return self.multiple

	def getRespuestaCorrecta(self):
		"""
			Getter de la respuesta correcta de la pregunta
		"""
		return ','.join(self.correct.split('-'))
	
	def __str__(self):
		"""
			Expresion en formato string la pregunta
		"""
		return """Enunciado: {}
		Multiple:{}
Respuestas:
{}
Respuesta correcta: {}
""".format(self.enunciado,self.multiple,'\n'.join([(str)(respuesta[0])+')'+(str)(respuesta[1]) for respuesta in self.respuestas.values()]),self.correct)
	
	
	def correcta(self,respuesta):
		"""
			Devuelve True si la respuesta introducida es la correcta
			
			Param: respuesta - id de la respuesta introducida
		"""
		if not self.multiple:
			return self.respuestas[respuesta][0] == self.correct
		else :
			for answer in respuesta.split('-'):
				if(answer not in self.correct.split('-')):
					return False
			return True
	
	def respuesta_valida(self,respuesta):
		"""
			True: respuesta esta dentro de diccionario de las respuestas posibles
			False: en caso contrario
			
			Param: answer - respuesta dada
		"""
		if not self.multiple:
			return respuesta in self.getRespuestas().keys()
		else:
			for answer in respuesta.split(','):
				if answer not in self.getRespuestas().keys() and answer != '' and answer != (str)(0):
					print answer,'Respuesta valida?:',False
					return False
			return True
		
		

