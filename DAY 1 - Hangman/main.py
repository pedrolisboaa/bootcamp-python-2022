from random import choice

# HANGMAN

lista_de_palavras = ['abacate', 'macaco', 'chocolate']
palavra_secreta = choice(lista_de_palavras)

letra = input('Escolha uma letra: ')

for i in palavra_secreta:
    if letra == i:
        print('certo!')
    else:
        print('Errado')

print(palavra_secreta)



