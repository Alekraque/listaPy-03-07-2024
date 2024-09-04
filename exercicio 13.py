sexo = input("você é homem ou mulher? digite \"h\" ou \"m\": ")

if sexo == 'h':
    altura_homem = float(input('digite sua altura homi: '))
    pesohomem = (72.7*altura_homem) - 58
    print(f'seu peso ideal é {pesohomem:.2f}')
else:
    altura_mulher = float(input('digite sua altura muie: '))
    pesomuie = (62.1*altura_mulher) - 44.7
    print(f'seu peso ideal é {pesomuie:.2f}')