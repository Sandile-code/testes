nomes = []
contador = 0
total_letras = 0
print("Cadastro de nomes para o casamento")

while contador < 3:
    nome_digitado = input(f"DIgite o {contador + 1}º nome ")

    nomes.append(nome_digitado)
    contador += 1
for nome in nomes:
    print(f" - {nome.upper()}")

    total_letras += len(nome)

print(f"O total de letras em todos os nomes é: {total_letras}")