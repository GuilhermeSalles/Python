R = float(input("Digite o Raio da esfera:"))

volCaixa = R ** 3
volEsfera = (4 * 3.14 * 6 ** 3) / 3

res = volCaixa // volEsfera

print("Cabem %.0f" %res, "esferas.")
