##requerimento de dados do usuario
idade  =  int(input("Digite sua idade:"))
jogos = bool(input('Já jogou pelo menos 3 jogos de tabuleiro(responta: True se sim; False se não)?'))
jogos_vencidos = int(input('Quantos jogos já venceu?'))

##processamento de dados
aptidão1 = 16 <= idade <= 18 and jogos 
aptidão = aptidão1 and  jogos_vencidos >= 1

##saída de dados
print(f'Apto para ingressar no clube de jogos de tabuleiro: {aptidão}')