v1 = int(input('Insira o primeiro valor: '))
v2 = int(input('Insira o segundo valor: '))
v3 = int(input('Insira o terceiro valor: '))

if v1 > v2 > v3:
    print(f'Do maior para o menor {v1} - {v2} - {v3}')
elif v2 > v1 > v3:
    print(f'Do maior para o menor {v2} - {v1} - {v3}')
elif v3 > v2 > v1:
    print(f'Do maior para o menor {v3} - {v2} - {v1}')
elif (v1 == v2 == v3) or (v2 == v1 == v3) or (v3 == v2 == v1):
    print('Numeros iguais')
