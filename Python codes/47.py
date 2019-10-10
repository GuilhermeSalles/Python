ct = 0 
soma = 0 
maior = 0
menor = 9999

cont = True

print('-' * 20)
while cont ==  True:
    n = int(input('Digite um número inteiro--> '))
    if n == 0:
        cont = False
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    soma = soma + n
    ct = ct + 1

media = soma / ct
print('-' * 20)
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Média: {media}')