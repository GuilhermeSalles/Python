def Fare(faren):
    cel = (faren - 32 )/1.8
    return cel

def Cel(celci):
    far = (celci * 1.8) + 32
    return far

def validacaoGraus(graus):
    if graus == "f" or graus == "c":
        return True
    else:
        return False

sel = str(input("Selecione qual converção deseja fazer  CELCIUS, OU FAIRENHIGT [C/F]")).lower().strip()[0]
while validacaoGraus(sel) == False:
    print("não existe está conversão no meu sistema T-T")
    sel = str(input("Pro favor selecione novamente qual conversão deseja fazer  CELCIUS, OU FAIRENHIGT [C/F]")).lower().strip()[0]

temp = float(input("Digite a temperatura: "))
if sel == "f":
    print("A converção em F°: {:.2f} F°".format(Fare(temp)))
elif sel == "c":
    print("A converção em C°: {:.2f} C°".format(Cel(temp)))