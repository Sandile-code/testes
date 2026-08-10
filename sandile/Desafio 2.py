velocidade = float(input("Qual a velocidade do carro?(diga os km/h)\n"))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f"Você foi multado por excesso de velocidade e o valor da multa é R${multa:.2f}")
else:
    print("Boa viagem!Continue dirigindo em segurança.")