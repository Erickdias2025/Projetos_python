# ENTRADA DAS DUAS NOTAS
nota1 = float(input('Qual a primeira nota do aluno? '))
nota2 = float(input('Qual a segunda nota do aluno? '))

# CALCULO DA MÉDIA
media = (nota1 + nota2) / 5

# VERIFICAÇÃO DA SITUAÇÃO DO ALUNO
print(f'Média final: {media:.1f}')

if media < 5.0:
    print(f'\033[31mREPROVADO\033[m')
elif 5.0 <= media <= 6.9:
    print(
        f'\033[33mRECULPERAÇÃO\033[m')
else:
    print(f'\033[32mAPROVADO\033[m')
