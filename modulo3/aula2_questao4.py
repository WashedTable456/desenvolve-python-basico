##Requerimento de dados
classe = str(input("Escolha a classe (guerreiro, mago ou arqueiro):"))
strength = int(input("Digite os pontos de força (de 1 a 20):"))
magic_pts = int(input("Digite os pontos de magia (de 1 a 20):"))

##Processamento e comparação

m = ( classe == 'mago' )  and ( strength <= 10 and magic_pts >= 15 )
g = (classe == 'guerreiro') and (strength >= 15 and magic_pts <= 10)
a = (classe == 'arqueiro') and ( 5 < strength < 15 and 5 < magic_pts < 15)

##saída de dados

print(f"Pontos de atributo consistentes com a classe escolhida: {m or g or a}")