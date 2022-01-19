from app.extensions import db
from app.association import association_pedidos_motoscarrinho

class MotosCarrinho(db.Model):
        __tablename__ = 'motoscarrinho'
        id = db.Column(db.Integer, primary_key = True)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_unitario = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)


        # motos carrinho (many) <-> carrinho(one)
        carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

        # motos(one) <-> motos carrinho(many)
        motos_id = db.Column(db.Integer, db.ForeignKey('motos.id'))

        # pedidos(many) <-> motos carrinho(many)
        pedidos = db.relationship('Pedidos', secondary=association_pedidos_motoscarrinho, backref='pedido_motosCarrinho')

        def json(self):
                return{
                'quantidade':self.quantidade,
                'preco_unitario':self.preco_unitario,
                'preco_total':self.preco_total
                }