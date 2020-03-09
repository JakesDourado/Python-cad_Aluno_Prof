lista_turmas = []

def cadastrar_turma_DAO(turma):
	lista_turmas.append(turma)

def listar_turmas_DAO():
	return lista_turmas

def editar_turma_DAO(nometurmaEditar, novoNometurma):
	for turma_elemento in lista_turmas:
		if(turma_elemento.getNome() == nometurmaEditar):
			turma_elemento.setNome(novoNometurma)

def excluir_turma_DAO(nometurmaExcluir):
	for i, turma_elemento in enumerate(lista_turmas):
		if(turma_elemento.getNome() == nometurmaExcluir):
			del(lista_turmas[i])