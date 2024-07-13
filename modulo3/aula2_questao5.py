##entrada de dados
genero = str(input("Digiite o seu gênero: "))
idade = int(input("Digite a sua idade: "))
tm_serviço = int(input("Tempo de serviço: "))


##processamento de dados
A = (genero == 'F' and idade >= 60) or (genero == 'M' and idade >= 65)
B = (tm_serviço >= 30)
C = (idade >= 60 and tm_serviço >= 25)

##saída de dados

print(f"Concessão da aposentadoria: {A or B or C}" )