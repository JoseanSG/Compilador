import re

f = open('CodigoMamalon.txt','r')
code = f.read()
f.close()

tot_digitos = len(code)
cont = 0
line = 1
tokens = []

class Token:
	def __init__(self, tipo, lexema):
		self.tipo = tipo
		self.lexema = lexema
	def print(self):
		return self.tipo + " " + self.lexema
		
while cont  < tot_digitos:
	buff = ""
	if code[cont] == "(":
		token = Token("simbolo_de_(","(")
		print(token.print())
		tokens.append(token)

	elif code[cont] == ")": 
		token = Token("simbolo_de_)",")")
		print(token.print())
		tokens.append(token)

	elif code[cont] == "==":
		token = Token("simbolo_de_comparacion","==")
		print(token.print())
		tokens.append(token)

	elif code[cont] =="=":
		token = Token("simbolo_de_asignacion","=")
		print(token.print())
		tokens.append(token)

	elif code[cont] == "+":
		token = Token("simbolo_de_+","+")
		print(token.print())
		tokens.append(token)

	elif code[cont] == '"':
		token = Token('simbolo_de_"','"')
		print(token.print())
		tokens.append(token)

	elif re.match('\w', code[cont]):

		while re.match('\w', code[cont]):
			if cont == (tot_digitos - 1):
				break
			buff = buff + code[cont]
			cont = cont + 1

		if buff =="Begin":
			token = Token("palabra_reservada","Begin")
			print(token.print())
			tokens.append(token)

		elif buff == "Nucleo":
			token = Token("palabra_reservada","Nucleo")
			print(token.print())
			tokens.append(token)

		elif buff == "Si":
			token = Token("palabra_reservada","Si")
			print(token.print())
			tokens.append(token)

		elif buff == "Imprimir":
			token = Token("palabra_reservada","Imprimir")
			print(token.print())
			tokens.append(token)

		elif buff == "Fin":
			token = Token("palabra_reservada","Fin")
			print(token.print())
			tokens.append(token)

	cont = cont + 1
print(len(tokens))
# patron = re.compile(r'\W+')
# palabras = patron.split(code)
# print(palabras)