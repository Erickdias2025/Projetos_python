from datetime import date
# CONFERINDO O ANO DO ATLETA
ano = int(input('Ano de nascimento do atleta: '))

# SOMA DA IDADE ATUAL
idade = date.today().year - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos ele é um atleta: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos ele é um atleta: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos ele é um atleta: JUNIOR')
elif idade == 20:
    print(f'O atleta tem {idade} anos ele é um atleta: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos ele é um atleta: MASTER')
