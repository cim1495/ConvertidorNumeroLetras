
basico = ["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
decenas = ["diez","veinte","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
centenas = ["ciento","doscientos","trescientos","cuatrocientos","quinientos","seiscientos","setecientos","ochocientos","novecientos"]
especial1 = ["once","doce","trece","catorce","quince","dieciseis","diecisiete","dieciocho","diecinueve"]
especial2 = ["veintiuno","veintidos","veintitres","veinticuatro","veinticinco","veintiseis","veintisiete","veintiocho","veintinueve"]
primeros = [1,2,3,4,5,6,7,8,9]
numero = input("Dime un numero: ")
digito = len(numero)
if digito == 1:
	for i in primeros:
		if i == int(numero):
			print(basico[i-1])
elif digito == 2:
	if int(numero) == 10:
		print(decenas[0])
	elif int(numero) == 20:
		print(decenas[1])		
	elif numero[0] == "1":
		for i in primeros:
			if i == int(numero[1]):
				print(especial1[i-1])
	elif numero[0] == "2":
		for i in primeros:
			if i == int(numero[1]):
				print(especial2[i-1])
	else:
		if int(numero[1]) == 0:
				print(decenas[int(numero[0])-1])
		else:
			for i in primeros:
				if i == int(numero[0]):
					print(decenas[i-1],end=" y ")
			for i in primeros:
				if i == int(numero[1]):
					print(basico[i-1])
elif digito == 3:
	if int(numero) == 100:
		print("cien")
	elif numero[0] == "1":
		print(centenas[0],end=" ")
		if numero[1] == "1":
			if int(numero[2]) == 0:
				print(decenas[int(numero[1])-1])
			for i in primeros:
				if i == int(numero[2]):
					print(especial1[i-1])
		elif numero[1] == "2":
			if int(numero[2]) == 0:
				print(decenas[int(numero[1])-1])
			for i in primeros:
				if i == int(numero[2]):
					print(especial2[i-1])
		else:
			if int(numero[2]) == 0:
				print(decenas[int(numero[1])-1])
			else:
				for i in primeros:
					if i == int(numero[1]):
						print(decenas[i-1],end=" y ")
				for i in primeros:
					if i == int(numero[2]):
						print(basico[i-1])
	else:
		for i in primeros:
			if i == int(numero[0]):
				print(centenas[i-1],end=" ")
		if numero[1] == "1":
			if int(numero[2]) == 0:
				print(decenas[int(numero[1])-1])
			for i in primeros:
				if i == int(numero[2]):
					print(especial1[i-1])
		elif numero[1] == "2":
			if int(numero[2]) == 0:
				print(decenas[int(numero[1])-1])
			for i in primeros:
				if i == int(numero[2]):
					print(especial2[i-1])
		else:
			if int(numero[2]) == 0:
				print(decenas[int(numero[1])-1])
			else:
				for i in primeros:
					if i == int(numero[1]):
						print(decenas[i-1],end=" y ")
				for i in primeros:
					if i == int(numero[2]):
						print(basico[i-1])
elif digito == 4 and int(numero) == 1000:
	print("mil")
else:
	print("Numero fuera de rango")