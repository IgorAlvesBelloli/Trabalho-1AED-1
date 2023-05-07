from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte
    
    #def cadastrar(self,modelo,cor,preco,potenciaDaFonte):
    #    #self.modelo = input("Modelo:")
    #    #self.cor = input("Cor:")
    #    #self.preco = input("Preço:")
    #    #self._potenciaDaFonte = input("Pontecia Da Fonte:")
    #    print(f"Cadastrado Desktop: {self.modelo}\n{self.cor}\n{self.preco}\n{self._potenciaDaFonte}")
    
    def getInformacoes(self):
        return super().getInformacoes() + f", Potência da fonte: {self._potenciaDaFonte}W"

    def cadastrar(self):
        #self.modelo = input("Modelo:")
        #self.cor = input("Cor:")
        #self.preco = input("Preço:")
        #self._potenciaDaFonte = input("Pontecia Da Fonte:")
        print(f"Cadastrado Desktop: {self.modelo}\nNa Cor:{self.cor}\nNo Valor de: R${self.preco}\nCom a Potência da Fonte de:{self._potenciaDaFonte}W")