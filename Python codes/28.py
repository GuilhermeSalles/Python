N1 = int(input("Digite um numero: "))

for i in range (1, N1 +1):
    if N1 % i == 0:
     print("É possivel dividir por:", i)