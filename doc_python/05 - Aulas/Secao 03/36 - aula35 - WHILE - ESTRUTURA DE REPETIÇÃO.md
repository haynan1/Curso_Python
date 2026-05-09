# Aula 36 - WHILE - ESTRUTURA DE REPETIÇÃO

## Fonte

- Python editável: `conteudos/secao_3/36 - aula35.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/36 - aula35.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[35 - aula34 - ESTRUTURA DE REPETIÇÃO - WHILE|Aula 35]]
- Próxima aula: [[37 - aula36 - OPERADORES DE ATRIBUIÇÃO EM PYTHON|Aula 37]]

## Ideia central

WHILE repete enquanto for VERDADEIRO.
Se nunca parar de ser verdadeiro… vira loop infinito.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O laço de repetição WHILE é usado quando queremos repetir um bloco de código
enquanto uma condição for verdadeira.

Estrutura básica:

while condição:
    bloco de código

A cada repetição:
1) O Python verifica a condição.
2) Se for True → executa o bloco.
3) Volta e verifica novamente.
4) Se for False → o loop termina.

IMPORTANTE:
Se a condição nunca se tornar falsa, teremos um LOOP INFINITO.

Um loop infinito acontece quando:
- A variável de controle não é atualizada.
- A condição nunca deixa de ser verdadeira.
- Esquecemos de alterar algo dentro do loop.

Sempre precisamos de:
✔ Uma variável de controle
✔ Uma condição
✔ Uma atualização dessa variável

Sem atualização → trava.
