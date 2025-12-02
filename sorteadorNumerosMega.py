from time import sleep
from random import randint

print('-' * 40)
print('jogo da mega sena'.center(40).upper())
print('-' * 40)

jogos = []
numeros = []
cont = int(input('Quantos jogos você quer que eu sorteie?: '))

print('sorteando...'.center(40).upper())
sleep(1)

for i in range(0, cont):
    for j in range(0, 6):
        num = randint(1, 60)
        if num in numeros:
            num = randint(1, 60)
        numeros.append(num)
    numeros.sort()
    jogos.append(numeros[:])
    print(f'Jogo {i + 1}: {numeros}')
    sleep(0.5)
    numeros.clear()

print('Boa sorte!'.center(40).upper())

