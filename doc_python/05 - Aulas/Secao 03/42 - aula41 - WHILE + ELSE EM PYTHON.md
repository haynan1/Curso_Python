# Aula 42 - WHILE + ELSE EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/42 - aula41.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/42 - aula41.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[41 - aula40 - Calculadora com WHILE + Validação de Entrada + Try-Except|Aula 41]]
- Próxima aula: [[43 - aula42 - Contagem de Frequência de Letras em uma String usando WHILE|Aula 43]]

## Ideia central

O ELSE DO WHILE SÓ EXECUTA SE O LOOP NÃO FOR QUEBRADO.
(SE NÃO TIVER BREAK)

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Em Python, o laço WHILE pode possuir um bloco ELSE.

Isso é algo pouco comum em outras linguagens, mas extremamente
importante para entender a lógica de controle de fluxo em Python.

A regra é simples:

O bloco ELSE de um WHILE só será executado se o loop terminar
NATURALMENTE.

Ou seja:

Ele executa quando a condição do WHILE se torna falsa.

Por outro lado, o ELSE NÃO executa se o loop for interrompido
com um BREAK.

Resumo da lógica:

WHILE termina naturalmente → ELSE executa.

WHILE interrompido com BREAK → ELSE NÃO executa.

Agora vamos analisar o código fornecido.

A variável "string" recebe o valor "Valorqualquer".

Depois criamos uma variável "i" com valor 0 para percorrer a
string usando índice.

A condição do WHILE é:

i < len(string)

Ou seja, o loop percorre cada posição da string.

Dentro do loop:

1) Pegamos a letra da posição atual.
2) Verificamos se ela é um espaço.
3) Se for espaço → BREAK (interrompe o loop).
4) Se não for → imprime a letra.
5) Incrementa i.

Como a string "Valorqualquer" NÃO possui espaço, o BREAK nunca
é executado.

Portanto:

O loop termina naturalmente quando i chega ao tamanho da string.

Isso faz com que o ELSE seja executado.

Depois disso...
