# Aula 39 - LAÇOS DE REPETIÇÃO - WHILE (ENQUANTO)

## Fonte

- Python editável: `conteudos/secao_3/39 - aula38.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/39 - aula38.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[38 - aula37 - LAÇO DE REPETIÇÃO - WHILE|Aula 38]]
- Próxima aula: [[40 - aula39 - ITERANDO STRINGS COM WHILE EM PYTHON|Aula 40]]

## Ideia central

WHILE pergunta primeiro.
Se for verdadeiro, executa.
Se for falso, para.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O laço WHILE é uma estrutura de repetição utilizada quando NÃO sabemos
exatamente quantas vezes o código deve executar, mas sabemos que ele
deve continuar ENQUANTO uma condição for verdadeira.

Estrutura básica:

while condição:
    bloco de código

Funcionamento:

1) O Python verifica a condição.
2) Se for True → executa o bloco.
3) Volta para o início.
4) Testa novamente.
5) Repete até a condição ser False.

⚠ LOOP INFINITO
Se a condição nunca se tornar False,
o programa ficará executando para sempre.

Isso geralmente acontece quando esquecemos de atualizar
a variável de controle.

No seu exemplo temos:

- Um while externo controlando as linhas
- Um while interno controlando as colunas

Isso é chamado de LOOP ANINHADO (loop dentro de loop).

Fluxo do código:

linha = 1
Enquanto linha <= 5:
    coluna = 1
    Enquanto coluna <= 5:
        imprime valores
        coluna aumenta
    linha aumenta

Isso gera uma "grade" 5x5.
