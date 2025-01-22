contP = total = menor = cont = 0
barato = ''
print(40*'=')
print('LOJA SUPER BARATÃO')
print(40*'=')

while True:
    nomeProduto = str(input('Informe o nome do produto: '))
    valorProduto = float(input('Informe o valor do produto:R$ '))
    cont += 1
    total += valorProduto
    if valorProduto > 1000:
        contP += 1
    if cont == 1:
        menor = valorProduto
        barato = nomeProduto
    else:
        if valorProduto < menor:
            menor = valorProduto
            barato = nomeProduto

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'O total gasto na compra foi de R$ {total}')
print(f'Ao total {contP} produto(s) custam mais de R$ 1000!')
print(f'O produto de menor valor foi {barato} que custa R$ {menor}')