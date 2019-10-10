print("Digite os numeros para a operação:")
#Variaveis para serem guardados os dados para efetuar a conta 
a = int (input("A: "))
b = int (input("B: "))
c = int (input("C: "))

delta = b**2 - 4 * a * c
#verifica se é possivel a continuação da formula
if delta <= 0:
    print("Conta inválida!")
else:
    #Continuação da formula
    conta = sqrt = delta**(.5)

    x1 = (-b + conta)/2 * a
    x2 = (-b - conta)/2 * a
#Saida dos dados resultado das contas
    print("Resultado:X1: %4.2f" %x1)
    print("Resultado:X2: %4.2f" %x2)
