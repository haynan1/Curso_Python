# Aula 05 - TIPOS NUMÉRICOS: INT E FLOAT NO PYTHON

## Fonte

- Python editável: `conteudos/secao_3/05 - aula04.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/05 - aula04.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[04 - aula03 - STRINGS, ASPAS E ESCAPE NO PYTHON|Aula 04]]
- Próxima aula: [[06 - aula05 - Tipo de Dado Booleano (bool) e Operador de Igualdade (==)|Aula 06]]

## Ideia central

INT é inteiro.
FLOAT flutua com ponto.
Se tem ponto, é flutuante.
Se não tem, é inteiro pronto.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

No Python, os números são classificados em tipos.

Os dois principais tipos numéricos iniciais são:

1) int
2) float

----------------------------------------
TIPO INT
----------------------------------------

O tipo int representa números inteiros.

Inteiro é todo número que NÃO possui parte decimal.
Ou seja, não possui ponto.

Exemplos:
11
-11
0
200
-999

Importante:
Se o número não tiver sinal (+ ou -),
ele é considerado positivo.

Exemplo:
11  -> positivo
-11 -> negativo

----------------------------------------
TIPO FLOAT
----------------------------------------

O tipo float representa números com ponto flutuante.
Ou seja, números que possuem parte decimal.

Exemplos:
1.1
10.11
0.0
-1.5

Importante:
Assim como no int, se o número não tiver sinal,
ele é considerado positivo.

----------------------------------------
FUNÇÃO type()
----------------------------------------

A função type() serve para descobrir
qual tipo o Python atribuiu a um valor.

Exemplo:

type(1)     -> int
type(0.0)   -> float
type("Oi")  -> str

O Python identifica automaticamente
o tipo do valor digitado.

Isso se chama INFERÊNCIA DE TIPO.
