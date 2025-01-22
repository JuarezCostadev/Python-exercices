from xml.etree.ElementTree import tostring


print(40*'=')
print('{:^30}BANCO UNIV')
print(40*'=')
valor = int(input('Insira o valor a ser sacado:R$ '))
ced = 50
totalced = 0 
total = valor
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break




