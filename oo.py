class Pessoa:
    
	nome = ''
	idade = -1
	
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade
		
	def comer(self, comida):
		print('Comendo ' + comida)
		
class Estudante(Pessoa):
	curso = ''
	
	def __init__(self, curso, nome, idade):
		super().__init__(nome,idade)
		self.curso = curso
		
	def comer(self, comida):
		print('Estou no RU')
		super().comer(comida)
	def printa(self):
	    print('Cursa ' + self.curso)
   
jeraudo = Estudante('Engenharia de Agrimensura', 'jeraudo', 78)
tipo = type(jeraudo)
print(tipo)
booleano = isinstance(jeraudo,Estudante)
print(booleano)
jeraudo.comer('bixcoito')
jeraudo.printa()
    
