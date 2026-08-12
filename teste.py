class ContaBancaria:
    def __init__(self, titular, _saldo):
        self.titular = titular
        self._saldo = _saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError ("Valor informado é inválido.")
        else:
            self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError ("Valor informado para o saque é inválido")
        if valor > self._saldo:
            raise ValueError ("Saldo insuficiente")
        else:
            self._saldo -= valor



conta = ContaBancaria(
    titular = "Sandile",
    _saldo = 1
)

try:
    conta.depositar("quinhentos")
    conta.sacar(550)
except ValueError as erro:
    print(erro)

