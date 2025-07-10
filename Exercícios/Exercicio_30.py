cores = {'limpa': '\033[m',
         'verde': '\033[4;32m'}
numero = int(
    input(f'{cores["verde"]}Cite um número qualquer:{cores["limpa"]} '))

if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')
