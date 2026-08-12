from abc import ABC, abstractmethod
class Quarto(ABC):
    def __init__(self, numero, preco_diaria, disponivel):
        self.numero = numero
        self.preco_diaria = preco_diaria
        self._disponivel = disponivel

    def reservar(self):
        if self._disponivel == False:
            self._disponivel == True
            return "Reservado"

        return "Indisponivel"
    def liberar(self):    
        if self._disponivel == False:
            self._disponivel == True
        
    @abstractmethod
    def calcular_custos(self, dias):
        pass

    def mostrar_dados(self):
        print(f"Quarto {self.numero}")
        print(f"Diária: {self.preco_diaria}")
        print(f"Disponibilidade: {self._disponivel}")