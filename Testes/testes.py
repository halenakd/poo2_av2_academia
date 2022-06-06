import os, sys

from sqlalchemy import null
currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

from datetime import date
from Config.config import *
from Config.criar_tabelas import *
from Models.endereco import Endereco
from Models.pessoa import Pessoa
from Models.colaborador import Colaborador
from Models.professor import Professor
from Models.exercicio import Exercicio
from Models.treino import Treino
from Models.exercicioTreino import ExercicioTreino
from Models.aluno import Aluno


'''' criando 6 exercicios '''
exercicio_1 = Exercicio(
    nome = "Supino", 
    descricao = "O praticante faz uma flexão de ombro horizontal seguida por uma extensão de cotovelo e volta", 
    series=4,
    repeticoes=12)
exercicio_2 = Exercicio(
    nome = "Agachamento", 
    descricao = "O praticante abaixa os quadris a partir de uma posição em pé e depois se levanta.",
    series=4,
    repeticoes=10)
exercicio_3 = Exercicio(
    nome = "Rosca direta", 
    descricao = "O praticante abaixa os quadris a partir de uma posição em pé e depois se levanta.",
    series=3,
    repeticoes=12)
exercicio_4 = Exercicio(
    nome = "Cadeira Extensora", 
    descricao = "O praticante escolher a carga e estende as pernas sentado e depois volta a posicao inicial.",
    series=4,
    repeticoes=12)
exercicio_5 = Exercicio(
    nome = "Triceps Testa", 
    descricao = "O praticante estende os cotovelos e depois volta a posicao inicial.",
    series=3,
    repeticoes=12)
exercicio_6 = Exercicio(
    nome = "Stiff", 
    descricao = "O praticante movimenta os quadris para trás, inclinando o tronco para frente e depois volta a posicao inicial.",
    series=3,
    repeticoes=12)    
db.session.add(exercicio_1)
db.session.add(exercicio_2)
db.session.add(exercicio_3)
db.session.add(exercicio_4)
db.session.add(exercicio_5)
db.session.add(exercicio_6)
db.session.commit()


''' criando 2 treinos '''
treino_1 = Treino(
    tipo = "A",
    vezes=3,
    duracao=1)
treino_2 = Treino(
    tipo = "A",
    vezes=3,
    duracao=1)
db.session.add(treino_1)
db.session.add(treino_2)
db.session.commit()


''' ligando exercicios aos treinos '''
ExercicioTreino_1 = ExercicioTreino(
    exercicio = exercicio_1, 
    treino = treino_1)
ExercicioTreino_2 = ExercicioTreino(
    exercicio = exercicio_2, 
    treino = treino_1)
ExercicioTreino_3 = ExercicioTreino(
    exercicio = exercicio_3, 
    treino = treino_1)
ExercicioTreino_4 = ExercicioTreino(
    exercicio = exercicio_4, 
    treino = treino_2)
ExercicioTreino_5 = ExercicioTreino(
    exercicio = exercicio_5, 
    treino = treino_2)
ExercicioTreino_6 = ExercicioTreino(
    exercicio = exercicio_6, 
    treino = treino_2)
db.session.add(ExercicioTreino_1)
db.session.add(ExercicioTreino_2)
db.session.add(ExercicioTreino_3)
db.session.add(ExercicioTreino_4)
db.session.add(ExercicioTreino_5)
db.session.add(ExercicioTreino_6)
db.session.commit()

''' criando 3 enderecos'''
endereco_1 = Endereco(
    numero = "611",
    logradouro = "Eng Odebrecht",
    bairro = "Garcia",
    cep = "89021200",
    estado = "SC",
    pais = "Brasil")
endereco_2 = Endereco(
    numero = "38",
    logradouro = "Emilio Tallmann",
    bairro = "Progresso",
    cep = "89001100",
    estado = "SC",
    pais = "Brasil")
endereco_3 = Endereco(
    numero = "702",
    logradouro = "XV de Novembro",
    bairro = "Centro",
    cep = "89010120",
    estado = "SC",
    pais = "Brasil")
db.session.add(endereco_1)
db.session.add(endereco_2)
db.session.add(endereco_3)
db.session.commit()


''' criando 1 professor '''
professor_1 = Professor(
    cpf = "12345678911",
    nome = "Amadeu da Luz",
    dataNascimento = date(1980, 7, 4),
    endereco = endereco_1,
    salario = 5000,
    turno = "matutino")
db.session.add(professor_1)
db.session.commit()
print(professor_1)


''' criando 2 alunos '''
aluno_1 = Aluno(
    cpf = "12345678912",
    nome = "Antonio Carlos",
    dataNascimento = date(1949, 12, 15),
    endereco = endereco_2, 
    treino= treino_1,
    objetivo="Emagrecimento",
    prof_aluno = professor_1 )
aluno_2 = Aluno(
    cpf = "12345678913",
    nome = "Ana Carolina Rosa",
    dataNascimento = date(2001, 5, 16),
    endereco = endereco_3,
    treino = treino_2,
    objetivo="Hipertrofia",
    prof_aluno = professor_1)
db.session.add(aluno_1)
db.session.add(aluno_2)
db.session.commit()


for a in db.session.query(Aluno).all():
    exercicios = db.session.query(ExercicioTreino).filter_by(treino_id = a.treino.id)
    ''' print do aluno '''
    print("------------------------")
    print(a)
    ''' print do treino do aluno '''
    print(a.treino)
    ''' print dos exercicios do treino do aluno '''
    print("Exercicios:")
    for e in exercicios:
        print(e.exercicio.nome)


if os.path.exists(arquivobd): 
    os.remove(arquivobd) 

db.create_all()