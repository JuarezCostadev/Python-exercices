from random import randint

print(20*'=-')
print('VAMOS JOGAR PAR OU ÍMPAR!!')
print(20*'=-')

valor = cont = 0 
while True:
    valor = int(input('Diga um valor: '))
    pc = randint(0, 11)
    total = valor + pc
    escolha = str(input('PAR OU IMPAR [P/I]: ')).lower().strip()[0]
    while escolha not in 'pi':
        escolha = str(input('PAR OU IMPAR [P/I]: ')).lower().strip()[0]
    print(f'Você escolheu {valor} e o computador escolheu {pc}, total = {total}')
    if escolha == 'p':
        if total % 2 == 0:
            print('VOCÊ GANHOU!')
            cont += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif escolha == 'i':
        if total % 2 == 1:
            print('VOCÊ GANHOU!')
            cont += 1
        else: 
            print('VOCÊ PERDEU!')
            break
print('Vamos jogar novamente...')
print(f'Você ganhou {cont} vezes.')
    
