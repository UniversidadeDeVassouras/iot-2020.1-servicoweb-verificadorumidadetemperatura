from application.model.entity.temp import Temperatura
from application.model.dao.dao_temp import TempDAO
from application.model.dao.dao_cliente import ClienteDAO
from application.model.entity.cliente import Cliente
from application import app
from flask import request, jsonify

@app.route('/temperatura', methods=["POST"])
def umidade():
    valor = request.json['valor']
    id_cliente = request.json['client']['id']
    cliente = ClienteDAO().buscar_por_id(id_cliente)
    if cliente != None:
        temperatura_cadastrada = TempDAO().inserir(Umidade(valor, cliente))
        return jsonify(temperatura_cadastrada.toDict())
    else:
        raise(Exception("Client não encontrado!"))
    

