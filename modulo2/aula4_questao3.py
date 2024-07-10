#coletando os dados dos nomes e preços dos respectivos produtos
#prodduto 1 
i1 = str(input('Digite o nome do produto 1:'))
p1_u = float(input('Digite o preço unitário do produto 1:'))
q1 = int(input('Digite a quantidade do produto 1::'))

#produto 2 
i2 = str(input('Digite o nome do produto 2:'))
p2_u = float(input('Digite o preço unitário do produto 2:'))
q2 = int(input('Digite a quantidade do produto 2:'))

#produto 3
i3 = str(input('Digite o nome do produto 3:'))
p3_u = float(input('Digite o preço unitário do produto 3:'))
q3 = int(input('Digite a quantidade do produto 3:'))

#cáculo do valor total em R$ da compra
T= p1_u * q1 + p2_u * q2 + p3_u * q3

#imprimindo o valor da compra para o usuário

print(f'Total: R${T:,.2f}')
