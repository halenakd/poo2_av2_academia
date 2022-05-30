import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

from Config.config import *

class Pessoa (db.Model):
    __tablename__ = 'Pessoa'

    id_pessoa = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(254))
    nome = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    email = db.Column(db.String(254))
    dataNasc = db.Column(db.String(254))
    endereco = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'Pessoa: {self.nome}, {self.cpf}'+\
               f'{self.email}, {self.telefone}, '+\
               f'{self.dataNasc}, {self.endereco}'


class Professor(Pessoa):
    __tablename__ = 'Professor'
    id_professor = db.Column(db.Integer, db.ForeignKey(Pessoa.id_pessoa, ondelete="CASCADE"), primary_key=True, autoincrement=False)
    ''' pessoa_prof = db.relationship("Pessoa", foreign_keys=[id_professor])'''
    turno = db.Column(db.String(254))

    # método para expressar o professor em forma de texto
    def __str__(self):
        return f"Professor: {self.nome}, Turno: {self.turno}"


class Exercicio (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(254))
    descricao = db.Column(db.String(254))
    series = db.Column(db.Integer)
    repeticoes = db.Column(db.Integer)

    # método para expressar o exercicio em forma de texto
    def __str__(self):
        return f"Exercicio: {self.nome}, {self.descricao}, {self.series} series, {self.repeticoes} repeticoes"


class Treino (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(254))
    '''exercicios = db.relationship('ExercicioTreino', backref='ExerciciosTreino', lazy = True)'''
    vezes = db.Column(db.Integer)
    duracao = db.Column(db.Integer)

    # método para expressar o treino em forma de texto
    def __str__(self):
        return f"Treino: {self.tipo}, {self.vezes} vez(es) p/semana, Duracao: {self.duracao} hora(s)"


class ExercicioTreino (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exercicio_id = db.Column(db.Integer, db.ForeignKey(Exercicio.id))
    exercicio = db.relationship("Exercicio")
    treino_id = db.Column(db.Integer, db.ForeignKey(Treino.id))
    treino = db.relationship("Treino")


class Aluno(Pessoa):
    __tablename__ = 'Aluno'
    id_aluno = db.Column(db.Integer, db.ForeignKey(Pessoa.id_pessoa, ondelete="CASCADE"), primary_key=True)

    prof_id = db.Column(db.Integer, db.ForeignKey(Professor.id_professor))
    prof_aluno = db.relationship("Professor", foreign_keys=[prof_id])

    treino_id = db.Column(db.ForeignKey(Treino.id))
    treino = db.relationship("Treino", foreign_keys=[treino_id])   

    objetivo = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f"Aluno: {self.nome}, Treino {self.treino.tipo}, Objetivo: {self.objetivo}"


if os.path.exists(arquivobd): 
    os.remove(arquivobd) 

db.create_all()