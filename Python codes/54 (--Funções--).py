def validarSexo(sex):
    if sex == "m" or sex == "f":
         return True
    else:
        return False
    
def validaAltura(altu): 
    if alt > 1 and alt < 2:
        return True
    else:
        return False

def ValidaIdade(idad):
    if idad > 1 and idad < 100:
        return True
    else:
        return False

def validaPeso(sel, alt, ida):
    if sel == "m":
        m = (72.7 * alt) / ida
        return m
    elif sel == "f":
        f = (62.1 * alt) / ida
        return f

sexo = str(input("Digite o seu sexo: [M/F]: ")).lower().strip()[0]
altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))

print("O peso ideal é {:.2f}".format(validaPeso(sexo,altura,idade)))


