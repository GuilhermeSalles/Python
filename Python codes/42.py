x = 0

vet = [0] * 3
while x < 1:
     x = int(input('Digite um numero inteiro--> '))

for i in range(0,3):
    a = int(input('digite um numero inteiro para o vetor--> '))
    vet[i] =  a

for i in range(1,3):
    if vet[i] > x :
        print('maior')
    elif vet[i] < x:
        print('menor')
    else:
        print('igual')