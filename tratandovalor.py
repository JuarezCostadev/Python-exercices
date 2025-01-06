valor = cont = soma = 0
valor = int(input('Insira um valor [999 PARA SAIR]: '))
while valor != 999:
    soma = soma + valor
    cont += 1
    valor = int(input('Insira um valor [999 PARA SAIR]: '))
print(f'O usuário digitou {cont} números e a soma entre eles é = {soma}')