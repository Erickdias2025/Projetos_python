n1 = int(input('Escolha o primeiro número: '))
n2 = int(input('Escolha o segundo número: '))

if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}')
elif n1 < n2:
    print(f'O número {n1} é menor que o número {n2}')
else:
    print('\033[32mOs dois números são iguais\033[m')
