
import os
from sqlalchemy.sql.expression import true
from services import colaboradores_service
from flask import Blueprint,jsonify,request,json
from schemas.colaboradores_schema import ColaboradoresSchema
from extensions.database_enum import DataBase
from extensions import utils

colaboradores = Blueprint("colaboradores", __name__, url_prefix="/api/colaboradores")

""" Selecionar qual database vai ser utilizado.."""
tipo_database = os.getenv("TIPO_DATABASE")
if not tipo_database:
    tipo_database = DataBase.SQLLITE.value

service = colaboradores_service.ColaboradoresService(tipo_database)

@colaboradores.route("/", methods=["GET"])
def index():
    app_name = os.getenv("APP_NAME")
    if app_name:
        return jsonify(f"API de Colaboradores da {app_name} Disponivel!")
    return jsonify("API de Colaboradores Disponivel!")

@colaboradores.route("/listar", methods=["GET"])
def listar():
   colaboradores_list = service.listar()
   return json.dumps(colaboradores_list,default=utils.obj_dict)
   
@colaboradores.route("/consultar/<nome>", methods=["GET"])
def consultar(nome):
    colaboradores_list = service.consultar(nome)
    return json.dumps(colaboradores_list,default=utils.obj_dict)

@colaboradores.route("/incluir", methods=["POST"])
def incluir():
   json_data = request.get_json()
   print(json_data)
   colaborador = ColaboradoresSchema.parse_obj(json_data)
   service.incluir(colaborador)
   return jsonify("Incluido com Sucesso! ")
