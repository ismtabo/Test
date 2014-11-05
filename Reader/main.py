#!/usr/bin/env python
#  
# -*- coding: utf-8 -*-

from readfile import Read
from tests import Test

def run(test):
	"""
		Ejecuta el test. Mostrando las preguntas y pidiendo la respuesta del usuario.
		param: test
	"""
	list_msg = ["Introduzca su respuesta o '0' para no contestar: ", "Introduzca sus respuestas separadas por comas(puede haber ninguna respuesta correcta) o '0' para no contestar: "]
	for qkey in range(1, test.getNumQuestions() + 1):
		pregunta = test.getQuestions(qkey)
		multiple = pregunta.getMultiple()
		print str(qkey) + ':' + (' [RM] ' if multiple else ''),
		print pregunta.getPregunta()

		for akey in sorted(pregunta.getRespuestas().keys()):
			print "{}) {}".format(akey, pregunta.respuestas[akey][1])
			
		msg = list_msg[(int)(multiple)] 
		user_answer = raw_input(msg)
		while (not pregunta.respuesta_valida(user_answer) and not user_answer == str(0)):
			user_answer = raw_input("(Entrada incorrecta) Intentelo de nuevo: ")
		
		user_answer = '-'.join(user_answer.split(',')) if multiple else user_answer
		print test.getQResult(qkey, user_answer)
		print ""

def main():
	"""
		Prodecimiento principal del programa
		TODO: Bucle infinito que te permita elegir otro test(o el mismo) al acabar el presente
	"""
	correct_path = True
# 	path = raw_input('Introduzca el nombre (o ruta) de su fichero de test\'.csv\':')
#  	path = 'testPOO.csv'
	path = 'testEDA.csv'
	try:
		io = Read(path)
	except IOError:
		correct_path = False
	else:
		correct_path = True
	while(not correct_path):
		path = raw_input("Introduzca la direccion del fichero: ")
		try:
			io = Read(path)
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

