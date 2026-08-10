nome = input("Qual o seu nome? \n ")
idade = int(input("Quantos anos você tem? \n "))
ano_Atual = int(input("Em que ano nós estamos?\n "))

ano_Nasc = ano_Atual - idade 
cem = idade + 100
futuro = ano_Atual + 100

print(f"Olá {nome}, você nasceu em {ano_Nasc} e tem {idade} anos.")
print(f"E em {futuro} você terá {cem} anos!")