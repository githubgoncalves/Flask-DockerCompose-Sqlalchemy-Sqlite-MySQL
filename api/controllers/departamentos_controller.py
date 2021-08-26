
import os
from services import departamento_service
from flask import Blueprint, json,jsonify,request,Response
from schemas.departamentos_schema import DepartamentosSchema
from extensions.database_enum import DataBase
from extensions import utils

departamentos = Blueprint("departamentos", __name__, url_prefix="/api/departamentos")

""" Selecionar qual database vai ser utilizado.."""
tipo_database = os.getenv("TIPO_DATABASE")
if not tipo_database:
    tipo_database = DataBase.SQLLITE.value

service = departamento_service.DepartamentosService(tipo_database)

@departamentos.route("/", methods=["GET"])
def index():
    app_name = os.getenv("APP_NAME")
    if app_name:
        return jsonify(f"API de Departamentos da {app_name} Disponivel!")
    return jsonify("API de Departamentos Disponivel!")

@departamentos.route("/listar", methods=["GET"])
def listar():
   departamentos_list = service.listar()
   return json.dumps(departamentos_list,default=utils.obj_dict)

@departamentos.route("/consultar/<nome>", methods=["GET"])
def consultar(nome):
   departamentos_list = service.consultar(nome)
   return json.dumps(departamentos_list,default=utils.obj_dict)

@departamentos.route("/incluir", methods=["POST"])
def incluir():
   json_data = request.get_json()
   departamento = DepartamentosSchema.parse_obj(json_data)
   service.incluir(departamento)
   return jsonify("Incluido com Sucesso!")

