from random import randint
from os import system

with open("br-sem-acentos.txt", "r") as arquivo:
    palavras = arquivo.read().split()

indice = randint(1, len(palavras) - 1)
palavra = palavras[indice]

resposta = ['_'] * len(palavra)
contador_erros = 0

while True:
    letra = str(input('Digite uma letra: ')).lower()
    if letra in palavra:
        for indice, valor in enumerate(palavra):
            if valor == letra:
                resposta[indice] = letra
        system('cls')
        print('A palavra é:', ' '.join(resposta))
    else:
        contador_erros += 1
        print(f'-> Você errou pela {contador_erros}ª vez')

    if contador_erros==6:
        print('Você perdeu')
        print(f'A palavra era: {palavra}')
        break
    if '_' not in resposta:
        print('Você ganhou')
        break
