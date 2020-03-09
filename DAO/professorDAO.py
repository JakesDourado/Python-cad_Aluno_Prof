lista_professores = []

def cadastrar_professor_DAO(professor):
	lista_professores.append(professor)

def listar_professores_DAO():
	return lista_professores

def editar_professor_DAO(nomeprofessorEditar, novoNomeprofessor):
	for professor_elemento in lista_professores:
		if(professor_elemento.getNome() == nomeprofessorEditar):
			professor_elemento.setNome(novoNomeprofessor)

def excluir_professor_DAO(nomeprofessorExcluir):
	for i, professor_elemento in enumerate(lista_professores):
		if(professor_elemento.getNome() == nomeprofessorExcluir):
			del(lista_professores[i])
