a = int(input("Digite um número:\n"))
b = int(input("Digite um número:\n"))
c = int(input("Digite um número:\n"))
d = int(input("Digite um número(Lembrando que será feito a soma dos 3 menores):\n"))

if a > b and a > c and a > d:
    soma = b + c + d
    print(f"A soma dos 3 menores é {soma}")
elif b > a and b > c and b > d:
    soma = a + c + d
    print(f"A soma dos 3 menores é {soma}")
elif c > a and c > b and c > d:
    soma = a + b + d
    print(f"A soma dos 3 menores é {soma}")
elif d > a and d > b and d > c:
    soma = a + b + c
    print(f"A soma dos 3 menores é {soma}")
    