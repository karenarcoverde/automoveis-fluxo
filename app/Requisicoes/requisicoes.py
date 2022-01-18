from app.extensions import db

class Requisicoes(db.Model):
        __tablename__ = 'requisicoes'
        id = db.Column(db.Integer, primary_key = True)  
        data = db.Column(db.Date, nullable = False)
        preco_frete = db.Column(db.Integer, primary_key = True)
        preco_total = db.Column(db.Integer, primary_key = True)