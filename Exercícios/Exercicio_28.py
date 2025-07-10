from time import sleep
from random import randint
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m'}
computador = randint(0, 5)  # faz o computador pensar
print(f'{cores['verde']}-=-{cores["limpa"]}'*20)
print(f'{cores["verde"]}  VOU PENSAR EM UM NÚMERO ENTRE 0 E 5, TENTE ADIVINHAR...{cores["limpa"]}')
print(f'{cores['verde']}-=-{cores["limpa"]}'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print(f'{cores["verde"]}UAU VOCÊ ACERTOU!, PARABÉNS{cores['limpa']}')
else:
    print(f'{cores["vermelho"]}POXA QUE PENA!, VOCÊ ERROU...{cores["limpa"]}')
    print(f'{cores["vermelho"]}TENTE NOVAMENTE!{cores["limpa"]}')
