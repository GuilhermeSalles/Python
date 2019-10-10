cont = True

while cont == True:
    
    ope = int(input('Digite uma das opções:[1,2,3,4]--> '))

    if ope == 1:
        C = float(input('Digite os graus Celsius para converter para converter para Fahrenheit --> '))
        F = (9 * + 160) / 5
        print('Os graus convertidos resultam em : {:.2f}'.format(F))

    elif ope == 2:
        F = float(input('Digite os graus Fahrenheit para converter para converter para Celsius --> '))
        C = (F - 32) * 5 / 9
        print('Os graus convertidos resultam em : {:.2f}'.format(C))

    elif ope == 3:
        H = float(input('Digite sua altura para mostrarmos o seu peso ideal[Homens]--> '))
        peso = (72.7 * H) - 58
        print('Seu peso ideal é: {:.2f}'.format(peso))

    elif ope == 4:
        H = float(input('Digite sua altura para mostrarmos o seu peso ideal[Mulheres]--> '))
        peso = (62.1 * H) - 44.7
        print('Seu peso ideal é: {:.2f}'.format(peso))

    op = input('Deseja terminar a operação[S/N]?? ')
    if op == 'S':
        print('Operação finalizada!!')
        cont = False