from Model.pessoa import Pessoa

class Professor(Pessoa):
	def __init__(self, nome, idade, cpf, salario):
		super().__init__(nome, idade, cpf)
		self.__salario = salario
		self.__turmas = []

	def __str__(self):
		return '{} - {} - {} - [Turmas {}]'.format(self.getNome(), self.getIdade(), self.getCpf(), self.mostraTurmas())

	def registrar_turma(self, turmas):
		self.__turmas.append(turmas)

	def mostraTurmas(self):
		aux = []
		for turma_elemento in self.getTurmas():
			aux.append(turma_elemento.getNome())
		return aux

	def getTurmas(self):
		return self.__turmas

	def setTurmas(Self, turmas):
		self.__turmas = turmas

	def getSalario(self):
		return self.__salario

	def setSalario(self, salario):
		self.__salario = salario
