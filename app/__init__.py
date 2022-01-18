from flask import Flask
from app.config import Config
from app.extensions import db

from app.usuario.model import Usuario
from app.carros.model import Carros
from app.carrosCompra.model import CarrosCompra
from app.cupons.model import Cupons
from app.motos.model import Motos
from app.motosCompra.model import MotosCompra
from app.requisicoes.model import Requisicoes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    return app