from Model.pessoa import Pessoa

class Aluno(Pessoa):
	
	def __init__(self, nome, idade, cpf, matricula):
		super().__init__(nome, idade, cpf)
		self.__matricula = matricula
		self.__turmas = []

	def mostraTurmas(self):
		aux = []
		for turma in self.getTumas():
			aux.append(turma.getNome())
		return aux

	def __str__ (self):
		return '{} - {} - {} - {} - [Matriculado {}]'.format(self.getNome(), self.getIdade(), self.getCpf(), self.getMatricula(), self.mostraTurmas())

	def realizar_matriula(self, turma):
		self.__turmas.append(turma)
	
	def getTumas(self):
		return self.__turmas
	
	def getMatricula(self):
		return self.__matricula

	def setMatricula(self, matricula):
		self.__matricula = matricula

		