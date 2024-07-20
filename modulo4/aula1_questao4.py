##Entrada de dados

n = int(input("Digite um número inteiro: "))
maior = 0

##Processamento
while(n > 0) :
    x = int(input("Digite um número inteiro para a variável x: "))
    if(x > maior) :
        maior = x
    n = n - 1

#Saída

print("maior")