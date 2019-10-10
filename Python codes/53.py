# Digite 10 números reais mostre o maior/menor e suas posições
# L = Linha
# C = Coluna

# Declaração da matriz e variaveis:
mat1 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
soma = 0
quant = 0

# Laço para acrecentar o números na matriz:
for l in range(0, 5):
    for c in range(0, 2):
        print('-=' * 20)
        mat1[l][c] = float(input('Digite um numero real: '))
        # Soma dos valores de cada "Capsula" da matriz
        soma += mat1[l][c]
        # Verificção de quantos nú,eros forão digitados
        quant += 1
        
# Declaração do maior/menor e das variaveis que vão receber o valor de "L" e "C" para mostrar a posição no print
maior = mat1[0][0]
x1 = 0
y1 = 0
menor = mat1[0][0]
x2 = 0
y2 = 0

# Laço para ver qual é maior/menor, e a posição do maior/menor
for l in range(0, 5):
    for c in range(0, 2):
        if  mat1[l][c] > maior:
            maior = mat1[l][c]
            x1 = l
            y1 = c
        if mat1[l][c] < menor:
            menor = mat1[l][c]
            x2 = l
            y2 = c

# Prints de saida
print('-=' * 20)
print()
print()
print()
print('-=' * 20)
print(f'O maior número é: {maior}, sua posição é: {x1}, {y1}')
print('-=' * 20)
print(f'O menor número é: {menor}, sua posição é: {x2}, {y2}')
print('-=' * 20)

# Conta / print da média geral
media = soma / quant
print(f'A média é: {media}')
print('-=' * 20)