from Config.config import *
from Models.colaborador import Colaborador

class Professor(Colaborador):
    __tablename__ = 'Professor'
    
    cpf = db.Column(db.String(11), db.ForeignKey('colaborador.cpf', ondelete="CASCADE"), primary_key=True, autoincrement=False)
    # lista reversa!
    alunos = db.relationship('Aluno', backref='professor')

    # método para expressar o professor em forma de texto
    def __str__(self):
        return f"Professor: {self.nome}, Turno: {self.turno}, Salário: {self.salario}"