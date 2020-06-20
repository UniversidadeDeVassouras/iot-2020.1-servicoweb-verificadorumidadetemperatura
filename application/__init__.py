from flask import Flask
from application.model.entity.cliente import Cliente

app = Flask(__name__)

umidade_list = []
temperatura_list = []
cliente_list = [Cliente(1, "Arduino 1")]

from application.controller import controller_umidade
from application.controller import controller_temp