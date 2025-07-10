nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
# print('O primeiro nome tem {} Letras'.format(nome.find(' ')))
separa = nome.split()
print('O seu primeiro nome é: {} e ele tem {} letras'.format(
    separa[0], len(separa[0])))
