frase=str(input('Digite uma frase:')).upper().strip()
palavra=frase.split()
junto=''.join(palavra)
inverso=''
for letra in range(len(junto)-1, -1, -1):
    inverso+=junto[letra]
if inverso == junto:
    print("É um palíndromo")
else:
    print('Não é um palíndromo.')