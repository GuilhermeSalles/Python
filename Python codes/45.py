nomes = []
notas = []
count = 0
sumNota = 0

for i in range(1, 6):
    name = str(input(f'Digite o nome do {i}º aluno: '))
    nota = float(input(f'Nota do aluno {name}: '))

    count += 1 
    sumNota += nota
    notas.append(nota)
    nomes.append(name)
    

media = sumNota / count
maior = notas[0]
menor = notas[0]

print()

for item in notas:
    if item > maior:
        maior = item

    elif item < menor:
        menor = item

for i in range(0, 5):
    print(f"Nome: {nomes[i]}, Nota: {notas[i]}")

print()
print('Maior nota: {}, Menor nota: {}.'.format(maior, menor))
print('Média: {}'.format(media))