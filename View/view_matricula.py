from Model.aluno import Aluno
from Model.turma import Turma
from Controller import aluno_controller
from Controller import turma_controller
import os

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	print ('# ---- PROGRAMA CITI 2018 ---- #')


def listar_alunos():
	clear()
	print('# ---- Listanto Alunos ---- #')
	for i, aluno_elemento in enumerate(aluno_controller.solicitar_listar_alunos()):
		print('[{}] - [{}]'.format(i, aluno_elemento))

def listar_turmas():
	clear()
	print('# ---- Listando Turmas ---- #')
	for i, turma_elemento in enumerate(turma_controller.solicitar_listar_turmas()):
		print('[{}] - [{}]'.format(i, turma_elemento))	

def matricular_alunos():
	listar_turmas()

	turma_matricula = input('Qual turma deseja matricular alunos?\n')
	
	for i, turma_elemento in enumerate(turma_controller.solicitar_listar_turmas()):
		if(turma_elemento.getNome() == turma_matricula):
			while (True):
				listar_alunos()
				print('# --- MATRICULANDO ALUNOS NA TURMA [{}]'.format(turma_elemento.getNome()))				
				aluno_matricula = input('Qual aluno deseja matricular na turma?\n')
				for i, aluno_elemento in enumerate(aluno_controller.solicitar_listar_alunos()):
					if(aluno_elemento.getNome() == aluno_matricula):
						aluno_elemento.realizar_matriula(turma_elemento)
						turma_elemento.matricular_aluno(aluno_elemento)
						print('# --- MATRICULA DO ALUNO [{}] REALIZADA NA TURMA DE [{}]--- #'.format(aluno_elemento.getNome(), turma_elemento.getNome()))

				comando = int(input('Dejesa matricular outro aluno? \n[1] Sim - [2] - Nao \n'))
				if(comando == 1):
					pass
				else:
					clear()
					break