a = int(input("Digite um vamor inteiro positivo:\n"))
b = int(input("Digite outro valor inteiro positivo:\n"))
resultado = 1

for i in range (b):
    resultado = resultado * a

print(f"O valor de {a} elevado a {b} é {resultado}")