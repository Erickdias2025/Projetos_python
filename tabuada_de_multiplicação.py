# TITULO

print("TABUADA")

multiplicação = "3"
# ESCOLHA DE OPERAÇÃO MATEMÁTICA
print("OPERAÇÃO MATEMÁTICA")
print("1 = +")
print("2 = -")
print("3 = *")
print("4 = /")

while True:
    try:
        escolha_sinal = int(input("OPERAÇÃO MATEMÁTICA: "))
        escolha_valor = int(input("VALOR INTEIRO: "))

# LOOP DE ERRO
    except ValueError:
        print(
            "\033[31mENTRADA INVÁLIDA!, TENTE NOVAMENTE USANDO NÚMEROS INTEIROS EX: 1, 10, 100\033[m")
        continue

# RESULTADO DA ESCOLHA DO VALOR DA TABUADA
    if escolha_sinal == 1:
        for i in range(1, 11):
            print(f"{escolha_valor:2} X {i:2} = {i+escolha_valor:3}")

    elif escolha_sinal == 2:
        for i in range(1, 11):
            print(f"{escolha_valor:2} X {i:2} = {i-escolha_valor:3}")

    elif escolha_sinal == 3:
        for i in range(1, 11):
            print(f"{escolha_valor:2} X {i:2} = {i*escolha_valor:3}")

    elif escolha_sinal == 4:
        for i in range(1, 11):
            print(f"{escolha_valor:2} X {i:2} = {i/escolha_valor:.2f}")

    else:
        print(
            "ENTRADA INVÁLIDA!, TENTE APENAS NÚMEROS VÁLIDOS!, EX: 1, 2, 3, 4 = +, -, *, /")
    break

# FIM DO PROJETO
