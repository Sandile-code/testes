lado_a = float(input("Quanto vale o lado A do triângulo?\n"))
lado_b = float(input("Quanto vale o lado B do triângulo?\n"))
lado_c = float(input("Quanto vale o lado C do triângulo?\n"))


if lado_a == lado_b == lado_c:
    print("O triângulo informado é um Equilátero e possui todos os lados iguais.")
elif lado_a == lado_b != lado_c or lado_a == lado_c != lado_b or lado_b == lado_c != lado_a:
    print("O triângulo informado é um Isósceles ou seja, possui dois lados diferentes.")
else:
    print("O triângulo informado é um Escaleno e possui todos os lados diferentes uns dos outros.") 
