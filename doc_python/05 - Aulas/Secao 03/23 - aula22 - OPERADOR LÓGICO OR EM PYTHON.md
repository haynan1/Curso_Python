# Aula 23 - OPERADOR LÓGICO OR EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/23 - aula22.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/23 - aula22.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/02 - Decisões|Decisões]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[22 - aula21 - OPERADORES LÓGICOS - FOCO NO AND|Aula 22]]
- Próxima aula: [[24 - aula23 - OPERADOR LÓGICO NOT|Aula 24]]

## Ideia central

No OR, basta um ser verdadeiro para tudo ser verdadeiro.
Ele devolve o primeiro valor verdadeiro que encontrar.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

OPERADORES LÓGICOS EM PYTHON

and  -> Todas as condições precisam ser verdadeiras.
or   -> Basta uma condição ser verdadeira.
not  -> Inverte o valor lógico.

============================
FOCO TOTAL NO OPERADOR OR
============================

O operador OR funciona da seguinte forma:

Se QUALQUER valor for verdadeiro (truthy),
a expressão inteira será considerada verdadeira.

Mas existe um detalhe MUITO importante:

O Python não retorna apenas True ou False.
Ele retorna o PRIMEIRO VALOR VERDADEIRO encontrado.

Isso se chama:
AVALIAÇÃO DE CURTO-CIRCUITO (Short-Circuit)

O Python avalia da esquerda para a direita.
Quando encontra um valor verdadeiro,
ele para imediatamente e retorna esse valor.

============================
VALORES FALSY (considerados falsos)
============================

São considerados falsos:

0
0.0
''
False
None

Qualquer outro valor é considerado TRUE (truthy).

============================
EXEMPLO CONCEITUAL
============================

0 or False or 0 or 'abc'

O Python avalia:

0 -> Falso
False -> Falso
0 -> Falso
'abc' -> Verdadeiro

Então ele retorna: 'abc'

============================
USO PRÁTICO
============================

Muito usado para definir...
