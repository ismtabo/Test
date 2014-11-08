#!/usr/bin/env python
#  
# -*- coding: utf-8 -*-


class Read:
	"""
	Implementacion de la entrada y salida del programa.
	"""
	def __init__(self,path,rwa='r',coding='utf-8'):
		"""
		Inicializa una instancia de la clase
		:param path: directorio del fichero de test
		:param rwa: flag de formato de apertura del fichero
		:param coding: formato de codificacion del fichero
		"""
		if path.split('/')[-1].split('.')[-1]=='csv':
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
		with open(self.path, self.rwa) as testfile:
			lines = testfile.readlines()
		lines = [line.rstrip('\n') for line in lines]
		infor = lines[0].split(';;')
		questions = map(lambda x: x.split(';;'),lines[1:])
		testfile.close()
		return infor,questions

