import math

# Define as constantes
COBERTURA_POR_LITRO = 6  # metros quadrados
CAPACIDADE_LATA = 18  # litros
PRECO_LATA = 80.00  # reais
CAPACIDADE_GALAO = 3.6  # litros
PRECO_GALAO = 25.00  # reais
FOLGA = 0.10  # 10%

# Solicita ao usuário o tamanho da área a ser pintada em metros quadrados
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

# Calcula a quantidade de litros de tinta necessária
litros_necessarios = area_a_ser_pintada / COBERTURA_POR_LITRO

# Calcula a quantidade de latas de tinta necessárias (arredondando para cima)
latas_necessarias = math.ceil(litros_necessarios / CAPACIDADE_LATA)

# Calcula o preço total das latas de tinta
preco_total_latas = latas_necessarias * PRECO_LATA

# Calcula a quantidade de galões de tinta necessários (arredondando para cima)
galoes_necessarios = math.ceil(litros_necessarios / CAPACIDADE_GALAO)

# Calcula o preço total dos galões de tinta
preco_total_galoes = galoes_necessarios * PRECO_GALAO

# Calcula a quantidade de latas de tinta necessárias ao misturar latas e galões (arredondando para cima)
litros_faltantes = litros_necessarios * (1 + FOLGA)  # considerando 10% de folga
latas_misturadas = math.floor(litros_faltantes / CAPACIDADE_LATA)
litros_restantes = litros_faltantes % CAPACIDADE_LATA
galoes_misturados = math.ceil(litros_restantes / CAPACIDADE_GALAO)

# Calcula o preço total ao misturar latas e galões
preco_total_mistura = (latas_misturadas * PRECO_LATA) + (galoes_misturados * PRECO_GALAO)

# Exibe as informações ao usuário
print("Situação 1: Comprar apenas latas de 18 litros")
print(f"Quantidade de latas necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total_latas:.2f}\n")

print("Situação 2: Comprar apenas galões de 3.6 litros")
print(f"Quantidade de galões necessários: {galoes_necessarios}")
print(f"Preço total: R$ {preco_total_galoes:.2f}\n")

print("Situação 3: Misturar latas e galões")
print(f"Quantidade de latas necessárias: {latas_misturadas}")
print(f"Quantidade de galões necessários: {galoes_misturados}")
print(f"Preço total: R$ {preco_total_mistura:.2f}")
