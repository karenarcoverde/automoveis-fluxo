from app.extensions import db


class Cupons(db.Model):
        __tablename__ = 'cupons'
        id = db.Column(db.Integer, primary_key = True, autoincrement=True)
        valor_desconto = db.Column(db.Integer, nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        categoria = db.Column(db.String(20), nullable = False)


        # cupons(many) <-> usuario(one)
        usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
         
        def json(self):
                return{
                'valor_desconto':self.valor_desconto,
                'quantidade':self.quantidade,
                'categoria':self.categoria,
                'usuario_id':self.usuario_id
                }
