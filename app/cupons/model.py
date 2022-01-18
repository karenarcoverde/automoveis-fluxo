from app.extensions import db


class Cupons(db.Model):
        __tablename__ = 'cupons'
        id = db.Column(db.Integer, primary_key = True)
        valor_desconto = db.Column(db.Integer, nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        categoria = db.Column(db.String(20), nullable = False)
