soma = 0 
notas = [0] * 10
print('-_-' * 17)

for i in range (0,10):
    notas[i] = float(input('Digite a nota do aluno--> '))
    soma = soma + notas[i]
    media = soma / 10
    print('-_-' * 17)

print()
print('-X-' * 17)
print('A média entre as 10 nota é de {:.2f}'.format(media))
print('-X-' * 17)
print()

for i in range(0,10):

    if notas[i] > media:
        print('Noota acima da média: {:.2f}'.format(notas[i]))
        print('-_-' * 17)