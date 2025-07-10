n1 = int(input('Escolha o primeiro número: '))
n2 = int(input('Escolha o segundo número: '))
n3 = int(input('Escolha o terceiro número: '))

if (n1 + n2 >= n3) and (n2 + n3 >= n1) and (n1 + n3 >= n2):
    print(f'Os números {n1}, {n2} e {n3} podem formar um triângulo')

else:
    print(f'Os números {n1}, {n2} e {n3} não podem formar um triângulo')
