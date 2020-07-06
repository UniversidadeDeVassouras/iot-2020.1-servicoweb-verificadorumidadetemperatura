from application.model.entity.temp import Temperatura
from datetime import date
from application import temperatura_list

class TempDAO:

    def __init__(self):
        self._lista_temperatura = temperatura_list

    #temperatura máxima do dia corrente informada por um cliente x
    def find_temp_max(self, cliente):
        if len(self._lista_temperatura) > 0:
            maior_temperatura = self._lista_temperatura[0]
            for temp in self._lista_temperatura:
                if self.pertence_dia_corrente(temp) and self.pertence_cliente(temp, cliente) and self.maior_que(temp, maior_temperatura):
                    maior_temperatura = temp
            return maior_temperatura
        return None;

    def maior_que(self, temperatura_um, temperatura_dois):
        return temperatura_um.get_valor() > temperatura_dois.get_valor()

    def menor_que(self, temperatura_um, temperatura_dois):
        return temperatura_um.get_valor() < temperatura_dois.get_valor()
    
    def pertence_dia_corrente(self, temperatura):
        return date.today() == temperatura.get_data()

    def pertence_cliente(self, temperatura, cliente):
        return temperatura.get_client().get_id() == cliente.get_id()    

    #temperatura mínima do dia corrente informada por um cliente X
    def find_temp_min(self, cliente):
        if len(self._lista_temperatura) > 0:
            today = date.today()
            menor_temperatura = self._lista_temperatura[0]
            for temp in self._lista_temperatura:
                if self.pertence_dia_corrente(temp) and self.menor_que(temp, menor_temperatura) and self.pertence_cliente(temp, cliente):
                    menor_temperatura = temp
            return menor_temperatura
        return None
        
    def inserir(self, temp):
        temp.set_id(len(self._lista_temperatura) + 1)
        temp.set_data(date.today())
        self._lista_temperatura.append(temp)
        return temp

