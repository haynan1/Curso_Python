# Aula 45 - FOR + RANGE EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/45 - aula44.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/45 - aula44.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[44 - aula43 - WHILE E FOR EM PYTHON (LAÇOS DE REPETIÇÃO)|Aula 44]]
- Próxima aula: [[46 - aula45 - ITERÁVEIS E ITERADORES EM PYTHON|Aula 46]]

## Ideia central

Range cria a sequência.
For percorre a sequência.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Em Python, o comando `range()` é usado para gerar uma sequência de números.

Ele é muito utilizado junto com o laço `for`, que percorre cada elemento
dessa sequência.

A estrutura do range é:

range(início, fim, passo)

Onde:

início (start)
É o número inicial da sequência.

fim (stop)
É o limite final da sequência.
IMPORTANTE: o número final NÃO é incluído.

passo (step)
Define de quanto em quanto a sequência irá aumentar.

Exemplo:

range(0, 100, 8)

Isso significa:

Comece em 0
Vá até antes de 100
Pulando de 8 em 8

A sequência gerada será:

0
8
16
24
32
40
48
56
64
72
80
88
96

O laço `for` é responsável por percorrer essa sequência.

Estrutura:

for variável in sequência:
    ação

Cada vez que o loop roda, a variável recebe o próximo valor da sequência.
