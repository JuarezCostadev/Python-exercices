valorHora = float(input('Informe o valor da sua hora trabalhada:R$ '))
horatrab = int(input('Informe as horas trabalhadas no mês: '))
salbruto = valorHora * horatrab
if salbruto <= 900:
    print('ISENTO DE DESCONTOS IR')
elif salbruto > 900 and salbruto <= 1500:
    salliquido = (salbruto - 0.05) + 0.11
    print(f'SALÁRIO BRUTO = {salbruto}\n DESCONTO DE 5% IR = {salbruto - 0.05} \n SALÁRIO LIQUIDO = {salliquido}')
elif salbruto > 1500 and salbruto <= 2500:
    salliquido = (salbruto - 0.10) + 0.11
    print(f'SALÁRIO BRUTO = {salbruto}\n DESCONTO DE 10% INSS = {salbruto - 0.10} \n SALÁRIO LIQUIDO = {salliquido}')
    
    