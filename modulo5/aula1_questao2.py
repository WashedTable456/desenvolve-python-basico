##Importação das bibliotecas


import random
import math

##Entrada de dados
n = int(input("Digite um número inteiro: "))
sum = 0

##Processamento
for i in range(n):
    f = random.randint(0,100)
    print(f) ##Método de verificação da real soma dos número da sequência de iteração: "prova visual"
    sum = sum + f
    

result = math.sqrt(sum)

##Saída de dados
print(result)