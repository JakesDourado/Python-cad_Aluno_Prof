lista_alunos = []

def cadastrar_aluno_DAO(aluno):
	lista_alunos.append(aluno)

def listar_alunos_DAO():
	return lista_alunos

def editar_aluno_DAO(nomeAlunoEditar, novoNomeAluno):
	for aluno_elemento in lista_alunos:
		if(aluno_elemento.getNome() == nomeAlunoEditar):
			aluno_elemento.setNome(novoNomeAluno)

def excluir_aluno_DAO(nomeAlunoExcluir):
	for i, aluno_elemento in enumerate(lista_alunos):
		if(aluno_elemento.getNome() == nomeAlunoExcluir):
			del(lista_alunos[i])


