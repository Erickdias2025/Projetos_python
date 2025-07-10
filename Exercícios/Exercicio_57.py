r = 'S'
while r == 'S':
    s = str(input('Digite o sexo [M/F]: '))
    if s == 'F':
        print(f'Sexo {s}, tudo certo!').upper()
    else:
        print('Entrada inválida, tente novamente')
