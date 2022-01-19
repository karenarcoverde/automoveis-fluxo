from app.extensions import db

# Carrinho
# tabela com as informações necessárias para poder pagar o que contem no carrinho
# id => chave primária
# forma_pagamento => pode ser PIX, boleto bancario, cartao de crédito etc.
# preco_frete => preço diferente para cada regiao e para cada transporte
# quantidade => quantidade de itens no carrinho
# preco_total => preço total, incluindo tudo que foi colocado no carrinho
# cupom_desconto => se tem cupom de desconto disponivel (true) ou nao (false)

class Carrinho(db.Model):
        __tablename__ = 'carrinho'
        id = db.Column(db.Integer, primary_key = True)
        forma_pagamento = db.Column(db.String(40), nullable = False)
        preco_frete = db.Column(db.Integer, nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)
        cupom_desconto = db.Column(db.Boolean, nullable = False)

        # carrinho(one) <-> usuario(one)
        usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
        usuario = db.relationship("Usuario", back_populates="carrinho")

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