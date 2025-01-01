##Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. 
# Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.
# Imprima a lista antes e depois da deleção                  
import random ##importando a biblioteca para a geração de valores aleatorios

lista1 = []
for i in range(20):
    lista1.append(random.randint(-10,10))

print(lista1)
   
len_slic, ind_slic = 0, 0
len_bslic, ind_bslic = 0, 0
for i in range(20):
    n = lista1[i]
    if n < 0: 
        len_slic += 1 
        if len_slic == 1:   ##condição de inicio de uma fatia 
            ind_slic = i
    else:
        if len_slic > len_bslic :
            len_bslic = len_slic
            ind_bslic = ind_slic
        len_slic = 0            

print(ind_bslic, len_bslic)            
del lista1 [ind_bslic : len_bslic + ind_bslic]
print(lista1)