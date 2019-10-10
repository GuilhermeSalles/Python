N1 = int(input('Digite o primeiro numero: '))
N2 = int(input('Digite o segundo numero: '))

if N1 > N2 :
    maior = N1
    menor = N2
if N2 > N1:
    maior = N2
    menor = N1
for i in range (menor +1, maior):
    print(i,end='')
print('O número Menor é {0}\nE o número Maior é {1}'.format(menor, maior))
