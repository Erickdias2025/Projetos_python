salário = float(input('Qual o salário?\nR$ '))
resultado = salário + (salário*15/100)
print('Seu salário era de R$ {:.2f}, e agora passou a ser R$ {:.2f}. Parabéns!'.format(
    salário, resultado))
