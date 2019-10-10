vet = [0] * 5
i = 0

while i < 5:
    x = int(input('Digite um numero inteiro--> '))
    if x % 5 == 0:
        vet[i] = x
        i += 1

for i in range(0,5):
    print(vet[i], end=' ')