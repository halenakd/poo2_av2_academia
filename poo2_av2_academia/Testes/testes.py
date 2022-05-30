import os, sys

from sqlalchemy import null
currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

from Config.config import *
from Config.criar_tabelas import *
from Models.models import *

exercicio1 = Exercicio(
    nome = "Supino", 
    descricao = "O praticante faz uma flexão de ombro horizontal seguida por uma extensão de cotovelo e volta", 
    series=4,
    repeticoes=10)
exercicio2 = Exercicio(
    nome = "Agachamento", 
    descricao = "O praticante abaixa os quadris a partir de uma posição em pé e depois se levanta.",
    series=4,
    repeticoes=10)
db.session.add(exercicio1)
db.session.add(exercicio2)
db.session.commit()
print(exercicio1)
print(exercicio2)


treino1 = Treino(
    tipo = "A",
    vezes=3,
    duracao=1)
db.session.add(treino1)
db.session.commit()
print(treino1)


ExercicioTreino1 = ExercicioTreino(
    exercicio = exercicio1, 
    treino = treino1)
ExercicioTreino2 = ExercicioTreino(
    exercicio = exercicio2, 
    treino = treino1)
db.session.add(ExercicioTreino1)
db.session.add(ExercicioTreino2)
db.session.commit()


professor1 = Professor(
    cpf = "12345678911",
    nome = "Amadeu da Luz",
    telefone = "47 99012 3232",
    email = "amadluz@gmail.com", 
    dataNasc = "04/07/1980",
    endereco = "Garcia",
    turno = "matutino")
db.session.add(professor1)

db.session.commit()

print(professor1)


aluno1 = Aluno(
    cpf = "12345678912",
    nome = "Antonio Carlos",
    telefone = "47 99012 3232",
    email = "antcarlos@gmail.com", 
    dataNasc = "15/12/1949",
    endereco = "Itoupava Central", 
    prof_aluno = professor1, 
    treino= treino1,
    objetivo="Emagrecimento")
aluno2 = Aluno(
    cpf = "12345678913",
    nome = "Ana Carolina Rosa",
    telefone = "47 98864 0465",
    email = "anacarol@gmail.com", 
    dataNasc = "16/05/2001",
    endereco = "Velha",
    prof_aluno = professor1, 
    treino = treino1,
    objetivo="Hipertrofia")
db.session.add(aluno1)
db.session.add(aluno2)
db.session.commit()
print(aluno1)
print(aluno2)