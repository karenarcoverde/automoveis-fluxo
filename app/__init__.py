from flask import Flask
from app.config import Config
from app.extensions import db, migrate

from app.usuario.model import Usuario
from app.carros.model import Carros
from app.carrosCompra.model import CarrosCompra
from app.cupons.model import Cupons
from app.motos.model import Motos
from app.motosCompra.model import MotosCompra
from app.requisicoes.model import Requisicoes

# cria o app
def create_app():
    # instanciacao do aplicativo
    app = Flask(__name__)

    # configuracao do app
    app.config.from_object(Config)

    # inicializacao da database
    db.init_app(app)
    migrate.init_app(app,db)

    return app