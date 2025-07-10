# SELEÇÃO DE NÚMEROS
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

# SOMA DOS LADOS
soma1 = (n1 + n2)
soma2 = (n2 + n3)
soma3 = (n3 + n1)

# POSSIBILIDADES FINAIS
if (soma1 >= n3) and (soma2 >= n1) and (soma3 >= n2) and (n1 == n2 == n3):
    print(
        f'Os números {n1}, {n2} e {n3} podem formam um triangulo: EQUILÁTERO')
elif (soma1 >= n3) and (soma2 >= n1) and (soma3 >= n2) and (n1 == n2 != n3):
    print(
        f'Os números {n1}, {n2} e {n3} podem formam um triangulo: ISÓSCELES')
elif (soma1 >= n3) and (soma2 >= n1) and (soma3 >= n2) and (n1 != n2 != n3):
    print(
        f'Os números {n1}, {n2} e {n3} podem formam um triangulo: ESCALENO')
else:
    print(f'Os números {n1}, {n2} e {n3} não podem formar um triangulo')
