import re
f = open('CodigoMamalon.txt','r')
code = f.read()
print(code)
f.close()

tot_digitos = len(code)
cont = 0
line = 1
tokens = {}

while cont  < tot_digitos:
	if re.match('\w', code[cont]):
		print(code[cont])
		cont = cont + 1
	else:
		cont = cont + 1
	# var = code[cont]
	# if var == "\n":
	# 	print(line)
	# 	line = line + 1 
	# 	print("salto")
	# cont = cont + 1