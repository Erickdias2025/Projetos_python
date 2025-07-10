from datetime import date

print('\033[32m=====ALISTAMENTO-MILITAR=====\033[m')

ano = int(input('Em que ano você nasceu? '))

idade = date.today().year - ano
falta_passou = (idade - 18)


if idade == 18:
    print('Hora de se alistar')
elif idade < 18:
    print(
        f'Você ainda tem {idade} anos não é hora de se alistar falta {abs (falta_passou)} anos para seu alistamento')
elif idade > 18:
    print(f'Seu prazo já passou em {falta_passou} anos')
