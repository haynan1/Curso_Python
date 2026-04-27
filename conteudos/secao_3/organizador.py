import os
import re

PASTA = '.'
UNDO_LOG = 'undo_log.txt'
SCRIPT_ATUAL = os.path.basename(__file__)

ARQUIVOS_EXCLUIDOS = {SCRIPT_ATUAL, UNDO_LOG}

# ---------- Funções utilitárias ----------

def limpar_prefixo_num(nome):
    return re.sub(r'^\d{2}\s-\s', '', nome)

def limpar_antes_primeira_letra(nome):
    match = re.search(r'[A-Za-z]', nome)
    return nome[match.start():] if match else nome

def mostrar_preview(acoes):
    if not acoes:
        print("\nNada para alterar.\n")
        return
    print("\n--- PREVIEW (nenhuma alteração foi feita) ---")
    for antigo, novo in acoes:
        print(f"{antigo}  ->  {novo}")
    print("-------------------------------------------\n")

def confirmar():
    resp = input("Digite SIM para confirmar a execução: ")
    return resp.strip().upper() == "SIM"

def salvar_undo(acoes):
    with open(UNDO_LOG, 'w', encoding='utf-8') as f:
        for antigo, novo in acoes:
            f.write(f"{antigo}|{novo}\n")

def executar_renomeacao(acoes):
    for antigo, novo in acoes:
        if not os.path.exists(novo):
            os.rename(antigo, novo)

# ---------- Operações ----------

def renomear_arquivos():
    arquivos = [
        f for f in os.listdir(PASTA)
        if os.path.isfile(f) and f not in ARQUIVOS_EXCLUIDOS
    ]

    arquivos_ord = sorted(arquivos, key=limpar_prefixo_num)

    acoes = []
    for i, nome in enumerate(arquivos_ord, start=1):
        nome_limpo = limpar_prefixo_num(nome)
        novo_nome = f"{i:02d} - {nome_limpo}"
        if nome != novo_nome:
            acoes.append((nome, novo_nome))

    mostrar_preview(acoes)
    if acoes and confirmar():
        salvar_undo([(novo, antigo) for antigo, novo in acoes])
        executar_renomeacao(acoes)
        print("✔ Arquivos renomeados com sucesso.")

def renomear_pastas():
    pastas = [
        p for p in os.listdir(PASTA)
        if os.path.isdir(p)
    ]

    pastas_ord = sorted(pastas, key=limpar_prefixo_num)

    acoes = []
    for i, nome in enumerate(pastas_ord, start=1):
        nome_limpo = limpar_prefixo_num(nome)
        novo_nome = f"{i:02d} - {nome_limpo}"
        if nome != novo_nome:
            acoes.append((nome, novo_nome))

    mostrar_preview(acoes)
    if acoes and confirmar():
        salvar_undo([(novo, antigo) for antigo, novo in acoes])
        executar_renomeacao(acoes)
        print("✔ Pastas renomeadas com sucesso.")

def limpar_prefixos_pastas():
    pastas = [
        p for p in os.listdir(PASTA)
        if os.path.isdir(p)
    ]

    acoes = []
    for nome in pastas:
        novo_nome = limpar_antes_primeira_letra(nome)
        if nome != novo_nome:
            acoes.append((nome, novo_nome))

    mostrar_preview(acoes)
    if acoes and confirmar():
        salvar_undo([(novo, antigo) for antigo, novo in acoes])
        executar_renomeacao(acoes)
        print("✔ Prefixos removidos das pastas.")

def limpar_prefixos_arquivos():
    arquivos = [
        f for f in os.listdir(PASTA)
        if os.path.isfile(f) and f not in ARQUIVOS_EXCLUIDOS
    ]

    acoes = []
    for nome in arquivos:
        novo_nome = limpar_antes_primeira_letra(nome)
        if nome != novo_nome:
            acoes.append((nome, novo_nome))

    mostrar_preview(acoes)
    if acoes and confirmar():
        salvar_undo([(novo, antigo) for antigo, novo in acoes])
        executar_renomeacao(acoes)
        print("✔ Prefixos removidos dos arquivos.")

def desfazer():
    if not os.path.exists(UNDO_LOG):
        print("❌ Nenhum undo disponível.")
        return

    with open(UNDO_LOG, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    acoes = []
    for linha in linhas:
        antigo, novo = linha.strip().split('|')
        if os.path.exists(antigo):
            acoes.append((antigo, novo))

    mostrar_preview(acoes)
    if acoes and confirmar():
        executar_renomeacao(acoes)
        os.remove(UNDO_LOG)
        print("✔ Undo realizado com sucesso.")

# ---------- Menu ----------

def menu():
    while True:
        print("""
========= ORGANIZADOR =========
1 - Renomear ARQUIVOS (reset + numeração)
2 - Renomear PASTAS (reset + numeração)
3 - Limpar prefixos das PASTAS
4 - Limpar prefixos dos ARQUIVOS
5 - DESFAZER última execução (UNDO)
0 - Sair
===============================
""")
        op = input("Escolha uma opção: ")

        if op == '1':
            renomear_arquivos()
        elif op == '2':
            renomear_pastas()
        elif op == '3':
            limpar_prefixos_pastas()
        elif op == '4':
            limpar_prefixos_arquivos()
        elif op == '5':
            desfazer()
        elif op == '0':
            break
        else:
            print("Opção inválida.")

menu()
