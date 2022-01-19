from app.extensions import db

class Carrinho(db.Model):
        __tablename__ = 'carrinho'
        id = db.Column(db.Integer, primary_key = True)
        nome = db.Column(db.String(30), nullable = False)
        forma_pagamento = db.Column(db.String(40), nullable = False)
        preco_frete = db.Column(db.Integer, nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)
        cupom_desconto = db.Column(db.Boolean, nullable = False)


        # carrinho(one) <-> usuario(one)
        usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

        # motos carrinho(many) <-> carrinho(one)
        motos_carrinho = db.relationship('MotosCarrinho', backref = 'motosCarrinho_carrinho')

        # carros carrinho(many) <-> carrinho(one)
        carros_compra = db.relationship('CarrosCarrinho', backref = 'carrosCarrinho_carrinho')
       
        def json(self):
                return{
                'forma_pagamento':self.forma_pagamento,
                'preco_frete':self.preco_frete,
                'quantidade':self.quantidade,
                'preco_total':self.preco_total,
                'cupom_desconto':self.cupom_desconto
                }