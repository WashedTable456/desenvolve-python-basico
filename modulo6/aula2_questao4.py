##Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. 
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. 
# Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

##Criação das listas iniciais
lista1 = []
lista2 = []


n = int(input("Digite a quantidade de itens da primeira lista: "))
print("Digite os elementos da lista 1: ")
for i in range(n):
    f = int(input())            ##Formatação da quantidade de elementos em cada lista, conforme as exigencias do enunciado
    lista1.append(f)
print(lista1)

n = int(input("Digite a quantidade de itens da segunda lista: "))
print("Digite os elementos da lista 2: ")
for m in range(n):
    g = int(input())
    lista2.append(g)
print(lista2)


lista4 = []
lista3 = min(len(lista1), len(lista2))
print(lista3)
for p in range(lista3):
    lista4.append(lista1 [p])
    lista4.append(lista2 [p])

print(f"Lista intercalada: {lista4}")


