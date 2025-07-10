from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos \033[32m{totmaior}\033[m pessoal maiores de idade')
print(f'E também tivemos \033[32m{totmenor}\033[m pessoas menores de idade')
