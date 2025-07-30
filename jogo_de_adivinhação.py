
from random import randint  # IMPORTANDO BIBLIOTECAS
from time import sleep

while True:
    tentativas = []  # VARIAVEL PARA ARMAZERAR AS TENTATIVAS FEITAS

    print("\033[33mJOGO DE ADIVINHAÇÃO\033[m")  # TITULO DO JOGO

    print("~"*30)

    while True:  # LOOP DO JOGO
        try:
            print("NIVEL 1 -> 1 ATÉ 10")  # AVISO DE NIVEL
            print("NIVEL 2 -> 1 ATÉ 100")
            print("NIVEL 3 -> 1 ATÉ 1000")
            escolha_nivel = int(
                # ESCOLHA DO NIVEL
                input("ESCOLHA UM NÍVEL PARA COMEÇAR! (1-2-3): "))
            if escolha_nivel not in [1, 2, 3]:
                print("\033[31mESCOLHA INVÁLIDA! USE APENAS 1, 2 OU 3.\033[m")
                continue
            break
        except ValueError:
            print(
                "\033[31mENTRADA INVÁLIDA! DIGITE APENAS NÚMEROS INTEIROS.\033[m")

    if escolha_nivel == 1:
        limite = 10
    elif escolha_nivel == 2:
        limite = 100
    else:
        limite = 1000

    escolha_maquina = randint(1, limite)
    print(f"VOCÊ ESCOLHEU O NÍVEL {escolha_nivel} (1 ATÉ {limite})")
    print("CERTO!, ENTÃO VAMOS COMEÇAR!")

    while True:
        try:
            escolha_jogador = int(
                input(f"ESCOLHA UM NÚMERO ENTRE 1 e {limite}: "))
        except ValueError:
            print("\033[31mENTRADA INVÁLIDA! DIGITE UM NÚMERO INTEIRO.\033[m")
            continue

        if escolha_jogador < 1 or escolha_jogador > limite:
            print(
                f"\033[31mNÚMERO FORA DO INTERVALO! DIGITE ENTRE 1 E {limite}.\033[m")
            continue

        tentativas.append(escolha_jogador)

        print("GERANDO RESULTADO....")
        sleep(1.5)

        if escolha_jogador > escolha_maquina:
            print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MENOR\033[m")
        elif escolha_jogador < escolha_maquina:
            print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MAIOR\033[m")
        else:
            print("\033[32mPARABÉNS!, VOCÊ ACERTOOU!\033[m")
            break

        print("~"*20)

        # DEMONSTRAÇÃO DE QUANTIDADES DE TENTATIVAS
    print(f"FORAM NECESSÁRIAS {len(tentativas)} TENTATIVA(S)")
    print(f"SEUS PALPITES FORAM {tentativas}")

    # PERGUNTA SOBRE REPETIÇÃO DO JOGO
    repetir = input("DESEJA JOGAR NOVAMENTE? (S/N): ").lower().strip()
    if repetir != "s":
        print("OBRIGADO POR JOGAR!, ATÉ A PRÓXIMA!")
        break
