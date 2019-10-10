i = 1
quant = 0
quant1 = 0
soma1 = 0
soma2 = 0
maior = 0
menor = 0
while i != 0:
    i = int(input("digite um número -->"))
    if i > maior:
        maior = i
        quant += 1
    elif i == 0:
        print('Bye')
    else:
        quant1 += 1
        menor = i
print(maior, menor)
'''
print("Aquantidade de pares é ", quant)
print("Aquantidade de impares é ", quant1)
print("Média par: ", soma1 / quant )
print("Média impar: ", soma2 / quant1)
cont1 = quant1 + quant
cont2 = soma1 + soma2
cont3 = cont2 / cont1
print("média dos numeros lidos %.2f" %cont3)'''

