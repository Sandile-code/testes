p = float(input("Digite o valor da aplicação mensal:\n"))
taxa = float(input("Digite o valor da taxa de juros que será aplicada:\n"))
n = int(input("Por fim, digite o número de meses:\n"))
i = taxa/100

if i > 0:
    va = p * (((1+i)**n - 1) / i)
else:
    va = p * n 

print(f"O valor acumulado apos {n} meses é R${va:.2f}")