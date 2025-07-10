import time
import random

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

while True:
    try:
        print('\033[33m=== JOKENPÔ ===\033[m')
        for i, opcao in enumerate(opcoes, 1):
            print(f'{i} = {opcao}')

        escolha_jogador = int(input('Escolha sua opção (1-3): '))
        if escolha_jogador not in [1, 2, 3]:
            print('Escolha inválida.')
            continue

        jogador = opcoes[escolha_jogador - 1]
        maquina = random.choice(opcoes)

        print('JÔ ✊')
        time.sleep(0.5)
        print('KEN ✋')
        time.sleep(0.5)
        print('PO! ✌')
        time.sleep(0.5)

        print(f'\nVocê: {jogador} | Máquina: {maquina}')

        if jogador == maquina:
            print('Empate! 😐')
        elif (jogador == 'PEDRA' and maquina == 'TESOURA') or \
             (jogador == 'PAPEL' and maquina == 'PEDRA') or \
             (jogador == 'TESOURA' and maquina == 'PAPEL'):
            print('Você venceu! 🎉')
        else:
            print('Você perdeu! 😢')

        repetir = input('\nJogar novamente? (1 = Sim | 2 = Não): ')
        if repetir != '1':
            print('Fim do jogo. Obrigado por jogar!')
            break

    except ValueError:
        print('Entrada inválida. Digite um número entre 1 e 3.')
