##Importação de bibliotecas

import emoji

##Entrda de dados/ apresentação dos emojis disponíveis


print("Emojis disponíveis: ")

print(emoji.emojize(':red_heart:'),'  - :red_heart:')
print(emoji.emojize(':thumbs_up:'),' - :thumbs_up:')
print(emoji.emojize(':thinking_face:'),' - :thinking_face:')
print(emoji.emojize(':partying_face:'),' - :partying_face:')

n = str(input("Digite uma frase e ela será emojizada: "))

##Saída de dados

print("Frase emojizada:")
print(emoji.emojize(n))