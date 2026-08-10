import revisão1
def calculadora(valor, taxa):
    try:
        imposto = valor * (taxa/100)
        total = valor + imposto
        if total > 1000:
            desconto = total * (5/100) 
            total = total - desconto 
        return total 
    except:
        return None
precos = [500, 1200, 800, "duzentos", 2000]
taxa_imp = 10


for i in precos:
    resultado = calculadora(i, taxa_imp)
    if resultado is not None:
        print(f"Preço com imposto aplicado é R${resultado:.2f}")
    else:
        print(f"Aviso: o Valor '{i}' é inválido e foi pulado")


print("================================================================")
print("PROXIMA ATIVIDADE")


compras = [10.50, 20.0, 50.0, 100.0, 2000.0]
total_carrinho = 0
for i in compras:
    total_carrinho += i 
print(f"O valor total das compras do carrinho é R${total_carrinho:.2f}")

print("===============================================================")
print("Atividade final")

total_final = 0
for item in compras:
    
    resultado = calculadora(item, taxa_imp)
    total_final += resultado
print(f"Resultado final dos preços é R${total_final}") 





