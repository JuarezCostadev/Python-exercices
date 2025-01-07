soma = cont = media = menor = maior = 0
escolha = 'S'
while escolha in 'Ss':
    num = int(input('Insira um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
media = soma / cont
print(f'MEDIA = {media}, QUANTIDADE DE NÚMEROS {cont}, MAIOR N {maior}, MENOR N {menor}')
    