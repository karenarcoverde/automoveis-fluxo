from app.extensions import db
from app.association import association_requisicoes_carros_compra, association_requisicoes_motos_compra

class Requisicoes(db.Model):
        __tablename__ = 'requisicoes'
        id = db.Column(db.Integer, primary_key = True)  
        data = db.Column(db.Date, nullable = False)
        preco_frete = db.Column(db.Integer, primary_key = True)
        preco_total = db.Column(db.Integer, primary_key = True)


        # carrinho(one) <-> usuario(one)
        usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

        # requisicoes(many) <-> carros compra(many)
        carros_compra = db.relationship('CarrosCompra', secondary=association_requisicoes_carros_compra, backref='carros_compra_requisicao')

        # requisicoes(many) <-> motos compra(many)
        motos_compra = db.relationship('MotosCompra', secondary=association_requisicoes_motos_compra, backref='motos_compra_requisicao')


        def json(self):
                return{
                'data':self.data,
                'preco_frete':self.valor_frete,
                'preco_total':self.valor_total,
                'usuario_id':self.usuario_id
                }