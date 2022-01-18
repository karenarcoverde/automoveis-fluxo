from app.extensions import db

association_requisicoes_carros_compra = db.Table('association_requisicoes_carros_compra',db.Model.metadata,
                                        db.Column('carroscompra',db.Integer, db.ForeignKey('carroscompra.id')),
                                        db.Column('requisicoes',db.Integer,db.ForeignKey('requisicoes.id')))

association_requisicoes_motos_compra = db.Table('association_requisicoes_motos_compra',db.Model.metadata,
                                        db.Column('motoscompra',db.Integer, db.ForeignKey('motoscompra.id')),
                                        db.Column('requisicoes',db.Integer,db.ForeignKey('requisicoes.id')))
