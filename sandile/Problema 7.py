n = int(input("Digite a quantidade de lados de um polígono convexo:\n"))
nd = n*(n - 3)/2

if n == 0:
    print("Um polígono não pode ter 0 lados.")
else:
    print(f"Um polígono de {n} lados possui {nd:.0f} diagonais diferentes")