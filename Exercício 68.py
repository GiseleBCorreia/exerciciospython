import random

print('------------------------')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('------------------------')

vitorias = 0

while True:
    n1 = int(input('Digite um valor: '))
    a2 = str(input('Par ou Ímpar [P/I]: ')).strip().upper()
    
    c = random.randint(0, 10)
    total = n1 + c

    if total % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    print('------------------------')
    print(f'Você jogou {n1} e o computador {c}. Total = {total}')

    if a2 == resultado:
        print('Você venceu! 🔥')
        vitorias += 1
    else:
        print('Você perdeu! 💀')
        break

print(f'Game over! Você venceu {vitorias} vezes.')
