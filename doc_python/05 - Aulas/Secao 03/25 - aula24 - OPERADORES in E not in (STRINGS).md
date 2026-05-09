# Aula 25 - OPERADORES in E not in (STRINGS)

## Fonte

- Python editável: `conteudos/secao_3/25 - aula24.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/25 - aula24.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Strings, formatação e validação inicial]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[24 - aula23 - OPERADOR LÓGICO NOT|Aula 24]]
- Próxima aula: [[26 - aula25 - INTERPOLAÇÃO DE STRINGS COM %|Aula 26]]

## Ideia central

IN pergunta: "Está dentro?"
NOT IN pergunta: "Não está dentro?"

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

🔎 OPERADORES in e not in

Os operadores in e not in são usados para verificar se um valor
está contido dentro de outro valor iterável.

📌 O que é um iterável?
É qualquer estrutura que pode ser percorrida elemento por elemento.
Exemplos:
- Strings
- Listas
- Tuplas
- Dicionários
- Conjuntos

📌 Strings são iteráveis!

Exemplo:

nome = "Otávio"

Cada caractere possui um índice:

 0  1  2  3  4  5
 O  t  á  v  i  o
-6 -5 -4 -3 -2 -1

Podemos acessar caracteres usando índices positivos ou negativos.

📌 Operador in

Ele verifica se uma sequência existe dentro da string.

Exemplo:
"vio" in "Otávio" → True
"zero" in "Otávio" → False

📌 Operador not in

Faz exatamente o contrário.

"vio" not in "Otávio" → False
"zero" not in "Otávio" → True

📌 Comparação é sensível a maiúsculas e minúsculas!

"o" in "Otávio" → True
"O" in "Otávio" → True
"otávio" in "Otávio" → False

Se quiser ignorar maiúsculas/minúsculas,
podemos usar .lower().

Esses operadores são muito usados para:
- Verificar textos
- Validar entradas do usuário
- Criar filtros
- Sistemas de busca simples
