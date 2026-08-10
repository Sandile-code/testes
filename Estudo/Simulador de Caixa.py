import time
saldo = 1000.00
acao = ""
menu = "======== Caixa Eletrônico ========\n" \
"Ver saldo\n" \
"Depositar\n" \
"Sacar\n" \
"Sair.\n" \
"================================== "

while True:
    print(menu)
    acao = input("Digite o que deseja fazer: ").lower()
    if acao == "ver saldo":
        print(f"O saldo atual é R${saldo:.2f}")
    elif acao == "depositar":
        try:
            depositar = float(input("Digite a quantia que deseja depositar: R$"))
            saldo += depositar
            print(f"A quantia de R${depositar:.2f} foi depositada na conta.")
        except: 
            print("Inválido! Digite um número.")
    elif acao == "sacar":
        try:
            sacar = float(input("Digite a quantia que deseja sacar: R$"))
            if sacar > saldo:
                print("Saldo insuficiente")
            else :
                print(f"Saque de R${sacar} foi efetuado.")
                saldo -= sacar
        except:
            print("Inválido! Digite um número")
    elif acao == "sair":
            print("Encerrando caixa eletronico....")
            time.sleep (3)
            print("Encerrado.")
            break