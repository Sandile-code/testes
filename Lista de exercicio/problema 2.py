ano_a = int(input("Digite o ano que a primeira pessoa nasceu: "))
mes_a = int(input("Digite o mês que a primeira pessoa nasceu: "))
dia_a = int(input("Digite o dia que a primeira pessoa nasceu: "))

ano_b = int(input("Digite o ano que a segunda pessoa nasceu: "))
mes_b = int(input("Digite o mês que a segunda pessoa nasceu: "))
dia_b = int(input("Digite o dia que a segunda pessoa nasceu: "))


if ano_a < ano_b:
    print("A primeira pessoa é mais velha (nasceu antes).")
elif ano_a > ano_b:
    print("A segunda pessoa é mais velha (nasceu antes).")
else:
    if mes_a < mes_b:
        print("A primeira pessoa é mais velha (nasceu antes).")
    elif mes_a > mes_b:
        print("A segunda pessoa é mais velha (nasceu antes).")
    else:
        if dia_a < dia_b:
            print("A primeira pessoa é mais velha (nasceu antes).")
        elif dia_a > dia_b:
            print("A segunda pessoa é mais velha (nasceu antes).")
        else:
            print("As duas pessoas nasceram no mesmo dia")