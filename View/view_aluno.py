1

from Model.aluno import Aluno
from Model.turma import Turma
from Controller import aluno_controller
import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	print ('# ---- PROGRAMA CITI 2018 ---- #')

def excluir_aluno():
	clear()
	listar_alunos()
	nomeAlunoExcluir= input('Digite o nome do aluno que deseja excluir: \n')
	aluno_controller.solicitar_excluir_aluno(nomeAlunoExcluir)

def editar_aluno():
	clear()
	listar_alunos()

	nomeAlunoEditar = input('Digite o nome do aluno que deseja editar: \n')
	novoNomeAluno = input('Digite o novo nome do aluno: \n')

	aluno_controller.solicitar_editar_aluno(nomeAlunoEditar, novoNomeAluno)
	listar_alunos()

def listar_alunos():
	clear()
	print('# ---- Listanto Alunos ---- #')
	for i, aluno_elemento in enumerate(aluno_controller.solicitar_listar_alunos()):
		print('[{}] - [{}]'.format(i, aluno_elemento))

def cadastrar_aluno():
	clear()
	print('# ---- Cadastrando Aluno ---- #')

	nome = input('Digite o nome:\n')
	cpf = input('Digite o cpf:\n')
	idade = input('Digite a idade:\n')
	matricula = input('Digite a matricula:\n')

	novo_aluno = Aluno(nome, idade, cpf, matricula)
	aluno_controller.solicitar_cadastrar_aluno(novo_aluno)

	print('# ---- Cadastro Finalizado! ---- #')	

def show_aluno_menu():
	cadastrar_aluno()
	while True:
		opcao = int(input('Dejesa cadastrar outro aluno? \n [1] - Sim \n [2] - Nao\n'))
		if(opcao == 1):
			cadastrar_aluno()
		elif(opcao == 2):
			clear()
			break
		else:
			print('Digite um comando valido!')