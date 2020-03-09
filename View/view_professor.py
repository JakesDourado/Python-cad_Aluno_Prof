import os
from Model.professor import Professor
from Controller import professor_controller 

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	print ('# ---- PROGRAMA CITI 2018 ---- #')

def excluir_professor():
	listar_professores()
	nomeProfessorExcluir= input('Digite o nome do professor que deseja excluir: \n')
	professor_controller.solicitar_excluir_professor(nomeProfessorExcluir)

def editar_professor():
	listar_professores()

	nomeProfessorEditar = input('Digite o nome do professor que deseja editar: \n')
	novoNomeProfessor = input('Digite o novo nome do professor: \n')

	professor_controller.solicitar_editar_professor(nomeProfessorEditar, novoNomeProfessor)
	listar_professores()

def cadastrar_professor():
	clear()
	print('# ---- Cadastrando Professor ---- #')

	nome = input('Digite o nome:\n')
	idade = input('Digite a idade:\n')
	cpf = input('Digite o cpf:\n')
	salario = float(input('Digite a salario:\n'))

	novo_professor = Professor(nome, idade, cpf, salario)
	professor_controller.solicitar_cadastrar_professor(novo_professor)

	print('# ---- Cadastro Finalizado! ---- #')

def listar_professores():
	clear()
	print('# ---- Listando Professores ---- #')
	for i, professor_elemento in enumerate(professor_controller.solicitar_listar_professores()):
		print('[{}] - [{}]'.format(i, professor_elemento))	

def show_professor_menu():
	cadastrar_professor()
	while True:
		opcao = int(input('Dejesa cadastrar outro professor? \n [1] - Sim \n [2] - Nao\n'))
		if(opcao == 1):
			cadastrar_professor()
		elif(opcao == 2):
			clear()
			break
		else:
			print('Digite um comando valido!')