i = 1
while i <= 10:
    numero = int(input("Digite um número ---> "))
    if i == 1:
        maior = numero
    elif numero > maior:
        maior = numero 
    i += 1

print ("O maior número é ---> ", maior)
