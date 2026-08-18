from abc import ABC, abstractmethod
class Hotel:
    def __init__(self):
        self.quartos = []

    def reservar_quarto (self, codigo):
        if not self.quartos:
            print("Ainda não existem quartos cadastrados.")
            return
        for quarto in self.quartos:

            if codigo == quarto.numero:
                if quarto.disponivel == True:
                    print("Quarto Reservado")
                    quarto.disponivel = False
                    return
               
                raise QuartoIndisponivelError("Quarto Indisponivel.")
            
        raise QuartoNaoEncontradoError("Quarto não foi encontrado.")
        
    def adicionar_quartos(self, quarto):
        self.quartos.append(quarto)

    def listar_quartos(self):
        for quarto in self.quartos:
            print(quarto)

class QuartoIndisponivelError(Exception):
    pass

class QuartoNaoEncontradoError(Exception):
    pass

class Quarto(ABC):
    def __init__(self, numero, preco_diaria, _disponivel):
        self.numero = numero
        self.preco_diaria = preco_diaria
        self._disponivel = _disponivel

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, valor):
        self._disponivel = valor


    @abstractmethod
    def calcular_custos(self, dias):
        pass

    def mostrar_dados(self):
        print(f"Quarto {self.numero}")
        print(f"Diária: {self.preco_diaria}")
        print(f"Disponibilidade: {self._disponivel}")

    def __str__(self):
        return f"Quarto {self.numero} - R${self.preco_diaria:.2f}"
    
class QuartoSimples(Quarto):
    def __init__(self, numero, preco_diaria, _disponivel):
        super().__init__(numero, preco_diaria, _disponivel)
       

    def calcular_custos(self, dias):
        return self.preco_diaria * dias
  

class QuartoLuxo(Quarto):
    def __init__(self, numero, preco_diaria, _disponivel):
        super().__init__(numero, preco_diaria, _disponivel)
        

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero (self, valor):
        if valor < 11 or valor > 50:
            print("Número de Quarto inválido")
        else:
            self._numero = valor

    def calcular_custos(self, dias):
        return self.preco_diaria * dias * 1.2

class Suite(Quarto):
    def __init__(self, numero, preco_diaria, _disponivel):
        super().__init__(numero, preco_diaria, _disponivel)

    @property
    def numero (self):
        return  self._numero
    
    @numero.setter
    def numero (self, valor):
        if valor > 10 or valor < 1:
            print("Número de quarto inválido.")
        else:
            self._numero = valor

    def calcular_custos(self, dias):
        return self.preco_diaria * dias * 4.5


hotel = Hotel()

quarto1 = QuartoSimples(900, 29.90, True)
quarto2 = QuartoLuxo(12, 250.00, True)
quarto3 = Suite(2, 450.00, True)

hotel.adicionar_quartos(quarto1)
hotel.adicionar_quartos(quarto2)
hotel.adicionar_quartos(quarto3)

hotel.reservar_quarto(12)
