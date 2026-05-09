# Aula 28 - FATIAMENTO DE STRINGS (SLICING)

## Fonte

- Python editável: `conteudos/secao_3/28 - aula27.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/28 - aula27.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Strings, formatação e validação inicial]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[27 - aula26 - FORMATAÇÃO DE STRINGS COM F-STRINGS|Aula 27]]
- Próxima aula: [[29 - aula28 - VALIDAÇÃO DE DADOS + STRINGS + CONDIÇÕES|Aula 29]]

## Ideia central

Fatiar é cortar sem destruir.
[início : fim : passo] controla tudo.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

FATIAMENTO DE STRINGS (SLICING)

Uma string é uma sequência de caracteres.
Cada caractere possui uma posição (índice).

Exemplo:

  0 1 2 3 4 5 6 7 8
  O l á   m u n d o
 -9-8-7-6-5-4-3-2-1

Índices positivos começam do 0.
Índices negativos começam do -1 (último caractere).

A sintaxe do fatiamento é:

string[inicio:fim:passo]

Onde:

- início → onde começa (inclusive)
- fim → onde termina (exclusivo)
- passo → de quantos em quantos caracteres pula

Exemplos importantes:

string[0:3] → pega do índice 0 até o 2
string[:5] → do início até o índice 4
string[4:] → do índice 4 até o final
string[::2] → pega de 2 em 2
string[::-1] → inverte a string

A função len() retorna a quantidade de caracteres da string.
Espaço também conta como caractere.
