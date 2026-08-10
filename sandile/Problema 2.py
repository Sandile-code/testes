numero = float(input("Digite um número real:\n"))
inteiro = int(numero)
arredondado = round(numero)
fracionaria = numero - inteiro

print(f"A parte inteira de {numero} é {inteiro}\n")
print(f"O número {numero} arrendondado é {arredondado}\n")
print(f"A parte fracionária de {numero} é {fracionaria:.4f}")

