from app.extensions import db
from app.association import association_requisicoes_carros_compra

class CarrosCompra(db.Model):
        __tablename__ = 'carroscompra'
        id = db.Column(db.Integer, primary_key = True, autoincrement=True)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_unitario = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)


        # carros compra (many) <-> carrinho(one)
        carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

        # carros(one) <-> carros compra(many)
        carros_id = db.Column(db.Integer, db.ForeignKey('carros.id'))

        # requisicoes(many) <-> carros compra(many)
        requisicoes = db.relationship('Requisicoes', secondary=association_requisicoes_carros_compra, backref='requisicao_carros_compra')

        def json(self):
                return{
                'quantidade':self.quantidade,
                'preco_unitario':self.preco_unitario,
                'preco_total':self.preco_total
                }