from app.extensions import db
from app.association import association_requisicoes_motos_compra

class MotosCompra(db.Model):
        __tablename__ = 'motoscompra'
        id = db.Column(db.Integer, primary_key = True, autoincrement=True)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_unitario = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)


        # motos compra (many) <-> carrinho(one)
        carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

        # motos(one) <-> motos compra(many)
        motos_id = db.Column(db.Integer, db.ForeignKey('motos.id'))

        # requisicoes(many) <-> motos compra(many)
        requisicoes = db.relationship('Requisicoes', secondary=association_requisicoes_motos_compra, backref='requisicao_motos_compra')



        def json(self):
                return{
                'quantidade':self.quantidade,
                'preco_unitario':self.preco_unitario,
                'preco_total':self.preco_total
                }