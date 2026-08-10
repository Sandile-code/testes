chico = 1.50
tax = 0.02
ze = 1.10
taxz = 0.03
anos = 0

while ze <= chico:
    chico += tax
    ze += taxz
    anos += 1

print(f"A quantidade de anos até zé superar chico é {anos}")