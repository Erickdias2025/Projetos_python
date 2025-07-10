soma = 0
cont = 0
while True:
    try:
        for c in range(1, 7):
            escolha = int(
                input(f'Digite o {c} valor: '))
            if escolha % 2 == 0:
                soma += escolha
                cont += 1
        print(f'Voce informou {cont} números PARES, e a soma foi {soma}')
        break
    except ValueError:
        print('\033[31mENTRADA INVÁLIDA\033[m')
