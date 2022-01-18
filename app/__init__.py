from flask import Flask
from .config import Config
from .extensions import db

from .usuario.model import Usuario
from .carros.model import Carros
from .carrosCompra.model import CarrosCompra
from .cupons.model import Cupons
from .motos.model import Motos
from .motosCompra.model import MotosCompra
from .requisicoes.model import Requisicoes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    return app