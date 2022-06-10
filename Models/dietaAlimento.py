from Config.config import*
from Models.alimento import Alimento
from Models.dieta import Dieta

class DietaAlimento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alimento_id = db.Column(db.Integer, db.ForeignKey(Alimento.id))
    alimento = db.relationship("Alimento")
    dieta_id = db.Column(db.Integer, db.Foreignkey(Dieta.id))
    dieta = db.relationship("Dieta")
    qntd = db.Column(db.String(254))
    porcao = db.Column(db.String(254))