cont = 0
while True:
    peso = float(input('Insira seu peso (KG): '))
    altura = float(input('Insira sua altura (M): '))
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print(f'Seu IMC é {imc:.2f} e está ABAIXO DO PESO!')
        break
    elif imc > 18.5 and imc < 24.9:
        print(f'Seu IMC é {imc:.2f}, Parabéns seu PESO É O IDEAL!')
        break
    elif imc > 24.9 and imc < 29.9:
        print(f'Seu IMC é {imc:.2f}, LEVEMENTE ACIMA DO PESO!')
        break
    elif imc > 29.9 and imc < 34.9:
        print(f'Seu IMC é {imc:.2f}, OBESIDADE GRAU I')
        break
    elif imc > 34.9 and imc < 39.9:
        print(f'Seu IMC é {imc:.2f} OBESIDADE GRAU II')
    else:
        print(f'Seu IMC é {imc:.2f} OBESIDADE GRAU III')
        break



