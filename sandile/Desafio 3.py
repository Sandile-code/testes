salario_bruto = float(input("Qual o seu salário bruto?\n"))
sInicio = salario_bruto * 0.10
sIntermediario = salario_bruto * 0.20

salario_liquidoI = salario_bruto - sInicio
salario_liquidoII = salario_bruto - sIntermediario

if salario_bruto <= 2000.00:
    print(f"O seu salario liquido é R${salario_bruto:.2f}")
elif salario_bruto > 2000.00 and salario_bruto <= 4000.00:
    print(f"O seu salario liquido é R${salario_liquidoI:.2f}")
else:
    print (f"O seu salario liquido é R${salario_liquidoII:.2f}")

