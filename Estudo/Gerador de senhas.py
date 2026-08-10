import random, string

letras = string.ascii_letters
numeros = string.digits
pontuacao = string.punctuation
todos = letras + numeros + pontuacao 
senha = ""
try:
    tamanho = int(input("Digite o tamanho da senha: "))
    for senha_gerada in range (tamanho):
        senha_gerada = random.choice(todos)
        senha += senha_gerada
    print(f"A Senha gerada foi {senha}")
except:
    print("Formato inválido. Digite um número válido.") 