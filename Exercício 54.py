x=0
for a in range(1, 8):
    ano=int(input(f'Em qual ano a {a}ª pessoa nasceu?').strip())
    conta=(2026-ano)
    if conta>=18:
        x+=1
print(f'{x} pessoas são maiores de idade.')


