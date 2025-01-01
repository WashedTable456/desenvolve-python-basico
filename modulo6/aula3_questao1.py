##A lista original
#Os 3 primeiros elementos
#Os 2 últimos elementos
#A lista invertida (do fim para o começo)
#Os elementos de índice par (0, 2, 4 … )
#Os elementos de índice ímpar (1, 3, 5, … )
#   
#
#


lista1 = []
n = int(input("Digite a quantidade de valores na lista(sendo o mínimo de 4 valores): "))
if n > 4 or n == 4:

    print("Digite os valores contidos na lista a seguir")
    for i in range(n):
        g = int(input())          ##formatação da estrutura de armazenamento de valores na lista criada pelo usuario   
        lista1.append(g)

    print(lista1)
    print(lista1[0:3])
    print(lista1[:1:-1])
    print(lista1[::-1])
    print(lista1[::2])
    print(lista1[1::2])
else:
    print("A lista deve possuir, pelo menos 4 elementos.")
