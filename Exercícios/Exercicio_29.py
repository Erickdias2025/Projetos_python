cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[4;32m'}
v = int(input(
    f'{cores["verde"]}EM QUAL VELOCIDADE ESTAVA O VEÍCULO?{cores["limpa"]}\nKM/H '))
limite = 80
multa = 7.00
if v > 80:
    km_acima = v - limite
    valor_multa = km_acima * multa
    print(
        f'{cores["vermelho"]}VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE EM {km_acima}KM/H {cores["limpa"]}')
    print(
        f'{cores["vermelho"]}A MULTA VAI CUSTAR R$ {valor_multa:.2f}{cores["limpa"]}')
else:
    print(
        f'{cores["verde"]}VOCÊ ESTÁ DENTRO DO LIMITE DE VELOCIDADE. SEM MULTA.{cores["limpa"]}')
