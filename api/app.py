
import os
from flask import Flask
from os import environ
from flask_restplus import Api
from flask_cors import CORS
from controllers.colaboradores_controller import colaboradores
from controllers.departamentos_controller import departamentos
from controllers.dependentes_controller import dependentes
from infra.config_database import create_datebase
from extensions.database_enum import DataBase

app = Flask(__name__)
CORS(app)

""" Selecionar qual database vai ser utilizado.."""
tipo_database = os.getenv("TIPO_DATABASE")
if not tipo_database:
    tipo_database = DataBase.SQLLITE.value

if tipo_database == DataBase.SQLLITE.value:
    print("Creating database ....")
    create_datebase.CreateDataBase(tipo_database)

def create_app():
    app.register_blueprint(colaboradores)
    app.register_blueprint(departamentos)
    app.register_blueprint(dependentes)

    api_doc = Api(app,
        version='1.0',
        title='Doc API TelaVita',
        description='API TelaVita',
        doc='/docs'
    )

if __name__ == "__main__":
    create_app()
    app.run(debug=(not environ.get('ENV') == 'PRODUCTION'), port=int(5000), host="0.0.0.0")

    
 