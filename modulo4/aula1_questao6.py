##Entrada de dados
n = int(input("quantidade de experimentos: "))
frog = 0
rat = 0
rabbit = 0

##Processamento
while(n > 0) :
    cob = int(input("quantidade de cobaias utilizadas: "))
    type_cob = input("Qualo tipo da cobaia (R, S, C): ")
    if(type_cob == 'S'):
        frog = cob + frog
    elif(type_cob == 'R'):
        rat = cob + rat
    elif(type_cob == 'C'):
        rabbit = cob + rabbit
    
    n = n - 1

#Cálculo dos dados requeridos 
total = rabbit + frog + rat
per_rat = rat / total * 100
per_frog = frog / total * 100
per_rabbit = rabbit / total * 100

##Saída 
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {rabbit}")
print(f"Total de ratos {rat}")
print(f"Total de sapos {frog}")
print(f"Percentual de coelhos: {per_rabbit} %")
print(f"Percentual de ratos: {per_rat} %")
print(f"Percentual de sapos: {per_frog} %")

