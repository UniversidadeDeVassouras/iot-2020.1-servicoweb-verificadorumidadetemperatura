from application.model.entity.umidade import Umidade
from datetime import date

class UmidadeDAO:
    
    def __init__(self):
        self._lista_umidade = []

    def inserir(self, umi):
        umi.set_id(len(self._lista_umidade) + 1)
        umi.set_data(date.today())
        self._lista_umidade.append(umi)
        return umi

    def media_umidades(self):
        media = 0
        for umi in self._lista_umidade:
            if umi.get_data() == date.today():
                media += umi.get_valor()
        media /= len(_lista_umidade)
        return media

        
