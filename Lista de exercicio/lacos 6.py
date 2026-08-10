n = int(input("Digite um númeiro inteiro positivo:\n"))
e = 1.0
fatorial = 1
for i in range (1, n + 1):
    fatorial *= i
    e += 1 / fatorial
print(f"O valor de E é {e:.4f}")