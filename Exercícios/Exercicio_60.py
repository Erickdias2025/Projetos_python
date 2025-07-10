while True:
    n = int(input('QUER VER A TABUADA DE QUAL VALOR? '))
    print('-'*33)
    if n < 0:
        break

    for c in range(1, 11):
        s = n*c
        print(f'{n} X {c:2} = {s}')
print('FIM')
