from Config.config import *
from Models.colaborador import *

class Professor(Colaborador):
    __tablename__ = 'Professor'
    id_professor = db.Column(db.Integer, db.ForeignKey(Colaborador.id, ondelete="CASCADE"), primary_key=True, autoincrement=False)
    # lista reversa!
    alunos = db.relationship("Aluno", backref="professor")
    # método para expressar o professor em forma de texto
    def __str__(self):
        return f"Professor: {self.nome}, Turno: {self.turno}, Salário: {self.salario}"