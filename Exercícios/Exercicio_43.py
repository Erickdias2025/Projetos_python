# PESO E ALTURA
peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))

# CALCULO DO IMC
soma1 = (altura**2)
imc = (peso/soma1)

# RESULTADO
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}')
    print('Você está abaixo do peso ideal')
elif imc > 18.5 < 25:
    print(f'Seu IMC é {imc:.2f}')
    print('Seu peso é ideal')
elif imc > 25 < 30:
    print(f'Seu IMC é {imc:.2f}')
    print('Você está em sobrepeso')
elif imc > 30 < 40:
    print(f'Seu IMC é {imc:.2f}')
    print('Você está em obesidade')
else:
    print(f'Seu IMC é {imc:.2f}')
    print('Você está em obesidade mórbida')
