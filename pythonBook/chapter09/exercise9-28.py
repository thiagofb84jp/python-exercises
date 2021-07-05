# 9.28. Programa para gerar horas e dias

from datetime import datetime

currentDate = datetime.today()

print("SJ", currentDate.strftime('%H%M%S %d/%m'))
print("BJ", currentDate.strftime('%H%M%S %d/%m'))
print("Project", currentDate.strftime('%H%M%S %d/%m'))
