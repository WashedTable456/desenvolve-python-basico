## Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
##A lista ordenada, sem modificar a lista original
##A lista original
##O índice do maior valor da lista
##O índice do menor valor da lista

##Importando a biblioteca random 
import random


#construção dos laços iterativos, bem como a criação da lista
lista = []

for i in range(20):
    n = random.randint(-100, 100)
    lista.append(n)

##apenas impressao da lista para efeito comparativo
print(lista)

##impressoes com base nas exigencias do enunciado
print(sorted(lista))

print("O índice do maior valor da lista é: ",
      lista.index(max(lista)) )

print("O índice do menor valor da lista é: ",
      lista.index(min(lista)) )


