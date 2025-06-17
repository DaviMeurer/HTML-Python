#IMPORTA O APP 
from flask import Flask
from .config import Config
from .routes import iniciar_rotas

def start_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    iniciar_rotas(app)
    

    return app