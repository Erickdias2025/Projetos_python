somaidade = 0
médiaidade = 0
maioridadehomem = 0
totmulher = 0
nomevelho = ''
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input(f'Idade de {nome}: '))
    sexo = str(input(f'Sexo de {nome} [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

médiaidade += idade/4
print(f'A média de idade do grupo é de {médiaidade:.1f} anos')
print(
    f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher} com menos de 20 anos')


