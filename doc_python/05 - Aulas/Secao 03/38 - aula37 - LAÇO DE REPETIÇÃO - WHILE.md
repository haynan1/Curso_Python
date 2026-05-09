# Aula 38 - LAÇO DE REPETIÇÃO - WHILE

## Fonte

- Python editável: `conteudos/secao_3/38 - aula37.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/38 - aula37.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[37 - aula36 - OPERADORES DE ATRIBUIÇÃO EM PYTHON|Aula 37]]
- Próxima aula: [[39 - aula38 - LAÇOS DE REPETIÇÃO - WHILE (ENQUANTO)|Aula 39]]

## Ideia central

WHILE repete ENQUANTO for verdadeiro.
Se nunca deixar de ser verdadeiro... vira pesadelo.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O laço WHILE é uma estrutura de repetição usada quando
não sabemos exatamente quantas vezes o código vai executar.

Ele funciona assim:

while condição:
    bloco de código

Enquanto a condição for verdadeira (True),
o bloco continuará executando.

⚠️ Muito cuidado:
Se a condição nunca se tornar falsa,
criamos um LOOP INFINITO.

----------------------------------------

Palavras importantes:

• contador → variável usada para controlar repetições
• continue → pula para a próxima iteração do laço
• break → encerra o laço imediatamente

----------------------------------------

Fluxo do while:

1) Verifica a condição
2) Se for True → executa o bloco
3) Volta para o início
4) Repete até a condição ser False
ou encontrar um break

----------------------------------------

Sobre o "continue":

Quando o Python encontra "continue",
ele ignora o restante do código dentro do laço
e volta para o início da repetição.

----------------------------------------

Sobre o "break":

Quando o Python encontra "break",
ele interrompe completamente o laço,
mesmo que a condição ainda seja verdadeira.
