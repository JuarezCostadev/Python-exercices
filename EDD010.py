turno = str(input('\nInsira o turno que você estuda:\n [M] - Matutino \n [V] - Vespertino \n [N] - noturno\n')).upper().strip()[0]
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor inválido! ')