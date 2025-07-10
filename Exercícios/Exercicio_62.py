# i = 1
#
# while i < 10:
#    i += 1
#    print(i)
# print("Terminou")
# print(i)

# crianças = ['Thaynara', 'Bianca', 'Yohanna']
#
# for item in crianças:
#    print(item)


# for index in range(len(crianças)):
#     print(crianças[index], index)
crianças = [
    ['joão', 'Pedro', 'Lucas'],
    ['Rodolfo', 'Ivete', 'Samuel'],
    ['Henrique', 'Bianca', 'Erick'],
    ['Yasmin'],]

matrix_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0],]

for linha in matrix_numeros:
    # print(linha)
    for coluna in linha:
        print(coluna[crianças])
