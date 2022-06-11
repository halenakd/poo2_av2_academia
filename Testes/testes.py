import os, sys

from sqlalchemy import null
currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

from Config.config import *
from datetime import date
from Config.criar_tabelas import *
from Models.endereco import Endereco
from Models.pessoa import Pessoa
from Models.usuario import Usuario
from Models.colaborador import Colaborador
from Models.exercicio import Exercicio
from Models.treino import Treino
from Models.exercicioTreino import ExercicioTreino
from Models.dieta import Dieta
from Models.aluno import Aluno
from Models.professor import Professor
from Models.alimento import Alimento
from Models.dietaAlimento import DietaAlimento
from Models.dietaAluno import DietaAluno
from Models.avaliacaoFisica import AvaliacaoFisica

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


''' criando 16 alimentos '''
alimento_1 = Alimento(
    nome = "maca",
    tipo = "fruta")
alimento_2 = Alimento(
    nome = "banana",
    tipo = "fruta")
alimento_3 = Alimento(
    nome = "ameixa",
    tipo = "fruta")
alimento_4 = Alimento(
    nome = "cenoura",
    tipo = "vegetal")
alimento_5 = Alimento(
    nome = "alface",
    tipo = "vegetal")
alimento_6 = Alimento(
    nome = "beterraba",
    tipo = "vegetal")
alimento_7 = Alimento(
    nome = "brocolis",
    tipo = "vegetal")
alimento_8 = Alimento(
    nome = "batata",
    tipo = "carboidrato")
alimento_9 = Alimento(
    nome = "pao integral",
    tipo = "carboidrato")
alimento_10 = Alimento(
    nome = "arroz integral",
    tipo = "carboidrato")
alimento_11 = Alimento(
    nome = "macarrao integral",
    tipo = "vegetal")
alimento_12 = Alimento(
    nome = "ovo",
    tipo = "proteina")
alimento_13 = Alimento(
    nome = "carne de frango",
    tipo = "proteina")
alimento_14 = Alimento(
    nome = "carne vermelha",
    tipo = "proteina")
alimento_15 = Alimento(
    nome = "queijo",
    tipo = "proteina")
alimento_16 = Alimento(
    nome = "iogurte",
    tipo = "proteina")
db.session.add(alimento_1)
db.session.add(alimento_2)
db.session.add(alimento_3)
db.session.add(alimento_4)
db.session.add(alimento_5)
db.session.add(alimento_6)
db.session.add(alimento_7)
db.session.add(alimento_8)
db.session.add(alimento_9)
db.session.add(alimento_10)
db.session.add(alimento_11)
db.session.add(alimento_12)
db.session.add(alimento_13)
db.session.add(alimento_14)
db.session.add(alimento_15)
db.session.add(alimento_16)
db.session.commit()


''' criando 5 tipos de dietas '''
dieta_1 = Dieta(
    duracao = "3 meses",
    objetivo = "Emagrecimento",
    tipo = "Dukan")
dieta_2 = Dieta(
    duracao = "2 meses",
    objetivo = "Emagrecimento",
    tipo = "Low Carb")
dieta_3 = Dieta(
    duracao = "12 meses",
    objetivo = "Controlar a pressao arterial",
    tipo = "Dash")
dieta_4 = Dieta(
    duracao = "6 meses",
    objetivo = "Criar massa",
    tipo = "Paleolitica")
dieta_5 = Dieta(
    duracao = "1 mes",
    objetivo = "Emagrecimento mais rapido",
    tipo = "Cetogenica")
db.session.add(dieta_1)
db.session.add(dieta_2)
db.session.add(dieta_3)
db.session.add(dieta_4)
db.session.add(dieta_5)
db.session.commit()


''' ligando alimentos e dietas '''
DietaAlimento_1 = DietaAlimento(
    alimento = alimento_1,
    dieta = dieta_1,
    qntd = "1 vez ao dia",
    porcao = "50g")
DietaAlimento_2 = DietaAlimento(
    alimento = alimento_12,
    dieta = dieta_1,
    qntd = "1 vez ao dia",
    porcao = "250g")
DietaAlimento_3 = DietaAlimento(
    alimento = alimento_10,
    dieta = dieta_2,
    qntd = "1 vez ao dia",
    porcao = "200g")
DietaAlimento_4 = DietaAlimento(
    alimento = alimento_8,
    dieta = dieta_2,
    qntd = "1 vez ao dia",
    porcao = "400g")
DietaAlimento_5 = DietaAlimento(
    alimento = alimento_16,
    dieta = dieta_3,
    qntd = "1 vez ao dia",
    porcao = "225g")
DietaAlimento_6 = DietaAlimento(
    alimento = alimento_13,
    dieta = dieta_3,
    qntd = "1 vez ao dia",
    porcao = "350g")
DietaAlimento_7 = DietaAlimento(
    alimento = alimento_9,
    dieta = dieta_4,
    qntd = "1 vez ao dia",
    porcao = "100g")
DietaAlimento_8 = DietaAlimento(
    alimento = alimento_7,
    dieta = dieta_4,
    qntd = "1 vez ao dia",
    porcao = "270g")
DietaAlimento_9 = DietaAlimento(
    alimento = alimento_5,
    dieta = dieta_5,
    qntd = "1 vez ao dia",
    porcao = "150g")
DietaAlimento_10 = DietaAlimento(
    alimento = alimento_14,
    dieta = dieta_5,
    qntd = "1 vez ao dia",
    porcao = "275g")
db.session.add(DietaAlimento_1)
db.session.add(DietaAlimento_2)
db.session.add(DietaAlimento_3)
db.session.add(DietaAlimento_4)
db.session.add(DietaAlimento_5)
db.session.add(DietaAlimento_6)
db.session.add(DietaAlimento_7)
db.session.add(DietaAlimento_8)
db.session.add(DietaAlimento_9)
db.session.add(DietaAlimento_10)
db.session.commit()


''' criando 1 professor '''
professor_1 = Professor(
    cpf = "12345678911",
    nome = "Amadeu da Luz",
    dataNascimento = date(1980, 7, 4),
    endereco = endereco_1,
    login = "amadeu_luz",
    email = "amadeu@gmail.com",
    telefone = "98302034",
    senha = "123",
    salario = 5000,
    turno = "matutino")
db.session.add(professor_1)
db.session.commit()


''' criando 2 alunos '''
aluno_1 = Aluno(
    cpf = "12345678912",
    nome = "Antonio Carlos",
    dataNascimento = date(1949, 12, 15),
    endereco = endereco_2, 
    login = "antonio_c",
    email = "antonio@gmail.com",
    telefone = "44509804",
    senha = "123",
    treino= treino_1,
    objetivo="Emagrecimento",
    professor = professor_1)
aluno_2 = Aluno(
    cpf = "12345678913",
    nome = "Ana Carolina Rosa",
    dataNascimento = date(2001, 5, 16),
    endereco = endereco_3,
    login = "anacarol",
    email = "ana@gmail.com",
    telefone = "32090893",
    senha = "123",
    treino = treino_2,
    objetivo="Hipertrofia",
    professor = professor_1)
db.session.add(aluno_1)
db.session.add(aluno_2)
db.session.commit()


''' criando 2 avaliacoes '''
avaliacao_1 = AvaliacaoFisica(
    aluno = aluno_1,
    data = date(2022, 6, 6),
    peso = 75,
    altura = 170,
    med_abdn = 85)
avaliacao_2 = AvaliacaoFisica(
    aluno = aluno_2,
    data = date(2022, 5, 21),
    peso = 55,
    altura = 164,
    med_abdn = 68)
db.session.add(avaliacao_1)
db.session.add(avaliacao_2)
db.session.commit()


''' ligando dietas e alunos '''
DietaAluno_1 = DietaAluno(
    aluno = aluno_1,
    dieta = dieta_3,
    data_inicio = date(2022, 1, 16))
DietaAluno_2 = DietaAluno(
    aluno = aluno_2,
    dieta = dieta_5,
    data_inicio = date(2022, 6, 4))
DietaAluno_3 = DietaAluno(
    aluno = aluno_1,
    dieta = dieta_2,
    data_inicio = date(2022, 1, 16))
DietaAluno_4 = DietaAluno(
    aluno = aluno_2,
    dieta = dieta_4,
    data_inicio = date(2022, 6, 4))
DietaAluno_5 = DietaAluno(
    aluno = aluno_2,
    dieta = dieta_1,
    data_inicio = date(2022, 6, 4))
db.session.add(DietaAluno_1)
db.session.add(DietaAluno_2)
db.session.add(DietaAluno_3)
db.session.add(DietaAluno_4)
db.session.add(DietaAluno_5)
db.session.commit()

""" mostrando professores criados """
print("\nPROFESSORES")
print("------------------------")
print(professor_1)

""" mostrando alunos e exercicios dos treinos dos alunos """
print("\nALUNOS, TREINOS E EXERCICIOS")
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
        print("- " + e.exercicio.nome)
    
''' print dos alunos do professor '''
print("\nLISTAS DE ALUNOS DOS PROFESSORES")
# lista reversa
print("------------------------")
print("Alunos do professor " + professor_1.nome + ":")
for p in professor_1.alunos:
    print("- " + p.nome)

""" mostrando avaliacoes fisicas dos alunos """
print("\nAVALIACOES FISICAS")
print("------------------------")
print(avaliacao_1)
print("------------------------")
print(avaliacao_2)

""" mostrando dietas dos alunos """
print("\nDIETAS")
for aluno in db.session.query(Aluno).all():
    dietas = db.session.query(DietaAluno).filter_by(aluno_id = aluno.cpf)
    ''' print do aluno '''
    print("------------------------")
    print("Aluno:", aluno.nome)
    print("Dietas:")
    for dieta in dietas:
        ''' print das dietas '''
        print(dieta.dieta.tipo)
        alimentos = db.session.query(DietaAlimento).filter_by(dieta_id = dieta.id)
        ''' print dos alimentos '''
        for alimento in alimentos:
            print("- " + alimento.alimento.nome)


if os.path.exists(arquivobd): 
    os.remove(arquivobd) 

db.create_all()