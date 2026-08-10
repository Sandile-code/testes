q = int(input("Digite a quantidade fitas que uma locadora possui:\n"))
v = float(input("Digite o valor cobrado por alguel das fitas(R$):\n"))

fa = ((q * 0.33)*12) * (v + ((q * 0.10 ) * (v * 0.10)))
vl = v + ( (q* 0.10) * (v * 0.10))
qf = q - (q * 0.02 * 12) + (q * 0.10 * 12)

print(f"O faturamento anual da locadora é R${fa:.2f}")
print(f"O valor ganho com multas por mês é {vl:.2f}")
print(f"A quantidade final de fitas do ano é {round(qf)}")