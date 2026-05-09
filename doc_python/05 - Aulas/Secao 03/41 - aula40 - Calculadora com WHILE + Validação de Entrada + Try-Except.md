# Aula 41 - Calculadora com WHILE + Validação de Entrada + Try/Except

## Fonte

- Python editável: `conteudos/secao_3/41 - aula40.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/41 - aula40.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[40 - aula39 - ITERANDO STRINGS COM WHILE EM PYTHON|Aula 40]]
- Próxima aula: [[42 - aula41 - WHILE + ELSE EM PYTHON|Aula 42]]

## Ideia central

Enquanto o usuário quiser calcular,
o WHILE vai rodar.

Se o número der erro,
TRY tenta converter
e EXCEPT vai tratar.

Se o operador for válido,
a conta vai funcionar.

Se quiser sair,
BREAK vai encerrar.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Este programa implementa uma calculadora simples usando WHILE.

A estrutura principal é:

while True

Isso cria um LOOP INFINITO. O programa continuará executando
até que o usuário escolha sair.

Dentro do loop acontecem várias etapas importantes:

1) Entrada de dados
O usuário digita dois números e um operador matemático.

2) Conversão de tipo
Os números digitados são strings. Para realizar cálculos,
precisamos convertê-los para float.

Isso é feito com:

float(valor)

Mas se o usuário digitar algo inválido (ex: letras),
isso gera um erro.

3) Tratamento de erro (Try / Except)

try:
    tenta executar o código

except:
    executa se ocorrer erro

Isso evita que o programa quebre.

4) Validação do operador

A variável:

operadores_permitidos = "+-/*"

define quais operadores são aceitos.

Depois verificamos:

if operador not in operadores_permitidos

Se o operador não estiver na lista,
o programa pede novamente.

5) Execução da operação

Usamos IF / ELIF para verificar qual operador foi digitado.

Cada operador executa uma operação matemática diferente.

6) Pergunta se o usuário quer sair

O código:

input(...).lower().startswith("s")

faz três coisas:

lower() → transforma em...
