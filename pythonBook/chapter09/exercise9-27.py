# 9.27. Acessando os dados do tempo

import time

agora = time.localtime()

print(f"Ano: {agora.tm_year}")
print(f"Mês: {agora.tm_mon}")
print(f"Dia: {agora.tm_mday}")
print(f"Hora: {agora.tm_hour}")
print(f"Minuto: {agora.tm_min}")
print(f"Segundo: {agora.tm_sec}")
print(f"Dia da Semana: {agora.tm_wday}")
print(f"Dia do Ano: {agora.tm_yday}")
print(f"Horário de Verão: {agora.tm_isdst}")
