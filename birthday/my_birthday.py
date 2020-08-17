#!/usr/bin/env python3

import wikipedia
import random

while True:
	shown = []
	valid = True
	birthday = input("Ingresa tu cumpleaños (DD/MM), 'q' para salir: ").split('/')
	if birthday[0] == 'q':
		break
	months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
			  9: 'September', 10: 'October', 11: 'November', 12: 'December'}
	try:
		page = f"{months[int(birthday[1])]} {int(birthday[0])}"
	except KeyError:
		print("Invalid date")
		valid = False
	if valid:
		date = wikipedia.page(page)
		print(date.url)
		try:
			births = date.section('Births').split('\n')
		except AttributeError:
			print("Fecha invalida")
			valid = False
		print(births)
		if len(births)==0:
			print("Nadie relevante nació en esa fecha :(")
			valid = False
		if all(x in shown for x in births):
			print("Ya viste todas las personas disponibles para esta fecha")
			valid = False
		if valid:
			res = births[int(random.randrange(0, len(births) - 1))]
			while res in shown:
				res = births[int(random.randrange(0, len(births) - 1))]
			shown.append(res)
			print(res)
