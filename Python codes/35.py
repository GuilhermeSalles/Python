i = 0
senha = 1234

while i <= 3-1:
    S1 = int(input("digite a senha: "))
    if S1 != senha:
        print("Acesso negado!")
        i += 1
    else:
        print("Acesso permitido!")
        i += 5

