numero = int(input("Digite um número inteiro entre 0 e 60:\n"))
sucessor = numero + 1

if numero >= 0 and numero < 60:
    print(f"O sucessor de {numero} é {sucessor}")
elif numero == 60:
    print(f"O sucessor de {numero} é 0")
else:
    print(f"Número inválido.")







