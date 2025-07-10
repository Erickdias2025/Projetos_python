valor_casa = float(input('Qual o valor da casa?R$ '))
salario = float(input('Qual seu sálario mensal?R$ '))
anos = float(input('Em quantos anos pretende fazer o pagamento? '))

meses = anos * 12
prestacao = valor_casa / meses
limite = salario*0.3

if prestacao <= limite:
    print('\033[32mTudo certo, seu empréstimo foi aprovado!\033[m')
else:
    print('\033[31mOuve uma incoerençia nos dados, seu empréstimo foi negado\033[m')
