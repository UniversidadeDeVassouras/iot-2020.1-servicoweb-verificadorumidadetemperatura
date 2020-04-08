from application.model.entity.temp import Temperatura
from datetime import date

class TempDAO:

    def __init__(self):
        self._lista_temperatura = []

    def find_temp_max(self):
        today = date.today()
        maior_temperatura = self._lista_temperatura[0]
        for temp in self._lista_temperatura:
            if today == temp.get_data() and temp.get_valor() > maior_temperatura.get_valor():
                maior_temperatura = temp
        return maior_temperatura

    
    def find_temp_min(self):
        today = date.today()
        menor_temperatura = self._lista_temperatura[0]
        for temp in self._lista_temperatura:
           if today == temp.get_data() and temp.get_valor() < menor_temperatura.get_valor():
               menor_temperatura = temp
        return menor_temperatura
        
    def inserir(self, temp):
        temp.set_id(len(self._lista_temperatura) + 1)
        temp.set_data(date.today())
        self._lista_temperatura.append(temp)
        return temp

