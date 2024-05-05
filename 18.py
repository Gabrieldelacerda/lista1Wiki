# Solicita ao usuário o tamanho do arquivo em MB e a velocidade do link em Mbps
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_link_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Calcula o tempo aproximado de download em minutos
# Convertendo a velocidade para MB por segundo (1 byte = 8 bits)
velocidade_link_mb_por_segundo = velocidade_link_mbps / 8
# Calcula o tempo de download em segundos
tempo_download_segundos = tamanho_arquivo_mb / velocidade_link_mb_por_segundo
# Converte o tempo de download para minutos
tempo_download_minutos = tempo_download_segundos / 60

# Exibe o tempo aproximado de download
print("O tempo aproximado de download do arquivo é de", round(tempo_download_minutos, 2), "minutos.")
