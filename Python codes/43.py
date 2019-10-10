i = 0
j = 0
vet1 = [0] * 3
vet2 = [0] * 3

while i < 3:
    a = int(input('Digite um valor para o vetor 1 --> '))
    vet1[i] = a
    vetor1 = vet1[i]
    i += 1
while j < 3:
    b = int(input('Digite um valor para o vetor 2 --> '))
    vet2[j] = b
    vetor2 = vet2[j]
    j += 1

for i  in range(0,3):
    if vetor1 == vetor2:
        print(' Ocorrencia de iguais!! nuemro {} na posição {}'.format(vet1[i], i))
        
