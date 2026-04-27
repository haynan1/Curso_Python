"""Organizador seguro para arquivos e pastas do curso.

Uso recomendado:

    python tools/organizador.py --target conteudos/secao_3

Por padrao, o script apenas mostra um preview. Para executar, confirme com SIM
quando solicitado.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path


DEFAULT_UNDO_LOG = "undo_log.txt"


def limpar_prefixo_num(nome: str) -> str:
    return re.sub(r"^\d{2}\s-\s", "", nome)


def limpar_antes_primeira_letra(nome: str) -> str:
    match = re.search(r"[A-Za-z]", nome)
    return nome[match.start() :] if match else nome


def mostrar_preview(acoes: list[tuple[Path, Path]]) -> None:
    if not acoes:
        print("\nNada para alterar.\n")
        return

    print("\n--- PREVIEW (nenhuma alteracao foi feita) ---")
    for antigo, novo in acoes:
        print(f"{antigo.name}  ->  {novo.name}")
    print("-------------------------------------------\n")


def confirmar() -> bool:
    resp = input("Digite SIM para confirmar a execucao: ")
    return resp.strip().upper() == "SIM"


def salvar_undo(undo_log: Path, acoes: list[tuple[Path, Path]]) -> None:
    with undo_log.open("w", encoding="utf-8") as arquivo:
        for antigo, novo in acoes:
            arquivo.write(f"{antigo.name}|{novo.name}\n")


def executar_renomeacao(acoes: list[tuple[Path, Path]]) -> None:
    for antigo, novo in acoes:
        if novo.exists():
            print(f"Ignorado, destino ja existe: {novo.name}")
            continue
        antigo.rename(novo)


def arquivos_do_alvo(target: Path, undo_log: Path) -> list[Path]:
    excluidos = {Path(__file__).name, undo_log.name}
    return [
        item
        for item in target.iterdir()
        if item.is_file() and item.name not in excluidos and item.name != "README.md"
    ]


def pastas_do_alvo(target: Path) -> list[Path]:
    return [item for item in target.iterdir() if item.is_dir()]


def montar_acoes_reset_num(items: list[Path]) -> list[tuple[Path, Path]]:
    itens_ord = sorted(items, key=lambda item: limpar_prefixo_num(item.name))
    acoes = []

    for indice, item in enumerate(itens_ord, start=1):
        nome_limpo = limpar_prefixo_num(item.name)
        novo = item.with_name(f"{indice:02d} - {nome_limpo}")
        if item.name != novo.name:
            acoes.append((item, novo))

    return acoes


def montar_acoes_limpar_prefixos(items: list[Path]) -> list[tuple[Path, Path]]:
    acoes = []

    for item in items:
        novo = item.with_name(limpar_antes_primeira_letra(item.name))
        if item.name != novo.name:
            acoes.append((item, novo))

    return acoes


def executar_fluxo(acoes: list[tuple[Path, Path]], undo_log: Path, mensagem: str) -> None:
    mostrar_preview(acoes)

    if not acoes:
        return

    if confirmar():
        salvar_undo(undo_log, [(novo, antigo) for antigo, novo in acoes])
        executar_renomeacao(acoes)
        print(mensagem)


def desfazer(target: Path, undo_log: Path) -> None:
    if not undo_log.exists():
        print("Nenhum undo disponivel.")
        return

    acoes = []
    with undo_log.open("r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            antigo, novo = linha.strip().split("|", 1)
            origem = target / antigo
            destino = target / novo
            if origem.exists():
                acoes.append((origem, destino))

    mostrar_preview(acoes)

    if acoes and confirmar():
        executar_renomeacao(acoes)
        undo_log.unlink()
        print("Undo realizado com sucesso.")


def menu(target: Path, undo_log: Path) -> None:
    while True:
        print(
            f"""
========= ORGANIZADOR =========
Alvo: {target}

1 - Renomear ARQUIVOS (reset + numeracao)
2 - Renomear PASTAS (reset + numeracao)
3 - Limpar prefixos das PASTAS
4 - Limpar prefixos dos ARQUIVOS
5 - DESFAZER ultima execucao (UNDO)
0 - Sair
===============================
"""
        )
        op = input("Escolha uma opcao: ")

        if op == "1":
            executar_fluxo(
                montar_acoes_reset_num(arquivos_do_alvo(target, undo_log)),
                undo_log,
                "Arquivos renomeados com sucesso.",
            )
        elif op == "2":
            executar_fluxo(
                montar_acoes_reset_num(pastas_do_alvo(target)),
                undo_log,
                "Pastas renomeadas com sucesso.",
            )
        elif op == "3":
            executar_fluxo(
                montar_acoes_limpar_prefixos(pastas_do_alvo(target)),
                undo_log,
                "Prefixos removidos das pastas.",
            )
        elif op == "4":
            executar_fluxo(
                montar_acoes_limpar_prefixos(arquivos_do_alvo(target, undo_log)),
                undo_log,
                "Prefixos removidos dos arquivos.",
            )
        elif op == "5":
            desfazer(target, undo_log)
        elif op == "0":
            break
        else:
            print("Opcao invalida.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Organiza arquivos e pastas do curso.")
    parser.add_argument(
        "--target",
        default=".",
        help="Pasta que sera organizada. Ex.: conteudos/secao_3",
    )
    parser.add_argument(
        "--undo-log",
        default=DEFAULT_UNDO_LOG,
        help="Nome do arquivo de undo criado dentro da pasta alvo.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target = Path(args.target).resolve()

    if not target.exists() or not target.is_dir():
        raise SystemExit(f"Pasta alvo invalida: {target}")

    undo_log = target / args.undo_log
    os.chdir(target)
    menu(target, undo_log)


if __name__ == "__main__":
    main()
