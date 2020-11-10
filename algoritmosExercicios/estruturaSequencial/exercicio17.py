"""
1. Faça um programa que peça o tamanho de um arquivo para
    download (em MB) e a velocidade de um link de Internet (em Mbps)
"""

tamanhoMb = 100
velocidadeMbps = 100

tempoDownload = (tamanhoMb / velocidadeMbps) * 60

print("Tempo aproximado de download: {:.0f} minutos"
      .format(tempoDownload))
