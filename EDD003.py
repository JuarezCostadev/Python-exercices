genero = str(input('Insira seu sexo [M/F]: ')).upper().strip()[0]
if genero == 'M':
    print('Seu sexo é masculino!')
elif genero == 'F':
    print('Seu sexo é feminino!')
else:
    print('Insira um dado válido!')