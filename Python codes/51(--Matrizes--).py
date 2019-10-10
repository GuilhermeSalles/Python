# Qual o maior e menor numero em uma matriz 2X3 = 6 itens:
# L = Linha
# C = Coluna

# Matriz:
mat1 = [[0 ,0], 
        [0, 0],
        [0, 0]]

# Laço para acrecentar o números na matriz:
for l in range(0, 3):
    for c in range(0, 2):
        mat1[l][c] = int(input(f'Digite um número inteiro para [{l}, {c}]: '))

# Declaração maior/menor:
maior = mat1[0][0]
menor = mat1[0][0]

# Laço para percorrer o array e verificar qual é maior/menor número digitado:
for l in range(0, 3):
    for c in range(0, 2):
        if mat1[l][c] > maior:
            maior = mat1[l][c]
        if mat1[l][c] < menor:
            menor = mat1[l][c] 

# Resultados:
print('-=' * 20)
print(f'O maior número digitado é: {maior}')
print(f'O menor número digitado é: {menor}')
print('-=' * 20)