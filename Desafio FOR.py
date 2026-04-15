# 1. Base de Dados (Dicionários dentro de uma Lista)
usuarios_sistema = [
    {"nome": "Ana Silva", "idade": 25, "ativo": True},
    {"nome": "João Souza", "idade": 17, "ativo": True},
    {"nome": "Beatriz Lopes", "idade": 30, "ativo": False},
    {"nome": "Marcos Pires", "idade": 15, "ativo": False},
    {"nome": "Clara Mendes", "idade": 22, "ativo": True},
    {"nome": "Roberto Carlos", "idade": 19, "ativo": False}
]

# --- INÍCIO DO DESAFIO ---

vermelho = '\033[31m'
reset = '\033[0m'

usuarios_vips=[]
usuarios_inativos=[]
for p in usuarios_sistema:
    if p['idade'] > 18 and p['ativo'] == True:
        usuarios_vips.append(p)
    elif p['ativo'] == False:
        usuarios_inativos.append(p['nome'])
print(f'Quantidade total de usuários VIPs: {len(usuarios_vips)}')
print(f'{vermelho}Lista de Atenção (Inativos):{reset}')
for nome in usuarios_inativos:
    print(nome)

# --- FIM DO DESAFIO ---
