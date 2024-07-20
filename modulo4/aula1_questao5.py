##Entrada de dados

n = int(input("Digite a quantidade de pessoas que participaram da pesquisa: "))
i = 0
z = n

## Processamento
while(n > 0) :
    idade_n = int(input("Idade do respondente: "))
    i = idade_n + i

    n = n - 1

media = i / z

##Saída 
print(f"A média é {media}")