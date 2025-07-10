preço = float(input('Qual o preço do produto?\nR$ '))
resultado = preço - (preço*5/100)
print(
    'Certo!, seu produto custava R$ {:.2f}, agora com nosso desconto incluso de 5% custará R$ {:.2f}, aproveite!'.format(preço, resultado))
