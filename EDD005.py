nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7 and media != 10:
    print('APROVADO!')
elif media < 7:
    print('REPROVADO!')
elif media == 10:
    print('APROVADO COM MÉRITO!')
else:
    ('Insira uma opção válida!')

