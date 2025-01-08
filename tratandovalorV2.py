num = soma = cont = 0

while True:
    num = int(input('Digite um número [999 PARA SAIR]: '))
    cont += 1
    if num == 999:
        break
    soma += num
print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma}.')