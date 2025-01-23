nota =cont = 0

while nota <= 10:
    nota = float(input('Informe a nota tirada: '))
    cont += 1
    while nota > 10:
        print('Insira uma opção valida!')
        cont += 1
        nota = float(input('Informe a nota tirada: '))
        
        
