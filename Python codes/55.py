def triangulo(lado1, lado2, lado3):
    if lado1 and lado2 and lado3 > 0:
        return "são"
    else: 
        return "não são"

def ladoMaior(lado1, lado2, lado3):
    if lado1 + lado2 >= lado3:
        return "lado1 + lado2 >= lado3"
    elif lado2 + lado3 >= lado1:
        return "lado2 + lado3 >= lado1"
    elif lado3 + lado1 >= lado2:
        return "lado3 + lado1 >= lado2"
    else:
        return "não da tem"

def tipoTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "eqilatero"
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        return "isoceles"
    else:
        return "escaleno"


T1 = float(input("Informe o lado do triângulo 1: "))
T2 = float(input("Informe o lado do triângulo 2: "))
T3 = float(input("Informe o lado do triângulo 3: "))

print("--" * 17)
print("Os lados {} maiores que 0".format(triangulo(T1,T2,T3)))
print("O lado maior é {}".format(ladoMaior(T1,T2,T3)))
print("O triângulo é {}".format(tipoTriangulo(T1,T2,T3)))
print("--" * 17)