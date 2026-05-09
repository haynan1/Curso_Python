# Aula 18 - CONDICIONAIS NO PYTHON (if / elif / else)

## Fonte

- Python editável: `conteudos/secao_3/18 - aula17.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/18 - aula17.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/02 - Decisões|Decisões]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[17 - aula16 - CONDICIONAIS NO PYTHON (if - elif - else)|Aula 17]]
- Próxima aula: [[19 - aula18 - FLUXO DE EXECUÇÃO EM CONDICIONAIS|Aula 19]]

## Ideia central

IF testa.
ELIF testa outra.
ELSE resolve o que sobra.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Condicionais são estruturas de decisão.

Elas permitem que o programa escolha qual bloco de código executar
com base em uma condição verdadeira (True) ou falsa (False).

Estrutura básica:

if condição:
    bloco

elif outra_condição:
    outro_bloco

else:
    bloco_final

Regras importantes:

1) O Python executa apenas o primeiro bloco verdadeiro.
2) Se uma condição for verdadeira, as próximas não são verificadas.
3) O else é opcional.
4) A indentação define o bloco de execução.
5) Um novo if inicia um novo bloco independente.

No arquivo enviado, temos vários exemplos importantes:

- Uso de variáveis booleanas.
- Cadeia de elif.
- Um segundo if separado do primeiro.
- Código fora do if (executado sempre).

Isso é fundamental para entender fluxo de execução.
