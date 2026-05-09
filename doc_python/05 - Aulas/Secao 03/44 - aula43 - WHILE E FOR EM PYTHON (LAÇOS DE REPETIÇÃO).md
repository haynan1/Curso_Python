# Aula 44 - WHILE E FOR EM PYTHON (LAÇOS DE REPETIÇÃO)

## Fonte

- Python editável: `conteudos/secao_3/44 - aula43.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/44 - aula43.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[43 - aula42 - Contagem de Frequência de Letras em uma String usando WHILE|Aula 43]]
- Próxima aula: [[45 - aula44 - FOR + RANGE EM PYTHON|Aula 45]]

## Ideia central

WHILE pergunta: "Ainda precisa repetir?"

FOR pergunta: "Quantos elementos existem para percorrer?"

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Em programação, muitas vezes precisamos repetir uma ação várias vezes.
Para isso utilizamos estruturas chamadas LAÇOS DE REPETIÇÃO.

As duas mais comuns em Python são:

1) WHILE
2) FOR

----------------------------------------
WHILE
----------------------------------------

O WHILE executa um bloco de código ENQUANTO uma condição for verdadeira.

Estrutura:

while condição:
    código

Exemplo conceitual:

while senha_errada:
    pedir_senha()

Ou seja:

"Enquanto a senha digitada for diferente da senha correta, continue pedindo."

Isso cria um LOOP.

Se a condição nunca se tornar falsa, o loop será infinito.

----------------------------------------
EXEMPLO DO SEU CÓDIGO (WHILE)
----------------------------------------

senha_salva = '123'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(...)
    repeticoes += 1

O que acontece:

1) A senha correta é "123".
2) Enquanto a senha digitada for diferente da salva...
3) O programa continua pedindo a senha.
4) Um contador registra quantas tentativas foram feitas.

----------------------------------------
FOR
----------------------------------------

O FOR é usado para percorrer...
