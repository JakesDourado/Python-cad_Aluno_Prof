import View.view_aluno as view_aluno
import View.view_professor as view_professor
import View.view_turma as view_turma
import View.view_matricula as view_matricula
import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	print ('# ---- PROGRAMA CITI 2018 ---- #')

def show_menu():
	while True:
		opcao = int(input('Menu: \n [1] - Cadastrar\n [2] - Listar\n [3] - Editar \n [4] - Excluir \n [5] - MATRICULA \n [6] - Sair \n'))
		if(opcao == 1):
			clear()
			comando = int(input('Cadastrar: \n [1] - Aluno\n [2] - Professor\n [3] - Turma \n [4] - Sair \n '))
			if(comando == 1):
				clear()
				view_aluno.show_aluno_menu()
			elif(comando == 2):
				clear()
				view_professor.show_professor_menu()
			elif(comando ==3):
				view_turma.show_turma_menu()
			elif(comando == 4):
				clear()
			else:
				print('Comando invalido!')
		elif(opcao == 2):
			clear()
			comando = int(input('Listar: \n [1] - Aluno\n [2] - Professor\n [3] - Turma \n [4] - Sair \n '))
			if(comando == 1):
				clear()
				view_aluno.listar_alunos()
			elif(comando == 2):
				clear()
				view_professor.listar_professores()
			elif(comando ==3):
				view_turma.listar_turmas()
			elif(comando == 4):
				clear()
			else:
				print('Comando invalido!')
		elif(opcao == 3):
			clear()
			comando = int(input('Editar: \n [1] - Aluno\n [2] - Professor\n [3] - Turma \n [4] - Sair \n '))
			if(comando == 1):
				clear()
				view_aluno.editar_aluno()
			elif(comando == 2):
				clear()
				view_professor.editar_professor()
			elif(comando ==3):
				view_turma.editar_turma()
			elif(comando == 4):
				clear()
			else:
				print('Comando invalido!')
		elif(opcao == 4):
			clear()
			comando = int(input('Excluir: \n [1] - Aluno\n [2] - Professor\n [3] - Turma \n [4] - Sair \n '))
			if(comando == 1):
				clear()
				view_aluno.excluir_aluno()
			elif(comando == 2):
				clear()
				view_professor.excluir_professor()
			elif(comando ==3):
				view_turma.excluir_turma()
			elif(comando == 4):
				clear()
			else:
				print('Comando invalido!')
		elif(opcao == 5):
			clear()
			view_matricula.matricular_alunos()
		elif(opcao == 6):
			clear()
			print('Volte Sempre!')
			break
		else:
			print('Digite um comanto valido!')