from app.extensions import db

association_requisicoes_carros_compra = db.Table('association_requisicoes_carros_compra',db.Model.metadata,
                                        db.Column('carros_compra',db.Integer, db.ForeignKey('carros_compra.id')),
                                        db.Column('requisicoes',db.Integer,db.ForeignKey('requisicoes.id')))

association_requisicoes_motos_compra = db.Table('association_requisicoes_motos_compra',db.Model.metadata,
                                        db.Column('motos_compra',db.Integer, db.ForeignKey('motos_compra.id')),
                                        db.Column('requisicoes',db.Integer,db.ForeignKey('requisicoes.id')))
