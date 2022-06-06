from Config.config import *
from Models.exercicio import *
from Models.treino import *
from Models.exercicioTreino import *


class ExercicioTreino (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exercicio_id = db.Column(db.Integer, db.ForeignKey(Exercicio.id))
    exercicio = db.relationship("Exercicio")
    treino_id = db.Column(db.Integer, db.ForeignKey(Treino.id))
    treino = db.relationship("Treino")