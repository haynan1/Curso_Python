# Aula 56 - Empacotamento e Desempacotamento de Listas

## Fonte

- Python editável: `conteudos/secao_3/56 - aula51.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/56 - aula51.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/04 - Coleções|Coleções]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[55 - aula50 - Percorrendo Listas com Índices (range + len)|Aula 55]]
- Próxima aula: [[57 - aula52 - Tuplas em Python (Listas Imutáveis)|Aula 57]]

## Ideia central

"Desempacotar é distribuir, * é guardar o resto."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Em Python, podemos "desempacotar" uma lista diretamente em variáveis.

Exemplo geral:

a, b, c = [1, 2, 3]

Cada variável recebe um valor da lista, na ordem.

Agora entra um conceito muito importante:

O operador * (asterisco)

Ele serve para capturar o "resto" dos elementos.

Exemplo:

a, *resto = [1, 2, 3, 4]

- a recebe 1
- resto recebe [2, 3, 4]

No seu caso:

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']

Vamos analisar:

- _ ignora 'Maria'
- _ ignora 'Helena'
- nome recebe 'Luiz'
- *resto recebe o que sobrar → nesse caso, nada → []

IMPORTANTE:

O "_" (underscore) é uma convenção para dizer:
"esse valor existe, mas eu não vou usar".

Saída do código:
Luiz
