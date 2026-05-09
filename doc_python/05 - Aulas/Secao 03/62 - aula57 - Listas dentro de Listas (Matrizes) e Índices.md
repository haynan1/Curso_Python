# Aula 62 - Listas dentro de Listas (Matrizes) e Índices

## Fonte

- Python editável: `conteudos/secao_3/62 - aula57.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/62 - aula57.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Dados, strings e estruturas]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[61 - aula56 - Manipulação de Strings com split() e join()|Aula 61]]
- Próxima aula: [[63 - aula58 - Interpretador do Python + Zen of Python|Aula 63]]

## Ideia central

"Lista dentro de lista: primeiro escolhe a caixa, depois o item."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Aqui estamos trabalhando com LISTAS ANINHADAS (listas dentro de listas).

Exemplo:

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

Isso significa:
- Temos uma lista principal (salas)
- Dentro dela, temos outras listas (cada sala)

----------------------------------------
🔹 COMO FUNCIONA O ÍNDICE
----------------------------------------

Para acessar um valor:

salas[linha][coluna]

Onde:
- linha → qual lista interna
- coluna → qual elemento dentro dessa lista

Exemplos:

salas[0] → ['Maria', 'Helena']
salas[0][1] → 'Helena'

salas[2][2] → 'Eduarda'

----------------------------------------
🔹 ERRO COMUM
----------------------------------------

salas[2][3]

Vai gerar erro (IndexError), porque:
- A lista 2 só tem índices 0, 1 e 2

Ou seja:
- Sempre valide o tamanho da lista com len()

----------------------------------------
🔹 LOOP EM LISTAS ANINHADAS
----------------------------------------

for sala in salas:
    for aluno in sala:
        print(aluno)

Aqui temos DOIS níveis de repetição:
- O primeiro percorre as salas
- O segundo percorre os alunos dentro da sala

----------------------------------------
🔹 INTERPRETAÇÃO...
