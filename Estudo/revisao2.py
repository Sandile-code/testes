num1 =  float(input("Digite um número: "))
operacao = input("Digite a operação utilizada (+, -, *, /): ")
num2 = float(input("Digite outro número: "))

if operacao == "+":
    resultado = num1+num2
    print(f"{resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"{resultado}")
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Impossivel dividir por 0")
    else: 
        resultado = num1 /  num2 
        print(f"{resultado}")
else:
    print("Operação inválida")