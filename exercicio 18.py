arquivo = float(input('Digite um tamanho de arquivo em MB: '))
velocidade = float(input('Digite a velocidade em Mbps(MB por segundos): '))

totalDeVelocidade = arquivo / velocidade
totalEmMinutos = totalDeVelocidade / 60

if totalEmMinutos != int(totalEmMinutos):
    totalEmMinutos = int(totalEmMinutos) + 1
else:
    totalEmMinutos = int(totalEmMinutos)
print(f'a velocidade de mb por minuto é de {totalEmMinutos:.2f}')
