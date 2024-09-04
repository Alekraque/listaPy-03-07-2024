print("Bem-vindo à loja de tintas!")
print("Vamos calcular quanto você vai precisar de tinta e o custo total.")

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

coberturaPorLitro = 6
litrosPorLata = 18
precoPorLata = 80.00
litrosPorGalao = 3.6
precoPorGalao = 25.00

litrosNecessarios = area / coberturaPorLitro

latasNecessarias = int(litrosNecessarios / litrosPorLata)
if litrosNecessarios % litrosPorLata != 0:
    latasNecessarias += 1

litrosRestantes = litrosNecessarios - (latasNecessarias * litrosPorLata)

galoesNecessarios = litrosRestantes * litrosPorGalao
if litrosRestantes % litrosPorGalao != 0:
    galoesNecessarios += 1

# Calcula o custo total
precoTotalLatas = latasNecessarias * precoPorLata
precoTotalGaloes = galoesNecessarios * precoPorGalao
precoTotal = precoTotalLatas + precoTotalGaloes

print(f"\nPara pintar uma área de {area:.2f} metros quadrados:")
print(f"Você precisará de {latasNecessarias} lata(s) de tinta.")
print(f"Você precisará de {galoesNecessarios} galão(ões) de tinta.")
print(f"O custo total será de R$ {precoTotal:.2f}.")
