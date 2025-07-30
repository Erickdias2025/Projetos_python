
from random import randint  # IMPORTANDO BIBLIOTECAS
from time import sleep

while True:
    maquina = randint(1, 10)  # GERANDO O RESULTADO ALEATÓRIO DA MAQUINA
    tentativas = []  # PONTO DE SAVE DE QUANTIDADE DE TENTATIVAS

    print("\033[33mJOGO DE ADIVINHAÇÃO\033[m")  # TITULO DO JOGO
    print("-"*30)
    print("ESCOLHI UM NÚMERO ENTRE 1-10")  # AVISO DA OFERTA DO JOGO
    print("CONSEGUE ADIVINHAR QUAL É?")  # AVISO DA OFERTA DO JOGO
    print("="*30)
    while True:  # LOOP DO JOGO
        try:
            # INSERÇÃO DE NÚMERO ESCOLHIDO PELO JOGADOR
            escolha = int(input("TENTE UM NÚMERO ENTRE (1-10): "))
        except ValueError:
            print(

                # MENSAGEM DE OCORRENÇIA INVÁLIDA
                "\033[mENTRADA INVÁLIDA, TENTE APENAS NÚMEROS INTEIROS EX: 1, 5, 10\033[m")
            continue

        tentativas.append(escolha)  # ARMAZENADO AS QUANTIDADES DE TENTATIVAS

        print("GERANDO RESULTADO....")
        sleep(1.5)

        if escolha > maquina:  # OCORRÊNÇIA NÚMERO 1 - JOGADOR CHUTA UM NÚMERO ALTO
            print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MENOR\033[m")
        elif escolha < maquina:  # OCORRÊNÇIA NUMERO 2 - JOGADOR CHUTA UM NÚMERO MENOR
            print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MAIOR\033[m")
        else:  # OCORRÊNÇIA NUMERO 3 - JOGADOR ACERTA O NÚMERO
            print("\033[32mPARÁBENS!, VOCÊ ACERTOOU!\033[m")
            break

        print("="*20)

    # DEMONSTRAÇÃO DE QUANTIDADES DE TENTATIVAS
    print(f"FORAM NECESSÁRIAS {len(tentativas)} TENTATIVA(S)")
    print(f"SEUS PALPITES FORAM {tentativas}")

    # PERGUNTA SOBRE REPETIÇÃO DO JOGO
    repetir = input("DESEJA JOGAR NOVAMENTE? (S/N): ").lower()
    if repetir != "s":
        print("OBRIGADO POR JOGAR!, ATÉ A PRÓXIMA!")
        break
