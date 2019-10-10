print("Digite sua data de nacimento:")
# Variaveis usadas para guardar a data de nascimento do usuário
D = int (input("Dia:"))
M = int (input("Mês:"))
A = int (input("Ano:"))
#Variavel para guardar o ano atual
A1 = int (input("Ano atual:"))

#Operação para converter a data de nascimento em dias
v1 = D + M * 30 + A * 365
#Operação para transformar o ano atual em dias
v2 = A1 * 365
#operação para saber os dias exatos
v3 = v2 - v1 
#saida do dados
print("Data transformada em dias: ", v3)