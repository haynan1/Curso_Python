# Aula 15 - FORMATAÇÃO DE STRINGS COM .format()

## Fonte

- Python editável: `conteudos/secao_3/15 - aula14.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/15 - aula14.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[14 - aula13 - F-STRINGS (FORMATAÇÃO DE STRINGS)|Aula 14]]
- Próxima aula: [[16 - aula15 - FUNÇÃO input() E CONVERSÃO DE TIPOS|Aula 16]]

## Ideia central

"Chaves marcam.
Format substitui.
Índice organiza."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Neste conteúdo aprendemos outra forma de
formatar textos em Python:

O método .format()

Sintaxe básica:

"texto {}".format(valor)

O método format substitui os valores
que estão dentro das chaves { }.

Existem três formas principais:

1) Por ordem automática
"{} {}".format(a, b)

2) Por índice numérico
"{0} {1}".format(a, b)

3) Por nome (mais organizado)
"{nome}".format(nome=valor)

No arquivo temos:

string = "a = {nome2} b = {nome1} c = {nome3:.2f}"

Observe:

{nome2}
{nome1}
{nome3:.2f}

Depois usamos:

string.format(
    nome1=a,
    nome2=b,
    nome3=c
)

Isso significa:

nome1 → recebe valor de a
nome2 → recebe valor de b
nome3 → recebe valor de c

O :.2f significa:

:  → inicia formatação
.2 → duas casas decimais
f  → formato float

Ou seja:
1.1 virou 1.10

IMPORTANTE:

O format funciona antes das f-strings.
Hoje em dia usamos mais f-string,
mas entender format é essencial
para ler códigos antigos.

Resumo mental:

{ } marca posição.
.format() substitui.
:.2f formata número decimal.
