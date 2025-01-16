p1 = float(input('Insira o preço do produto:R$ '))
p2 = float(input('Insira o preço do 2º produto:R$ '))
p3 = float(input('Insira o preço do último produto:R$ '))

menor = min(p1, p2, p3)

print(f'O menor preço é R$ {menor}, essa seria a escolha ideal!')