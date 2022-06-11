from Config.config import *
from Models.usuario import Usuario

"""
Return que depende da classe Pessoa
return f"Colaborador('{self.nome}', '{self.cpf}', '{self.dtnasc}', '{self.salario}', '{self.turno}')"
"""

class Colaborador(Usuario):
    cpf = db.Column(db.String(11), db.ForeignKey('usuario.cpf', ondelete="CASCADE"), primary_key=True)
    salario = db.Column(db.Integer)
    turno = db.Column(db.String(254))
    
    __mapper_args__ = { 
        'polymorphic_identity':'colaborador'
    }

    """
    return que está utilizando a classe pessoa do Model.model
    """

    def __str__(self):
        return f"Colaborador('{self.nome}', '{self.salario}', '{self.turno}')"