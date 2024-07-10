#requerimento do valor temperatura do usuário
F = int(input('Qual a temperatura em graus Fahrenheit?'))
#Convertendo o valor para °C
C = (F - 32) * (5 / 9)
#imprimindo os valores convertidos na tela 
print(f"{F} graus Fahrenheit são {C} graus Celsius")