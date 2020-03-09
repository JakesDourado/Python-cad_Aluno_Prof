import os
from Model.turma import Turma
from Controller import turma_controller 
from Controller import professor_controller


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	print ('# ---- PROGRAMA CITI 2018 ---- #')

def excluir_turma():
	clear()
	listar_turmas()
	nomeTurmaExcluir = input('Digite o nome da turma que deseja excluir: \n')
	turma_controller.solicitar_excluir_turma(nomeTurmaExcluir)


def editar_turma():
	clear()
	listar_turmas()

	nomeTurmaEditar = input('Digite o nome do turma que deseja editar: \n')
	novoNomeTurma = input('Digite o novo nome da turma: \n')

	turma_controller.solicitar_editar_turma(nomeTurmaEditar, novoNomeTurma)
	listar_turmas()

def listar_turmas():
	clear()
	print('# ---- Listando Turmas ---- #')
	for i, turma_elemento in enumerate(turma_controller.solicitar_listar_turmas()):
		print('[{}] - [{}]'.format(i, turma_elemento))	


def listar_professores():
	clear()
	print('# ---- Listando Professores ---- #')
	for i, professor_elemento in enumerate(professor_controller.solicitar_listar_professores()):
		print('[{}] - [{}]'.format(i, professor_elemento))	


def cadastrar_turma():
	clear()
	print('# ---- Cadastrando turma ---- #')

	nome = input('Digite o nome:\n')
	periodo = input('Digite o periodo:\n')
	
	listar_professores()

	nome_professor = input('Qual o professor da turma:\n')
	for professor in professor_controller.solicitar_listar_professores():
		if(professor.getNome() == nome_professor):
			nova_turma = Turma(nome, periodo, professor)
			
			professor.registrar_turma(nova_turma)
			turma_controller.solicitar_cadastrar_turma(nova_turma)

	print('# ---- Cadastro Finalizado! ---- #')

def show_turma_menu():
	cadastrar_turma()
	while True:
		opcao = int(input('Dejesa cadastrar outra turma? \n [1] - Sim \n [2] - Nao\n'))
		if(opcao == 1):
			cadastrar_turma()
		elif(opcao == 2):
			clear()
			break
		else:
			print('Digite um comando valido!')