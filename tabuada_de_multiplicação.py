# TITULO
print("TABUADA DE MULTIPLICAÇÃO")

# ESCOLHA DE VALOR
while True:
    try:
        escolha = int(input("ESCOLHA UM VALOR INTEIRO: "))
# LOOP DE ERRO
    except ValueError:
        print(
            "\033[31mENTRADA INVÁLIDA!, TENTE NOVAMENTE USANDO NÚMEROS INTEIROS EX: 1, 10, 100\033[m")
        continue

# RESULTADO DA ESCOLHA DO VALOR DA TABUADA
    for i in range(1, 11):
        print(f"{escolha:2} X {i:2} = {i*escolha:3}")
    break

# FIM DO PROJETO
