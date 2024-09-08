unidades = ['um', 'dois', 'três', 'quatro', 'cinco', 
            'seis', 'sete', 'oito', 'nove']
dezenas = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
           'sessenta', 'setenta', 'oitenta', 'noventa']
outros_casos = ['onze', 'doze', 'treze', 'catorze', 'quinze', 
                'dezesseis', 'dezessete', 'dezoito', 'dezenove']

while True:
    numero = int(input("Escreva um número até 99: "))
    if 1 <= numero <= 99:
        break

dezena = numero // 10
unidade = numero % 10

numero_extenso = ''

if dezena == 1:
    if unidade == 0:
        numero_extenso += 'dez'
    else:
        numero_extenso += outros_casos[unidade - 1]
elif dezena > 1:
    numero_extenso += dezenas[dezena - 1]
    if unidade != 0:
        numero_extenso += f' e {unidades[unidade - 1]}'
else:
    numero_extenso += unidades[unidade - 1]
                
print(numero_extenso)
