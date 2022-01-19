from app.extensions import db

# Motos
# tabela que contem as informações sobre todos os carros
# id => chave primária
# cor => cor da moto: vermelho, branco, preto etc.
# modelo => por exemplo Suzuki Boulevard, modelo: Boulevard
# marca => por exemplo Suzuki Boulevard, marca: Suzuki
# ano_fabricacao => ano em que foi fabricado a moto
# motor => motor 1.0, 2.0 etc.
# estoque => quantidade de um determinada moto que tem em estoque 
# preco => preço da moto
# nacional => se a moto é nacional (true) ou não (false)
# importada => se a moto é importada (true) ou não (false)

class Motos(db.Model):
        __tablename__ = 'motos'
        id = db.Column(db.Integer, primary_key = True)
        cor = db.Column(db.String(10), nullable = False)
        modelo = db.Column(db.String(20), nullable = False)
        marca = db.Column(db.String(20), nullable = False)
        ano_fabricacao = db.Column(db.Integer, nullable = False)
        motor = db.Column(db.String(10), nullable = False)
        estoque = db.Column(db.Integer, nullable = False)
        preco = db.Column(db.Integer, nullable = False)   
        nacional = db.Column(db.Boolean, nullable = False)
        importada = db.Column(db.Boolean, nullable = False)


        # motos(one) <-> motos carrinho(many)
        moto_carrinho = db.relationship('MotosCarrinho', backref = 'motosCarrinho')
        
        def json(self):
                return{
                'cor':self.cor,
                'modelo':self.modelo,
                'marca':self.marca,
                'ano_fabricacao':self.ano_fabricacao,
                'motor':self.motor,      
                'estoque':self.estoque,
                'preco':self.preco,
                'nacional':self.nacional,
                'importada':self.importada
                }