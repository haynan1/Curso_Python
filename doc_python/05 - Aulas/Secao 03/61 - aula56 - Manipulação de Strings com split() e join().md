# Aula 61 - Manipulação de Strings com split() e join()

## Fonte

- Python editável: `conteudos/secao_3/61 - aula56.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/61 - aula56.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Dados, strings e estruturas]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[60 - aula55 - Imprecisão de Ponto Flutuante e Decimal|Aula 60]]
- Próxima aula: [[62 - aula57 - Listas dentro de Listas (Matrizes) e Índices|Aula 62]]

## Ideia central

"split separa, join reúne."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Neste conteúdo, você aprende duas funções MUITO importantes para trabalhar com texto:

1) split()
2) join()

----------------------------------------
🔹 SPLIT()
----------------------------------------

O método split() serve para DIVIDIR uma string em partes.

Exemplo:
'maçã,banana,uva'.split(',')

Resultado:
['maçã', 'banana', 'uva']

Ou seja:
- A string vira uma LISTA
- O separador (',') indica onde cortar

----------------------------------------
🔹 PROBLEMA COM ESPAÇOS
----------------------------------------

Quando usamos split(), podem sobrar espaços extras:

Exemplo:
'   Olá , mundo   '.split(',')

Resultado:
['   Olá ', ' mundo   ']

Esses espaços são "lixo" que precisamos limpar.

----------------------------------------
🔹 STRIP()
----------------------------------------

O método strip() remove espaços do início e do fim da string.

Exemplo:
'   Olá   '.strip()

Resultado:
'Olá'

----------------------------------------
🔹 JOIN()
----------------------------------------

O método join() faz o OPOSTO do split:
Ele junta uma lista em uma única string.

Exemplo:
', '.join(['maçã', 'banana'])

Resultado:
'maçã, banana'

----------------------------------------
🔹 FLUXO DO SEU...
