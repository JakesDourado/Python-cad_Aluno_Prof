from DAO import turmaDAO

def solicitar_cadastrar_turma(turma):
	turmaDAO.cadastrar_turma_DAO(turma)

def solicitar_listar_turmas():
	return turmaDAO.listar_turmas_DAO()

def solicitar_editar_turma(nometurmaEditar, novoNometurma):
	turmaDAO.editar_turma_DAO(nometurmaEditar, novoNometurma)

def solicitar_excluir_turma(nometurmaExcluir):
	turmaDAO.excluir_turma_DAO(nometurmaExcluir)