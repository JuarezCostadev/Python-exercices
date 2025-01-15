


letra = str(input('Insira uma letra: ')).lower().strip()
vogais = 'aeiou'
if letra in 'aeiou':
    print(f'A letra {letra} é uma VOGAL!')
elif len(letra) == 1:
    print(f'A letra {letra} é CONSOANTE!')
else:
    print(f'Insira uma opção válida!')

