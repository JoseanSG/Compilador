texto = "qwuepi qwieu oqiqwe + + + +qwe + 123 141"

tot_digitos = len(texto)
cont = 0

while cont < tot_digitos :
	buff = ""

	if (ord('a') <= ord(texto[cont]) and ord(texto[cont]) <= ord('z')) or (ord("0") <= ord(texto[cont]) and ord(texto[cont]) <= ord("9")):
		while (ord('a') <= ord(texto[cont]) and ord(texto[cont]) <= ord('z')) or (ord("0") <= ord(texto[cont]) and ord(texto[cont]) <= ord("9")):
			buff = buff + texto[cont]
			cont = cont + 1;
			if cont == (tot_digitos - 1):
				buff = buff + texto[cont]
				break
		print("La palabra encontrada es",buff)
		if cont == (tot_digitos - 1):
			break

	elif texto[cont] == "+":
		print("Suma")
		cont = cont + 1
		if cont == (tot_digitos - 1):
			buff = buff + texto[cont]
			break

	elif texto[cont] == " ":
		print("Espacio")
		cont = cont + 1
		if cont == (tot_digitos - 1):
			buff = buff + texto[cont]
			break