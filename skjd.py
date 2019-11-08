def trocar(valores,pos1,pos2):
    if 0 <= pos1 < len(valores) and 0 <= pos2 < len(valores):
        for i in range(0,3):
            temp = valores[pos1]
            valores[pos1] = valores[pos2]
            valores[pos2] = temp
    return valores

matriz = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        n = int(input("Digite um numero impar: "))
        while n % 2 == 0:
            n = int(input("Digite um numero impar por favor: "))
        if n % 2 == 1:
            matriz[i][j] = n


print(matriz)
print(trocar(matriz,0,2))