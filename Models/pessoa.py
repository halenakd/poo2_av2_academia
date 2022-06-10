from Config.config import * 
from Models.endereco import Endereco

class Pessoa(db.Model):
    __tablename__ = 'Pessoa'

    cpf = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    dataNascimento = db.Column(db.Date(), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey(Endereco.id))
    endereco = db.relationship("Endereco", foreign_keys=[endereco_id])

    # método para expressar a pessoa em forma de texto

    def __str__(self):
        return f"{self.cpf}, {self.nome}, {self.dataNascimento}, {self.endereco}"
