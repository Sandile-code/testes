from abc import ABC, abstractmethod
class Concessionária:
    def __init__(self):
        self.veiculos = []

    def adicionar(self, veiculo):
        self.veiculos.append(veiculo)

    def listar(self):
        for veiculo in self.veiculos:
            veiculo.mostrar_dados()

    def pesquisar_placa(self):
        if not self.veiculos:
            print("Não existem veículos cadastrados na concessionária.")
            return
        else:
            placa = int(input("Digite a placa"))
            for veiculo in self.veiculos:
                if placa == veiculo.placa:
                    print("Veículo encontrado.")
                    veiculo.mostrar_dados()
                    return
        
            print("Veículo não encontrado")
        
    def calcular_custo_frota(self, distancia):
        for veiculo in self.veiculos:
            print(f"{veiculo.marca} {veiculo.modelo} - R${veiculo.calcular_custos(distancia):.2f}")
        custo_total = sum(veiculo.calcular_custos(distancia) for veiculo in self.veiculos)
        print(f"Custo total: R${custo_total:.2f}")

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def mostrar_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

    @abstractmethod
    def calcular_custos(self, distancia):
        pass

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})" 
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, placa, consumo):
       super().__init__(marca, modelo, ano, placa)
       self.consumo = consumo


    def calcular_custos(self, distancia):
        litros = distancia / self.consumo

        return litros * 6

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, placa, cilindrada):
        super().__init__(marca, modelo, ano, placa)
        self.cilindrada = cilindrada

    def calcular_custos(self, distancia):
        return distancia * 0.15

class Aviao(Veiculo):
    def __init__(self, marca, modelo, ano, placa, passageiros):
        super().__init__(marca, modelo, ano, placa)
        self.passageiros = passageiros

    def calcular_custos(self, distancia):
        return distancia * 10

veiculos = [
    Carro("Toyota","Corolla",2024,12, 500),
    Moto("Honda","CB500",2023,500, 320),
    Aviao("Boeing","737",2020,180, 1500)
]
concessionaria = Concessionária()
for veiculo in veiculos:
    concessionaria.adicionar(veiculo)    

   