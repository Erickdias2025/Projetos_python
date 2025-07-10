dias = int(input('Quantos dias alugados?\n'))
km = float(input('Quantos km rodados?\n'))
pago = (dias*60)+(km*0.15)
print('O total a pagar é de R${:.2f}'.format(pago))