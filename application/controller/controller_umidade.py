from application.model.entity.umidade import Umidade
from application.model.dao.dao_umidade import UmidadeDAO
from application.model.dao.dao_cliente import ClienteDAO
from application.model.entity.cliente import Cliente
from application import app
from flask import request, jsonify

@app.route('/umidade', methods=["POST"])
def inserir_umidade():
    valor = request.json['valor']
    id_cliente = request.json['client']['id']
    cliente = ClienteDAO().buscar_por_id(id_cliente)
    if cliente != None:
        umidade_cadastrada = UmidadeDAO().inserir(Umidade(valor, cliente))
        return jsonify(umidade_cadastrada.toDict())
    else:
        raise(Exception("Client não encontrado!"))

@app.route('/umidade', methods=["GET"])
def buscar_umidade_media():
    tipo = request.args['tipo']
    id_cliente = request.args['client']
    cliente = ClienteDAO().buscar_por_id(int(id_cliente))
    temperatura = None
    if tipo.lower() == "media":
        media = UmidadeDAO().media_umidades(cliente)
        return jsonify(media)
    return '', 204

    
    