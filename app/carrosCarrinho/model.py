from app.extensions import db
from app.association import association_pedidos_carroscarrinho

class CarrosCarrinho(db.Model):
        __tablename__ = 'carroscarrinho'
        id = db.Column(db.Integer, primary_key = True)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_unitario = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # carros carrinho (many) <-> carrinho(one)
        carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

        # carros(one) <-> carros carrinho(many)
        carros_id = db.Column(db.Integer, db.ForeignKey('carros.id'))

        # pedidos(many) <-> carros carrinho(many)
        pedidos = db.relationship('Pedidos', secondary=association_pedidos_carroscarrinho, backref='pedido_carrosCarrinho')

        def json(self):
                return{
                'quantidade':self.quantidade,
                'preco_unitario':self.preco_unitario,
                'preco_total':self.preco_total
                }