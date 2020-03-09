from DAO import professorDAO

def solicitar_cadastrar_professor(professor):
	professorDAO.cadastrar_professor_DAO(professor)

def solicitar_listar_professores():
	return professorDAO.listar_professores_DAO()

def solicitar_editar_professor(nomeprofessorEditar, novoNomeprofessor):
	professorDAO.editar_professor_DAO(nomeprofessorEditar, novoNomeprofessor)

def solicitar_excluir_professor(nomeprofessorExcluir):
	professorDAO.excluir_professor_DAO(nomeprofessorExcluir)