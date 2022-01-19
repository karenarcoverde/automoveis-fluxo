from app.extensions import db
from app.association import association_pedidos_carroscarrinho, association_pedidos_motoscarrinho

# Pedidos
# tabela com as informações referentes a junção das tabelas "carros carrinhos" e "motos carrinhos"
# id => chave primária
# data => data em que foi colocado no carrinho os carros e as motos
# preco_frete => preço total do frete juntando os carrinhos do carro e da moto
# preco_total => preço total juntando os carrinhos do carro e da moto

class Pedidos(db.Model):
        __tablename__ = 'pedidos'
        id = db.Column(db.Integer, primary_key = True)  
        data = db.Column(db.Date, nullable = False)
        preco_frete = db.Column(db.Integer, primary_key = True)
        preco_total = db.Column(db.Integer, primary_key = True)


        # carrinho(one) <-> usuario(one)
        usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

        # pedidos(many) <-> carros carrinho(many)
        carros_compra = db.relationship('CarrosCarrinho', secondary=association_pedidos_carroscarrinho, backref='carrosCarrinho_pedido')

        # pedidos(many) <-> motos carrinho(many)
        motos_compra = db.relationship('MotosCarrinho', secondary=association_pedidos_motoscarrinho, backref='motosCarrinho_pedido')


        def json(self):
                return{
                'data':self.data,
                'preco_frete':self.valor_frete,
                'preco_total':self.valor_total,
                'usuario_id':self.usuario_id
                }