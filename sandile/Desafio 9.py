num1 = float(input("Digite o valor do primeiro número: "))
operacao = input("Digite a operação para ser realizado a conta (+, -, *, /): ")
num2 = float(input("Digite o valor do segundo número: "))

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado:{resultado:.2f}")
elif operacao ==  "-":
    resultado = num1 - num2
    print(f"Resultado:{resultado:.2f}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado:{resultado:.2f}")
elif operacao == "/":
    if num2 == 0:
        print("Não é possivel dividir por zero")
    else:
        resultado = num1 / num2
    print(f"Resultado: {resultado:.2f}")
    
else:
    print("Operação inválida")