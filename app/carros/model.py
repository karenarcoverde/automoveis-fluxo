from app.extensions import db


class Carros(db.Model):
        __tablename__ = 'carros'
        id = db.Column(db.Integer, primary_key = True)
        cor = db.Column(db.String(10), nullable = False)
        modelo = db.Column(db.String(20), nullable = False)
        marca = db.Column(db.String(20), nullable = False)
        ano_fabricacao = db.Column(db.Integer, nullable = False)
        motor = db.Column(db.String(10), nullable = False)
        estoque = db.Column(db.Integer, nullable = False)
        preco = db.Column(db.Integer, nullable = False)




def json(self):
        return{
            'cor':self.cor,
            'modelo':self.modelo,
            'marca':self.marca,
            'ano_fabricacao':self.ano_fabricacao,
            'motor':self.motor,      
            'estoque':self.estoque,
            'preco':self.preco
        }

        
        