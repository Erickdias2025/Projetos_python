from random import randint

e = 'S'
tlt = escolha_jogador = 0
while e:
    escolha_jogador = int(input('Escolha um número: '))
    if escolha_jogador == escolha_maquina:
        escolha_maquina = randint(0, 10)
        print(
            f'Você escolheu o {escolha_jogador}, enquanto eu escolhi o {escolha_maquina}, PARÁBENS! VOCÊ VENCEU!')
        tlt = escolha_jogador
        print(f'Foram necessárias {tlt} tentativas para vencer')

    else:
        print(
            f'Você escolheu o {escolha_jogador}, enquanto eu escolhi o {escolha_maquina}, POXA VOCÊ PERDEU...')
print('FIM DO JOGO')
