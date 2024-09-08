import string

sequencia = str(input("Sequência de caracteres: "))

sequencia_tratamento = ''

for caracter in sequencia:
    if caracter in string.ascii_letters:
        sequencia_tratamento += caracter.upper()

sequencia_inverso = sequencia_tratamento[::-1]

if sequencia_tratamento == sequencia_inverso:
    print(f"A sequência {sequencia} é um palíndromo")
else:
    print(f"A sequência {sequencia} não é um palíndromo")
    
