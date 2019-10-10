# Digite o nome e as duas notas do aluno, mostre a média de cada aluno, e a média geral
# L = Linha
# C = Coluna

# Declaração da matriz e variaveis:
mat1 = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
media1 = 0
media2 = 0

# Laço para acrecentar o números na matriz:
for l in range (0, 5):
    print('-=' * 20)
    nome = str(input('Digite o nome do aluno: '))      
    for c in range(0, 2):
        print('-=' * 20)
        mat1[l][c] = int(input(f'Digite a nota do aluno {nome}: '))
        # 'Funções' média
        media1 = media1 + mat1[l][c]
        media2 = media2 + mat1[l][c]
    # Média de cada aluno
    print('-=' * 20)
    print(f'Média do aluno {nome}: {media1/2}')
    # Isso é feito para zerar a variável para não ter erros 
    media1 = 0

# Print da média geral
print('-=' * 20)
print(f'Média geral: {media2/10}')

