## Entrada de dados 
Δs = float(input("Digite a distância em Km: "))
m = float(input("Digite o peso(massa) do pacote em Kg: "))

##Processamento de dados

if Δs <= 100 :
    p = m * 1

if 101 <= Δs <= 300 :
    p = m * 1.50

if Δs > 300 :
    p = m * 2

if m > 10 :
    p = p + 10    

##Saída de dados
print(f"O preço da entrega é de {p}")
