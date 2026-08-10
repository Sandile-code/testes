menu = "==========Menu do Balaco Baco==============\n" \
"1 - Lasanha\n" \
"2 - Risoto\n" \
"3 - Macarrão la Madeira\n" \
"4 - Strogonoff de carne\n" \
"5 - Sair do Menu..\n" \
"================================================="
print(f"{menu}")
opcao = int(input("Digite a opção desejada:\n"))


while opcao != 5:
    if opcao == 1:
        print("Lasanha cozinhada a lenha, gostosa e cremosa ao paladar por R$ 20,00 o prato.\n")
        print(f"{menu}")
    if opcao == 2:
        print("Risoto riquissimo, feito no ponto perfeito, em promoção por apenas R$12,00\n")
        print(f"{menu}")
    if opcao == 3: 
        print("Macarrão cozinhado ao molho madeira, doce e suculento com carne moída por apenas R$23,00 por prato.\n")
        print(f"{menu}")
    elif opcao == 4: 
        print("Strogonoff de carne macia, feita com molho especial pra encantar a cada mordida, por apenas R$ 19,00\n")
        print(f"{menu}")
    opcao = int(input("Continue escolhendo (ou 5 para sair): "))      
else :
        print("Programa encerrando....")

    


