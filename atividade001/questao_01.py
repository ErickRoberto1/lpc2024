from random import randint

dado_valores = []
contador = [0, 0, 0, 0, 0, 0]

for _ in range(100):
    dado_valores.append(randint(1, 6))
print(dado_valores)

for valor in dado_valores:
    contador[valor - 1] += 1

for numero, vezes in enumerate(contador):
    print(f"Número: {numero + 1} - Vezes: {vezes}") 