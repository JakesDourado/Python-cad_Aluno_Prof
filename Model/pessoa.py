class Pessoa(object):
	def __init__(self, nome, idade, cpf):
		self.__nome = nome
		self.__idade = idade
		self.__cpf = cpf

	def __str__ (self):
		return '{} - {} - {}'.format(self.getNome(), self.getIdade(), self.getCpf())

	def getNome(self):
		return self.__nome

	def getIdade(self):
		return self.__idade
	
	def getCpf(self):
		return self.__cpf

	def setNome(self, nome):
		self.__nome = nome

	def setCpf(self, cpf):
		self.__cpf = cpf

	def setIdade(self, idade):
		self.__idade = idade
