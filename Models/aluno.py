from Config.config import *
from Models.pessoa import *
from Models.professor import *
from Models.treino import *

class Aluno(Pessoa):
    __tablename__ = 'Aluno'
    id_aluno = db.Column(db.Integer, db.ForeignKey(Pessoa.id, ondelete="CASCADE"), primary_key=True, autoincrement=False)

    prof_id = db.Column(db.Integer, db.ForeignKey(Professor.id_professor, ondelete="CASCADE"), nullable = False)
    prof_aluno = db.relationship("Professor", foreign_keys=[prof_id])

    treino_id = db.Column(db.ForeignKey(Treino.id))
    treino = db.relationship("Treino", foreign_keys=[treino_id])   

    objetivo = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f"Aluno: {self.nome}, Endereco: {str(self.endereco)},\n Professor: {self.prof_aluno.nome}, Treino {self.treino.tipo}, Objetivo: {self.objetivo}"