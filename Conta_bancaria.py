class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Saldo não pode ser negativo.")
        else:
            self._saldo = valor

    def depositar(self, valor):
        if valor <= 0:
            return False

        self.saldo += valor
        return True
    
    def sacar(self, valor):
        if valor > self.saldo or valor <= 0:
            return False

        self.saldo -= valor
        return True
    
    def mostrar_dados(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo:.2f}")
    