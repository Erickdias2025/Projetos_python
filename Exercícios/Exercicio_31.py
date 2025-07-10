cores = {'limpa': '\033[m',
         'verde': '\033[32m'}
distancia = float(
    input(f'{cores["verde"]}QUAL A DISTÂNÇIA DA SUA VIAGEM EM KM?{cores["limpa"]}\n'))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('SUA PASSAGEM CUSTOU R${:.2f}'.format(preco))
