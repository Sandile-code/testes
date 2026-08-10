n = int(input("Digite um valor inteiro positivo:\n"))

for i in range (2, n):
    if n % i == 0 :
        print(f"{i}")