# LISTA DE DESCONTO
print('\033[0;32m===CONFIRA A LISTA DE DESCONTOS ABAIXO===\033[m')
print('\033[0;35mDINHEIRO/CHEQUE: 10% DE DESCONTO\033[m')
print('\033[0;35mCARTÃO A VISTA: 5% DE DESCONTO\033[m')
print('\033[0;35m2X NO CARTÃO: PREÇO NORMAL\033[m')
print('\033[0;35m3X OU MAIS NO CARTÃO: 20% DE JUROS\033[m')

while True:
    try:
        # ENTRADA DO PREÇO DO PRODUTO
        print('\033[0;32m===VALOR DO PRODUTO===\033[m')
        entrada = input('R$ ').replace(',', '.')
        valor = float(entrada)

        # ESCOLHA O MÉTODO DE PAGAMENTO

        print('\033[0;32m___MÉTODO DE PAGAMENTO___\033[m')
        print('\033[0;32m___ESCOLHA UMA OPÇÃO DE 0 A 4___\033[m')
        print('='*32)
        print('OPÇÃO 1: DINHEIRO/CHEQUE')
        print('OPÇÃO 2: À VISTA NO CARTÃO')
        print('OPÇÃO 3: 2X NO CARTÃO')
        print('OPÇÃO 4: 3X OU MAIS NO CARTÃO')

        metodo = int(input('Digite o número da opção: '))

        if metodo == 1:
            total = valor * 0.90
            print(f'você escolheu o pagamento à vista no dinheiro/cheque.')
            print(f'Desconto de 10%, Total a pagar: R$ {total:.2f}')
        elif metodo == 2:
            total = valor * 0.95
            print(f'Você escolheu pagamento à vista no cartão.')
            print(f'Desconto de 5%. Total a pagar: R$ {total:.2f}')
        elif metodo == 3:
            total = valor
            print(f'Você escolheu pagamento em até 2x no cartão.')
            print(f'Preço normal. Total a pagar: R$ {total:.2f}')
        elif metodo == 4:
            total = valor * 1.20
            print(f'Você escolheu pagamento em 3x ou mais no cartão.')
            print(f'Acréscimo de 20%. Total a pagar: R$ {total:.2f}')
        else:
            print('\033[31mOpção inválida. Escolha de 1 a 4.\033[m')
            continue
        break
    except ValueError:
        print(
            '\033[31mEntrada inválida. Digite um valor válido (Ex:Valor: R$ 20.50 E Método: 1)\033[m')
