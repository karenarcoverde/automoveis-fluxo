from app.extensions import db

class Carrinho(db.Model):
        __tablename__ = 'carrinho'
        id = db.Column(db.Integer, primary_key = True, autoincrement=True)
        preco_frete = db.Column(db.Integer, nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)
        cupom_desconto = db.Column(db.Boolean, nullable = False)

        # carrinho(one) <-> usuario(one)
        usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

        # motos compra(many) <-> carrinho(one)
        motos_compra = db.relationship('MotosCompra', backref = 'motos_compra_carrinho')

        # carros compra(many) <-> carrinho(one)
        carros_compra = db.relationship('CarrosCompra', backref = 'carros_compra_carrinho')
       


def json(self):
        return{
            'preco_frete':self.preco_frete,
            'quantidade':self.quantidade,
            'preco_total':self.preco_total,
            'cupom_desconto':self.cupom_desconto
        }
        
