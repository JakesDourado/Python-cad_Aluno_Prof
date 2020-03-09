class Turma(object):
	def __init__(self, nome, periodo, professor):
		self.__nome = nome
		self.__periodo = periodo
		self.__professor = professor
		self.__alunos = []


	def __str__(self):
		return '{} - {} - {} - [Alunos {}]'.format(self.getNome(), self.getPeriodo(), self.getProfessor(), self.mostraAlunos())

	def mostraAlunos(self):
		aux = []
		for aluno in self.getAlunos():
			aux.append(aluno.getNome())
		return aux

	def getAlunos(self):
		return self.__alunos

	def matricular_aluno(self, aluno):
		self.__alunos.append(aluno)

	def getNome(self):
		return self.__nome

	def getPeriodo(self):
		return self.__periodo

	def getProfessor(self):
		return '[Professor: {} - {}]'.format(self.__professor.getNome(), self.__professor.getCpf())

	def setNome(self, nome):
		self.__nome = nome

	def setPeriodo(self, periodo):
		self.__periodo = periodo

	def setProfessor(self, professor):
		self.__professor = professor