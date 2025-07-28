while True:
    try:
        numero = int(input("ESCOLHA UM NÚMERO INTEIRO: "))
        operador = input("ESCOLHA UM OPERADOR (+, -, *, /): ")

    except ValueError:
        print(
            "\033[31mENTRADA INVÁLIDA, TENTE NOVAMENTE COM NÚMERO INTEIROS EX: 10, 50, 100\033[m")
        continue

    if operador not in ["+", "-", "*", "/"]:
        print(
            "\033[31mENTRADA INVÁLIDA, TENTE NOVAMENTE COM OPERADORES VÁLIDOS\033[m")
        continue

    for i in range(1, 11):
        if operador == "+":
            print(f"{numero} + {i:2} = {numero+i}")
        elif operador == "-":
            print(f"{numero} - {i:2} = {numero-i}")
        elif operador == "*":
            print(f"{numero} * {i:2} = {numero*i}")
        elif operador == "/":
            print(f"{numero} / {i:2} = {numero/i:.2f}")

    repetir = input("DESEJA GERAR NOVAMENTE? (S, N): ").lower()
    if repetir != "s":
        print("ENCERRANDO O PROGRAMA..., ATÉ A PRÓXIMA!")
        break
