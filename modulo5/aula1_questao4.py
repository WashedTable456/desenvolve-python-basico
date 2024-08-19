##Importando a biblioteca

from datetime import datetime


##Processamento de dados/

data_a = datetime.now()
hora_a = data_a.strftime('%H:%M')
data_fa = data_a.strftime('%d/%m/%Y')

print(f"Data: {data_fa}")
print(f"Hora: {hora_a}")