ct = 0 
soma = 0 
print('-' * 20)
n = int(input('Digite um numero--> '))
maior = n
menor = n 
cont = True
while cont == True:
    n = int(input('Digite um numero--> '))
    if n == 0:
        cont = False
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma = soma + n
    ct += 1
media = soma / ct

print('-' * 20)
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Média: {media}')
