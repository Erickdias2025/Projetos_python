from random import shuffle
n1 = str(input('Primeiro Aluno(A): '))
n2 = str(input('Segundo Aluno(A): '))
n3 = str(input('Terceiro Aluno(A): '))
n4 = str(input('Quarto Aluno(A): '))
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('Siga a ordem da apresentação')
print(alunos)
