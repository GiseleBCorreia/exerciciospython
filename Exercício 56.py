somaidade = 0
mediaidade=0
maioridadehomem=0
nomevelho=''
totmulher20=0

for p in range(1, 5):
    print(f'----{p}ª PESSOA----')
    nome = str(input(f'Nome: ')).strip().upper()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade>maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Ff' and idade<20:
        totmulher20+=1


mediaidade = (somaidade / 4)
print(f'A média das idades é {mediaidade}')
print(f'O homem mais velho tem {idade} anos e se chama {nome}')
print(f'Ao todo tem {totmulher20} mulher(es) maior(s) de 20 anos')