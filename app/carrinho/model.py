from app.extensions import db

class Carrinho(db.Model):
        __tablename__ = 'carrinho'
        id = db.Column(db.Integer, primary_key = True)
        preco_frete = db.Column(db.Integer, nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)
        cupom_desconto = db.Column(db.Boolean, nullable = False)

def json(self):
        return{
            'preco_frete':self.preco_frete,
            'quantidade':self.quantidade,
            'preco_total':self.preco_total,
            'cupom_desconto':self.cupom_desconto
        }
        