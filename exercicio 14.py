joaoPescador = int(input('quantos kilos joaoPescador trouxe (digite um numero inteiro): '))
if joaoPescador < 50:
    print('você não excedeu o limite de kilos')
else:
    excesso = joaoPescador - 50
    multa = excesso*4
    print(f'joao pescador terá que pagar R${multa} pois seu excesso foi de {excesso}kg')
