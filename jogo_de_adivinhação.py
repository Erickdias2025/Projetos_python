
from random import randint  # IMPORTANDO BIBLIOTECAS
from time import sleep

maquina = randint(1, 10)  # GERANDO O RESULTADO ALEATÓRIO DA MAQUINA

tentativas = []  # PONTO DE SAVE DE QUANTIDADE DE TENTATIVAS

print("\033[33mJOGO DE ADIVINHAÇÃO\033[m")  # TITULO DO JOGO

print("ESCOLHI UM NÚMERO ENTRE 1 E 10")  # AVISO DA OFERTA DO JOGO
print("CONSEGUE ADIVINHAR QUAL É?")  # AVISO DA OFERTA DO JOGO

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

    if escolha > maquina:  # OCORRÊNÇIA NUMERO 1
        print("GERANDO RESULTADO....")
        sleep(1.5)
        print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MENOR\033[m")
    elif escolha < maquina:  # OCORRÊNÇIA NUMERO 2
        print("GERANDO RESULTADO....")
        sleep(1.5)
        print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MAIOR\033[m")
    else:  # OCORRÊNÇIA NUMERO 3
        print("GERANDO RESULTADO....")
        sleep(1.5)
        print("\033[32mPARÁBENS!, VOÇÊ ACERTOU!\033[m")
        break


# DEMONSTRAÇÃO DE QUANTIDADES DE TENTATIVAS
print(f"FORAM NECESSÁRIAS {len(tentativas)} TENTATIVA(S)")
