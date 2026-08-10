numero = int(input("Digite um número, o qual será feito uma tabuada de 1 a 10: "))
print(f"a tabuada de {numero} é:")
print("-" * 15)
for tabuada in range(1, 11):
    print(f"{numero} x {tabuada} = {numero * tabuada} ")