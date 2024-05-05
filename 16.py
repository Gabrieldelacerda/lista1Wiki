import math

cobertura = 3
capacidade = 18
preco_lata = 80

area = float(input('Qual o tamanho da área a ser pintada? '))
litros_necessarios = area * cobertura
latas_necessarias = math.ceil(litros_necessarios / capacidade)
preco_total = latas_necessarias * preco_lata
print(f'A quantidade de latas equivale a {latas_necessarias}')
print(f'Preço total: {preco_total:.2f}')