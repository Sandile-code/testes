num = int(input("Digite um número de 4 dígitos: "))

if 1000 <= num <= 9999:
    parte1 = num // 100
    
    parte2 = num % 100
    
    soma = parte1 + parte2
    quadrado_da_soma = soma ** 2
    
    if quadrado_da_soma == num:
        print(f"O número {num} possui a característica!")
        print(f"Pois: {parte1} + {parte2} = {soma} e {soma}² = {quadrado_da_soma}")
    else:
        print(f"O número {num} não possui a característica.")
        print(f"Cálculo: ({parte1} + {parte2})² = {quadrado_da_soma}")
else:
    print("Erro: Por favor, digite um número que tenha exatamente 4 dígitos.")