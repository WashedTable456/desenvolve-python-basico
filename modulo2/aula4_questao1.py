#obtendo as medidas das dimensões de um terreno, bem como o preço do m²
mq = float(input('preço do m²:'))
c = int(input('qual a medida do comprimento do terreno?'))
l = int(input('qual a medida da largura do terreno?'))
#método de cálculo da área
A = c * l
#método de cálculo da área 
p = A * mq 
print(f"O terreno possui{A}m2 e custa R${p}")