import random

numero_aleatorio = random.randint(1, 15)
tentativa = 0
contador = 0
while numero_aleatorio != tentativa:
    try:
        tentativa = int(input("Adivinhe o número oculto: "))
        contador +=1
        if tentativa > numero_aleatorio:
            print("Palpite foi maior que o número oculto")
        elif tentativa < numero_aleatorio:
            print("Palpite menor que o número oculto")
    except:
        print("Inválido, Digite um número.")
print(f"Acertou! O número oculto era {numero_aleatorio}")
print(f"A quantidade de tentativas necessárias foi {contador}")