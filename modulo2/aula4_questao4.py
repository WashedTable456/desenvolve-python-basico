#entrada de dados
n = int(input("Digite um número inteiro: "))

#processamento

### Começas da nota de maior valor até a nota de menor valor
n_100 = n // 100
###Atualização de quanto falta, e  assim por diante ...
n = n % 100 

n_50 = n // 50 
n = n % 50

n_20 = n // 20
n = n % 20

n_10 = n // 10
n = n % 10 

n_5 = n // 5
n = n % 5

n_2 = n // 2
resto = n % 2

n_1 = resto

#Saída dos dados

print(f"{n_100}nota(s) de R$100,00")
print(f"{n_50}nota(s) de R$50,00")
print(f"{n_20}nota(s) de R$20,00")
print(f"{n_10}nota(s) de R$10,00")
print(f"{n_5}nota(s) de R$5,00")
print(f"{n_2}nota(s) de R$2,00")
print(f"{n_1}nota(s) de R$1,00")