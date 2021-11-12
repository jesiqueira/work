from flask import Flask

def create_app():
    app = Flask(__name__)

    #Rotas
    from app.controllers.main.rotas import main

    #Registrar Blueprint
    app.register_blueprint(main)

    return app
