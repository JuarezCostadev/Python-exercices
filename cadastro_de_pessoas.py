cont18 = contH = contM = 0

while True:
    print(40*'=')
    print('CADASTRE UMA PESSOA')
    idade = int(input('Digite sua idade: '))
    print(40*'=')
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        contH += 1
    if sexo == 'F' and idade < 20:
        contM += 1  
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if escolha == 'N':
        break
   
print(f'total de pessoas com mais de 18 anos = {cont18}')
print(f'total de homens cadastrados = {contH}')
print(f'O total de mulheres menores de 20 anos foi de {contM}')

        
        

