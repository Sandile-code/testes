n = int(input("Digite os valores que serão contados\n"))
negativo = 0

for a in range (n):
    valor = float(input(f"Digite o {a+1}º valor:\n"))

    if valor < 0:
        negativo += 1
print(F"Total de valores negativos encontrados:{negativo}")