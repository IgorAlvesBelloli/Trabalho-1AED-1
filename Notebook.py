from Computador import Computador
class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria
    
   # def cadastrar(self):
   #     print(f"Cadastrado Notebooke: {self.modelo}\n{self.cor}\n{self.preco}\n{self.__tempoDeBateria}")
    
    def getInformacoes(self):
        return super().getInformacoes() + f", Tempo de bateria: {self.__tempoDeBateria}h"

    def cadastrar(self):
        print(f"Cadastrado Notebooke: {self.modelo}\nNa Cor:{self.cor}\nNo Valor de: R${self.preco}\nCom a Duração de: {self.__tempoDeBateria} Horas da Bateria")