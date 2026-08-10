x = int(input("Digite o número da sua conta corrente de 3 dígitos:\n"))
reverso = int("".join(reversed(str(x))))
soma = x + reverso 

if x > 999:
    print(f"Conta inválida.")
somaA = str(soma)

d1 = int(somaA[0])* 1
d2 = int(somaA[1])* 2
d3 = int(somaA[2])* 3
d4 = int(somaA[3])* 4 if len (somaA) > 3 else 0

soma_geral = d1+d2+d3+d4

d = soma_geral%10
print(f"O digito verificador da conta {x} é {d}")