from application.model.entity.umidade import Umidade
from application.model.entity.cliente import Cliente
from datetime import date

class UmidadeDAO:
    
    def __init__(self):
        self._lista_umidade = []

    def inserir(self, umi):
        umi.set_id(len(self._lista_umidade) + 1)
        umi.set_data(date.today())
        self._lista_umidade.append(umi)
        return umi

    def pertence_dia_corrente(self, umidade):
        return date.today() == temp.get_data()

    def verificar_relacao(self, umidade, cliente):
        return umi.get_cliente().get_id() == cliente.get_id()
    
    # nome do método tem demonstrar O QUÊ ele faz. Mas NUNCA o COMO ele faz
    #SOe o nome do método estiver muito grande, significa que o método está com muitas responsabilidade
    #Método precisam ter sua responsabilidade bem definida.
    #Média das umidades no dia corrente e que sejam pertencentes ao cliente X
    #Nome do método tem que ser explicativo (sobre o O QUÊ)
    def media_umidades(self, cliente):
        media = 0
        for umi in self._lista_umidade:
            if self.pertence_dia_corrente(umi) and self.verificar_relacao(umi, cliente):
                media += umi.get_valor()
        media /= len(_lista_umidade)
        return media
