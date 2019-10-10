maior = 0 
menor = 0
soma = 0
falsinha = False
i = 1

while i <= 10:
    num = int(input('Digite um número:'))
    if num > maior:
        maior = num
    if falsinha == False:
        menor = num  
    if falsinha == True and num < menor:
        menor = num
    soma += num
    falsinha = True
    i += 1

media = soma /10 
print(f'Maior: {maior}, Menor: {menor}, Soma: {media} ')