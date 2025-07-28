from random import randint

maquina = randint(1, 10)

print("ESCOLHI UM NÚMERO ENTRE 1 E 10")
print("CONSEGUE ADIVINHAR QUAL É?")
while True:
    try:
        escolha = int(input("TENTE UM NÚMERO ENTRE (1-10): "))
    except ValueError:
        print(
            "\033[mENTRÁDA INVÁLIDA, TENTE APENAS NÚMEROS INTEIROS EX: 1, 5, 10\033[m")
        continue

    if escolha > maquina:
        print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MENOR\033[m")
    elif escolha < maquina:
        print("\033[31mQUASE LÁ!, TENTE UM NÚMERO MAIOR\033[m")
    else:
        print("\033[32mPARÁBENS!, VOÇÊ ACERTOU!\033[m")
        break
