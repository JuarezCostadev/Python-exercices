n1 = int(input('Insira o 1º valor: '))
n2 = int(input('Insira o 2º valor: '))
n3 = int(input('Insira o 3º valor: '))

# N1 MAIOR
if n1 > n2 and n1 > n3:
    print(f'O 1º valor é o MAIOR!')
# n2 MAIOR
elif n2 > n1 and n2 > n3:
    print(f'O 2º valor é o MAIOR!')
# n3 MAIOR
elif n3 > n1 and n3 > n2:
    print(f'O 3º valor é o MAIOR!')
elif n1 == n2 and n1 == n3 and n2 == n3:
    print(f'Os valores são iguais!')