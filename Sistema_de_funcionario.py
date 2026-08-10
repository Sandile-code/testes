class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, salario, cargo):
        super().__init__(nome, idade, cpf)
        self.salario = salario
        self.cargo = cargo

    def calcular_salario(self):
        return self.salario

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Cargo: {self.cargo}")
        print(f"Salário: {self.salario}")

funcionario = Funcionario(
    "Leandro",
    32,
    "123",
    3100,
    "Programador"
)

class Gerente(Funcionario):
    def __init__(self, nome, idade, cpf, salario, cargo, bonus):
        super().__init__(nome, idade, cpf, salario, cargo)
        self.bonus = bonus

    def calcular_salario(self):
        return super().calcular_salario() + self.bonus


    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Bonus: {self.bonus}")

gerente = Gerente(
    "Pietro",
    26,
    "902",
    6000,
    "Gerente",
    3000
)

class Estagiario(Funcionario):
    def __init__(self, nome, idade, cpf, salario, cargo, universidade):
        super().__init__(nome, idade, cpf, salario, cargo)
        self.universidade = universidade

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Universidade: {self.universidade}")

estagiario = Estagiario(
    "João",
    20,
    "333",
    1200,
    "Estágiario",
    "UFMT"
)


print(estagiario.calcular_salario())

funcionarios = [
    funcionario,
    gerente,
    estagiario
]
for pessoa in funcionarios:
    print(pessoa.mostrar_dados())