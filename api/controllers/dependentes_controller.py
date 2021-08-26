import os
from services import dependentes_service
from flask import Blueprint,jsonify,request,json
from schemas.dependentes_schema import DependentesSchema
from extensions.database_enum import DataBase
from extensions import utils

dependentes = Blueprint("dependentes", __name__, url_prefix="/api/dependentes")

""" Selecionar qual database vai ser utilizado.."""
tipo_database = os.getenv("TIPO_DATABASE")
if not tipo_database:
    tipo_database = DataBase.SQLLITE.value

service = dependentes_service.DependentesService(tipo_database)

@dependentes.route("/", methods=["GET"])
def index():
    app_name = os.getenv("APP_NAME")
    if app_name:
        return jsonify(f"API de Dependentes da {app_name} Disponivel!")
    return jsonify("API de Dependentes Disponivel!")

@dependentes.route("/listar", methods=["GET"])
def listar():
   dependentes_list = service.listar()
   return json.dumps(dependentes_list,default=utils.obj_dict)

@dependentes.route("/consultar/<id_colaborador>", methods=["GET"])
def consultar(id_colaborador):
   dependentes_list = service.consultar(id_colaborador)
   return json.dumps(dependentes_list,default=utils.obj_dict)

@dependentes.route("/incluir", methods=["POST"])
def incluir():
   json_data = request.get_json()
   dependente = DependentesSchema.parse_obj(json_data)
   service.incluir(dependente)
   return jsonify("Incluido com Sucesso!")

