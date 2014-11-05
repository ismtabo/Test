#!/usr/bin/env python
#  
# -*- coding: utf-8 -*-


class Read:
	"""
		Interfaz de la entrada y salida del programa.
	"""
	def __init__(self,path,rwa='r',coding='utf-8'):
		"""
			Inicializa una instancia de la clase
		"""
		if path.split('/')[-1].split('.')[-1]=='csv':
			self.path = path
			self.rwa = rwa
			self.format = format
		else:
			raise IOError('File path is not a csv file')

	def getContent(self):
		"""
			Lee el fichero de la clase y separa las lineas y los elementos de cada linea del csv
			con el separador ';;'
		"""
		with open(self.path, self.rwa) as testfile:
			lines = testfile.readlines()
		lines = [line.rstrip('\n') for line in lines]
		infor = lines[0].split(';;')
		questions = map(lambda x: x.split(';;'),lines[1:])
		testfile.close()
		return infor,questions

