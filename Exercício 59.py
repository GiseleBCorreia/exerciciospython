n1=int(input('Digite o primeiro valor:'))
n2=int(input('Digite o segundo valor:'))
opção=0
print('--- Menu de opções ---')
print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior')
print('[4] Novos números')
print('[5] Sair do programa')

while opção != 5:
    opção=int(input('Digite a opção desejada:'))
    if opção == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif opção == 2:
        print(f'O resultado da multiplicação entre {n1} e {n2} é {n1*n2}')
    elif opção == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        else:
            print(f'O maior número entre {n1} e {n2} é {n2}')
    elif opção == 4:
        n1=int(input('Digite o primeiro valor:'))
        n2=int(input('Digite o segundo valor:'))
    else:
       print('Programa encerrado. Volte sempre!')
