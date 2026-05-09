# Aula 22 - OPERADORES LÓGICOS - FOCO NO AND

## Fonte

- Python editável: `conteudos/secao_3/22 - aula21.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/22 - aula21.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/02 - Decisões|Decisões]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[21 - aula20 - ENTENDENDO COMPARAÇÃO DE STRINGS NO PYTHON|Aula 21]]
- Próxima aula: [[23 - aula22 - OPERADOR LÓGICO OR EM PYTHON|Aula 23]]

## Ideia central

AND é exigente:
Se UM falhar, tudo para.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Operadores Lógicos são usados para combinar condições.

Os principais operadores são:

and  -> e
or   -> ou
not  -> não

Hoje o foco é no operador AND.

==================================================
COMO O AND FUNCIONA?
==================================================

O operador AND exige que TODAS as condições sejam verdadeiras.

Exemplo simples:

True and True   -> True
True and False  -> False
False and True  -> False
False and False -> False

Ou seja:

Se qualquer parte da expressão for falsa,
o resultado inteiro será falso.

==================================================
FALSY (Valores considerados falsos)
==================================================

No Python, alguns valores são considerados False
mesmo que não sejam o tipo bool.

São chamados de FALSY:

0
0.0
'' (string vazia)
False
None

Qualquer outro valor normalmente é considerado True.

==================================================
AVALIAÇÃO DE CURTO-CIRCUITO
==================================================

O AND funciona com algo chamado "curto-circuito".

Ele avalia da esquerda para a direita.
Se encontrar um valor falso, ele para ali mesmo.

Exemplo:

True and 0 and True

O Python...
