i = 1
soma = 0

while i != 0:

    n1 = int(input("Digite um numero negativo: "))
    if n1 == 0:
        print("Fim da equação")
        i = 0
    elif n1 < -1:
        soma += n1
        i += 1
        
print(f"Sua divida é {soma}")
