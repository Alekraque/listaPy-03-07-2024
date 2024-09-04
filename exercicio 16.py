print("Bem-vindo à loja de tintas!")
print("Vamos calcular quanto você vai precisar de tinta e o custo total.")

area_str = input("Digite o tamanho da área a ser pintada em metros quadrados: ")


if area_str.replace('.', '', 1).isdigit() and area_str.count('.') <= 1:
    area = float(area_str)
    if area > 0:
        cobertura_por_litro = 3  # metros quadrados que 1 litro de tinta cobre
        litros_por_lata = 18  # litros por lata
        preco_por_lata = 80.00  # preço de cada lata

        litros_necessarios = area / cobertura_por_litro

        latas_necessarias = int(litros_necessarios / litros_por_lata)
        if litros_necessarios % litros_por_lata != 0:
            latas_necessarias += 1

        preco_total = latas_necessarias * preco_por_lata

        print(
            f"\nPara pintar uma área de {area:.2f} metros quadrados, você precisará de {latas_necessarias} lata(s) de tinta.")
        print(f"O custo total será de R$ {preco_total:.2f}.")
        print("Obrigado por usar nosso serviço!")
    else:
        print("A área deve ser um número positivo.")
else:
    print("Por favor, insira um número válido para a área.")
