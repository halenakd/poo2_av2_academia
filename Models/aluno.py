from Config.config import *
from Models.usuario import Usuario
from Models.colaborador import Colaborador
from Models.treino import *

class Aluno(Usuario):
    __tablename__ = 'Aluno'
    cpf = db.Column(db.String(11), db.ForeignKey('usuario.cpf', ondelete="CASCADE"), primary_key=True)

    prof_id = db.Column(db.String(11), db.ForeignKey('colaborador.cpf', ondelete="CASCADE"), nullable=False)
    professor = db.relationship("Colaborador", foreign_keys=[prof_id])
    treino_id = db.Column(db.ForeignKey(Treino.id))
    treino = db.relationship("Treino", foreign_keys=[treino_id])   

    objetivo = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f"Aluno: {self.nome}, Endereco: {str(self.endereco)},\n Professor: {self.professor.nome}, Treino {self.treino.tipo}, Objetivo: {self.objetivo}"