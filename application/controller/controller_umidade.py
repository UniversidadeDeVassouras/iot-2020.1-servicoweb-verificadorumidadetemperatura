from application.model.entity.umidade import Umidade
from application.model.dao.umidade_dao import UmidadeDAO
from application.model.entity.cliente import Cliente
from application import app
from flask import request, jsonify

@app.route('/umidade')
def umidade():
    valor = request.json['valor']
    id_cliente = request.json['client']['id']
    cliente = Cliente()
    cliente.set_id(id_cliente)
    umidade_cadastrada = UmidadeDAO().inserir(Umidade(valor, cliente))
    return jsonify(umidade_cadastrada.toDict())ss
   