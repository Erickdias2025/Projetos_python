salario = float(input('Qual seu salário? R$'))
# ACIMA DE 1.250 OU IGUAL É 10%, ABAIXO É 15%.

if salario >= 1.250:
    porcentagem = salario*0.10
    valor = salario+porcentagem
    print(f'Seu salário vai ser de R${valor:.3f}')
else:
    porcentagem = salario*0.15
    valor = salario+porcentagem
    print(f'Seu salário vai ser de R${valor:.3f}')
