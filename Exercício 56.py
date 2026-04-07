soma=0

for c in range(1,5):

    nome=str(input(f'Escreva o nome da {c}ª pessoa:')).strip().upper()

    idade=int(input(f'Escreva a idade da {c}ª pessoa:'))

    sexo=str(input(f'Escreva o sexo da {c}ª pessoa:')).strip().upper()

    soma+=idade

media=(soma/4)

print(f'A média das idade é {media}')