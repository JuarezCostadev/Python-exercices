n1 = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))

if n1 == n2:
    print(f'Os valores são iguais! ')
elif n1 > n2:
    print(f'O {n1} é MAIOR que {n2}')
else:
    print(f'O {n2} é MAIOR que {n1}')