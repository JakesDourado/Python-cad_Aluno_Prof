from DAO import alunoDAO

def solicitar_cadastrar_aluno (aluno):
	alunoDAO.cadastrar_aluno_DAO(aluno)

def solicitar_listar_alunos():
	return alunoDAO.listar_alunos_DAO()

def solicitar_editar_aluno(nomeAlunoEditar, novoNomeAluno):
	alunoDAO.editar_aluno_DAO(nomeAlunoEditar, novoNomeAluno)

def solicitar_excluir_aluno(nomeAlunoExcluir):
	alunoDAO.excluir_aluno_DAO(nomeAlunoExcluir)