frase = input("Digite uma frase qualquer\n")
contador = 0

for letra in frase:
   if letra.lower() == "a":
    contador += 1
print(f"A quantidade de letra A na frase é {contador}")