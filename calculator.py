def calculator(a,op,b):
	if op == 'sum':
		return a + b
	elif op == 'sub':
		return a - b
	elif op == 'mult':
		return a * b
	elif op == 'div':
		return a / b
	elif op == 'pow':
		return a ** b
	elif op == 'rad':
		return a ** (1/b)
	else:
	    print('Comando invalido')

def main():
	op = input('Escolha a opção desejada (sum / sub / mult / div / pow / rad / SAVE / EXIT): ')
	if op == 'EXIT':
	    exit()
	a = input('Insira o primeiro valor: ')
	b = input('Insira o segundo valor: ')
	if op == 'SAVE':
	    
	print(calculator(float(a),op,float(b)))
main()
