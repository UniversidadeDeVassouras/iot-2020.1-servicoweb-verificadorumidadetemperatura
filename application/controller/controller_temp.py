from application.model.entity.temp import Temperatura
from application.model.dao.dao_temp import TempDAO
from application.model.dao.dao_cliente import ClienteDAO
from application.model.entity.cliente import Cliente
from application import app
from flask import request, jsonify

@app.route('/temperatura', methods=["POST"])
def inserir_temperatura():
    valor = request.json['valor']
    id_cliente = request.json['client']['id']
    cliente = ClienteDAO().buscar_por_id(id_cliente)
    if cliente != None:
        temperatura_cadastrada = TempDAO().inserir(Temperatura(valor, cliente))
        return jsonify(temperatura_cadastrada.toDict())
    else:
        raise(Exception("Client não encontrado!"))

@app.route('/temperatura', methods=["GET"])
def buscar_temperatura():
    tipo = request.args['tipo']
    id_cliente = request.args['client']
    cliente = ClienteDAO().buscar_por_id(int(id_cliente))
    temperatura = None
    if tipo.lower() == "maxima":
        temperatura = TempDAO().find_temp_max(cliente)
    elif tipo.lower() == "minima":
        temperatura = TempDAO().find_temp_min(cliente)
    if temperatura:
        return jsonify(temperatura.toDict())
    else:
        return '',204
    

