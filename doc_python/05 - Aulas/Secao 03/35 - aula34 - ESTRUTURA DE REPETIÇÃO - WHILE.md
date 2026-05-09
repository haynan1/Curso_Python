# Aula 35 - ESTRUTURA DE REPETIÇÃO - WHILE

## Fonte

- Python editável: `conteudos/secao_3/35 - aula34.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/35 - aula34.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[34 - aula33 - https---docs.python.org-pt-br-3-library-stdtypes.html|Aula 34]]
- Próxima aula: [[36 - aula35 - WHILE - ESTRUTURA DE REPETIÇÃO|Aula 36]]

## Ideia central

WHILE = "ENQUANTO for verdadeiro, continue repetindo."
Se não houver parada, vira loop infinito.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O laço WHILE é uma estrutura de repetição usada quando não sabemos
quantas vezes algo deve se repetir.

Ele executa um bloco de código ENQUANTO uma condição for verdadeira.

Estrutura básica:

while condicao:
    bloco_de_codigo

Fluxo de funcionamento:

1) O Python verifica a condição.
2) Se for True → executa o bloco.
3) Volta para o início.
4) Testa novamente.
5) Repete até a condição ser False.

LOOP INFINITO

Se a condição nunca se tornar False,
o programa ficará executando para sempre.
Isso é chamado de LOOP INFINITO.

Exemplo clássico:

condicao = True
while condicao:
    print("Nunca vai parar")

Esse código nunca termina porque a variável condicao
nunca muda para False.

COMO PARAR UM LOOP?

Podemos usar:

1) Alteração da condição.
2) A palavra reservada BREAK.

O BREAK força a saída imediata do loop,
mesmo que a condição ainda seja verdadeira.

No código enviado:

- A condição começa como True.
- O loop pede o nome.
- Se o usuário digitar "sair", o BREAK encerra o laço.
- Depois disso, o programa continua normalmente.
