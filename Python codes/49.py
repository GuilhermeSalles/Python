num = int(input('Digite um número maior que [1]--> '))

while num <= 1:
    dig = int(input('Digite um número novamente--> '))
    num = dig
    
if num % 2 == 1:
    print("primo")
else:
    print("não primo")
