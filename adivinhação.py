# IMPORTAÇÃO DE ESCOLHA DA MÁQUINA
from random import randint

tentativas = []
escolha = randint(1, 10)

# PERFIL DO JOGO
print("--JOGO-DE-ADIVINHAÇÃO--")

while True:
    try:
        jogador = int(
            input("ESCOLHA UM NÚMERO INTEIRO ENTRE [1-10]: "))
    except ValueError:
        print(
            "\033[31mENTRADA INVÁLIDA!, TENTE NOVAMENTE USANDO APENAS NÚMEROS INTEIROS EX: 1, 10, 100\033[m")
        continue

    # SEPARANDO AS OPÇÕES DE ADVINHAÇÕES
    if jogador < escolha:
        print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MAIOR!\033[m")

    elif jogador > escolha:
        print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MENOR!\033[m")

    else:
        print("\033[32mPARÁBENS! VOCÊ CONSEGUIU!\033[m")
        break
