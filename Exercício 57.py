sexo=str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido. Digite seu sexo [M/F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')
