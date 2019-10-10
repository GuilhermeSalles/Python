x = int(input("Digite um valor para X: "))
n = int(input("Digite um valor para N: "))

conta = 0

if x > 0:
    for i in range(1,n + 1):
     conta = x ** i
else:
     print('Digite outro número.')

print('O número {} elevado a {} resulta em {}'.format(x, n, conta))
