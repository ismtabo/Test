#!/usr/bin/env python
#  
# -*- coding: utf-8 -*-

from Reader.test import Test
from writefile import Write

def run(test):
	"""
		TODO: Pedir una a una preguntas para introducir en el test, también dar la opción de corregir introducidas
		param: test
	"""
	

def main():
	"""
		Prodecimiento principal del programa
		TODO: Bucle infinito que te permita elegir otro test(o el mismo) al acabar el presente
	"""

	correct_path = True
	path = 'test.csv'
	try:
		io = Write(path)
	except IOError:
		correct_path = False
	else:
		correct_path = True
	while(not correct_path):
		path = raw_input("Introduzca la direccion del fichero: ")
		try:
			io = Write(path)
		except IOError:
			correct_path = False
		else:
			correct_path = True

	info, answers = io.getContent()

	test = Test(info, answers)

	run(test)

	print test.finalResult()
	
	return 0

if __name__ == '__main__':
	main()

