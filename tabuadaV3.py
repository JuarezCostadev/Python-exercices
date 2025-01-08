valor = cont = 0

while True:
    valor = int(input('Quer ver a tabuada de qual número? '))
    if valor < 0:
        break
    print('-=' * 30)
    for c in range(0 ,11):
        print(f'{valor} X {c} = {valor * c}')

    print('-=' * 30)



   