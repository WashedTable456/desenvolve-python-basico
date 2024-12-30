##Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
#Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
##Ambas as listas
##A lista intersecção ordenada
##A quantidade de vezes que cada elemento aparece em cada lista

import random ##importando a biblioteca random

lista1 = []
for i in range(1, 20):##Estrutura dos laços de repetição que preencherao as listas com os valores pedidos no enunciado
    lista1.append(random.randint(0, 50))

lista2 = []
for b in range(1, 20):
    lista2.append(random.randint(0, 50))


lista3 = [] ##criação da lista interseção
for f in lista1:
    if f in lista2:
        lista3.append(f)

##retorno das listas, pedidas conforme o enunciado 

print(lista1, lista2)
lista3.sort()  ##O metodo utilizado se deve ao fato de que a função ".sort()" nao possui retorno, ao final de sua execução; apenas modifica a lista
for i in lista3:
    print(f"{i} | {lista1.count(i)}, {lista2.count(i)}")
print(lista3)


