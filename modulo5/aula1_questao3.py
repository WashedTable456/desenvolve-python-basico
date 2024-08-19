#Importação das bibliotecas e definição do número que será advinhado
import random

n = random.randint(0,10)

##Entrada de dados e processamento


while True:
    f = int(input("Advinho o número entre 1 e 10: "))
    if f > n: 
        print("Muito alto, tente novamente")
    if f < n:
        print("Muito baixo, tente novamente!")
    if f == n:
        break

print(f"Correto! O número é {n}")
