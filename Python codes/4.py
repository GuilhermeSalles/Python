#Vriaveis para guardar os dados do salário e percentual
print("Digite as informações")
S = float(input("Salário mensal:"))
P = float(input("Percentual para reajuste:"))
#indicando que R é float
R = float
#Operação para calcular o reajuste do salário
R = (S + P) / 100 + S
#saida de dados
print("Salário com reajuste: R$ %.2f" %R)