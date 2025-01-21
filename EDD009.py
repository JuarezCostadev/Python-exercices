print(40*'=')
print('TABAJARA ORG')
print(40*'=')

sal = float(input('Informe o salário do colaborador:R$ '))
if sal < 280:
    aumento = 0.20
elif sal >= 280 and sal <= 700:
    aumento = 0.15
elif sal > 1500:
    aumento = 0.05
else:
    ('Insira uma opção válida! ')

reajuste = sal * aumento / 100
novosal = sal * reajuste

print(f'O salário informado foi {sal}')
print(f'O percentual de aumento foi de {aumento}%')
print(f'O novo salario foi de {novosal}')
print(f'O reajuste foi de {reajuste}')