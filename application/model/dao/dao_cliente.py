from application import cliente_list

class ClienteDAO():

    def __init__(self):
        self._lista_cliente = cliente_list

    def buscar_por_id(self, id):
        cliente_list = list(filter(lambda cliente: cliente.get_id() == id, self._lista_cliente))
        if len(cliente_list) > 0:
            return cliente_list[0]
        else:
            return None