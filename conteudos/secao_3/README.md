# Seção 3 - Arquivos de aula em Python

Esta pasta reúne os arquivos Python usados como base e apoio da seção 3 do curso.

## Convenção atual

- Os arquivos são ordenados por prefixo numérico.
- O padrão principal é `NN - aulaXX.py`.
- Arquivos com nomes especiais, como `arquivo_de_testes_0.py`, devem ser mantidos apenas quando forem úteis como rascunho ou demonstração.

## Como adicionar uma aula

1. Copie `../../templates/nova_aula.py`.
2. Renomeie seguindo a próxima numeração disponível.
3. Preencha título, objetivo, exemplos e exercícios.
4. Rode o arquivo no Python para verificar erros de sintaxe.

## Ferramenta de organização

O script de organização fica em `../../tools/organizador.py`.

Exemplo:

```bash
python ../../tools/organizador.py --target .
```

Use sempre o preview antes de confirmar qualquer renomeação.
