#!/usr/bin/env python
#  
# -*- coding: utf-8 -*-



import operator
from random import shuffle
from six import iteritems
import string


class Pregunta:
	"""
		Implementacion de una Pregunta:
			Atributos:
				enunciado
				correct - respuesta correct
				respuestas - lista de posibles respuestas
	"""
	
	def __init__(self,enunciado,correcta,respuestas):
		"""
			Inicializa la instancia de pregunta con:
			enunciado = (String)
			correct = (String) id de la respuesta correct
			preguntas = list<String> respuestas posibles
		"""
		self.enunciado = enunciado
		self.correct = correcta
		# Sacamos la letra de cada respuesta
		self.respuestas = respuestas
		# ida = [answer.split(')')[0] for answer in self.respuestas]
		# stra = [answer.split(')')[1] for answer in self.respuestas]
		self.respuestas = map(lambda x: x.split(')'), self.respuestas)
		shuffle(self.respuestas)
		self.respuestas = dict(zip(string.lowercase[:len(self.respuestas)],self.respuestas))
		# print self.respuestas
		self.respuestas = dict(sorted(self.respuestas.iteritems(),key=operator.itemgetter(0)))
		# print self.respuestas
		
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

	
	def __str__(self):
		"""
			Expresion en formato string la pregunta
		"""
		return """Enunciado: {}
Respuestas:
{}
Respuesta correcta: {}
""".format(self.enunciado,'\n'.join([(str)(respuesta[0])+')'+(str)(respuesta[1]) for respuesta in self.respuestas.values()]),self.correct)
	
	
	def correcta(self,respuesta):
		"""
			Devuelve True si la respuesta introducida es la correcta
			Param: respuesta - id de la respuesta introducida
		"""
		return self.respuestas[respuesta][0] == self.correct

