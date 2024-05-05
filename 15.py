# Solicita o valor do salário por hora e o número de horas trabalhadas no mês
valor_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcula o desconto para o Imposto de Renda (11%)
imposto_renda = 0.11 * salario_bruto

# Calcula o desconto para o INSS (8%)
inss = 0.08 * salario_bruto

# Calcula o desconto para o sindicato (5%)
sindicato = 0.05 * salario_bruto

# Calcula o salário líquido (após os descontos)
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

# Exibe os resultados
print("+ Salário Bruto : R$", salario_bruto)
print("- IR (11%) : R$", imposto_renda)
print("- INSS (8%) : R$", inss)
print("- Sindicato (5%) : R$", sindicato)
print("= Salário Líquido : R$", salario_liquido)
