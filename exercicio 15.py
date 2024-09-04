salario = int(input('quanto você ganha por hora: '))
horas = int(input('e quantas horas você trabalha no mês: '))

salarioBruto = salario * horas
print(f'seu salário no mês é {salarioBruto}')

renda = 0.11
inss = 0.08
sindico = 0.05

comRenda = salarioBruto * renda
comInss = salarioBruto * inss
comSindico = salarioBruto * sindico
todosImpostos = comSindico + comInss + comRenda
salarioLiquido = salarioBruto - todosImpostos

print(f'você tem o desconto de R${todosImpostos} e o seu salario liquido é R${salarioLiquido}')
