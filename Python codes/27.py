N1 = int(input("Digite um numero: "))

i = 1

while i <= N1:
    if N1 % i == 0:
     print("É possivel dividir por:", i)
    i += 1