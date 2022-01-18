from ..extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nome = db.Column(db.String(30), nullable = False)
    cpf = db.Column(db.Integer, unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    telefone = db.Column(db.Integer, nullable = False)
    endereço = db.Column(db.String(30), nullable = False)

    # carrinho(one) <-> usuario(one)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    # requisicoes(many) <-> usuario(one)
    requisicao = db.relationship('Requisicoes', backref = 'requisicao_usuario')

    # cupons(many) <-> usuario(one)
    cupom = db.relationship('Cupons', backref = 'cupons_usuario')

    def json(self):
            return{
                'nome':self.nome,
                'cpf':self.cpf,
                'email':self.email,
                'telefone':self.telefone,
                'endereço':self.endereço
            }

