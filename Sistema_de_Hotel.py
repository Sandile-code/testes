from abc import ABC, abstractmethod
class Hotel:
    def __init__(self):
        self.quartos = []

    def reservar_quarto (self):
        if not self.quartos:
            print("Ainda não existem quartos cadastrados.")
            return

        
        



class QuartoIndisponivelError(Exception):
    pass

class QuartoNaoEncontradoError(Exception):
    pass

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
            return "Quarto liberado."
        
    @abstractmethod
    def calcular_custos(self, dias):
        pass

    def mostrar_dados(self):
        print(f"Quarto {self.numero}")
        print(f"Diária: {self.preco_diaria}")
        print(f"Disponibilidade: {self._disponivel}")

class QuartoSimples(Quarto):
    def __init__(self, numero, preco_diaria, disponivel):
        super().__init__(numero, preco_diaria, disponivel)
       

    def calcular_custos(self, dias):
        return self.preco_diaria * dias

    def mostrar_dados(self):
        return super().mostrar_dados()    

class QuartoLuxo(Quarto):
    def __init__(self, _numero, preco_diaria, disponivel):
        super().__init__( preco_diaria, disponivel)
        self._numero = _numero

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero (self, valor):
        if valor <= 10:
            print("Número de Quarto inválido")
        else:
            self._numero = valor

    def calcular_custos(self, dias):
        return self.preco_diaria * dias * 1.2

    def mostrar_dados(self):
        return super().mostrar_dados()

class Suite(Quarto):
    def __init__(self, _codigo, preco_diaria, disponivel):
        super().__init__( preco_diaria, disponivel)
        self._codigo = _codigo

    @property
    def codigo (self):
        return self._codigo
    @codigo.setter
    def codigo (self, valor):
        if valor > 10 or valor < 0:
            print("Número de quarto inválido.")
        else:
            self._codigo = valor


    def calcular_custos(self, dias):
        return self.preco_diaria * dias * 4.5

    def mostrar_dados(self):
        return super().mostrar_dados()

