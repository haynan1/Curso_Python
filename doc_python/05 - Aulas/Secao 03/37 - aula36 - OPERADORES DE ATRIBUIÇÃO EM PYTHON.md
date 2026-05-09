# Aula 37 - OPERADORES DE ATRIBUIÇÃO EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/37 - aula36.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/37 - aula36.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[36 - aula35 - WHILE - ESTRUTURA DE REPETIÇÃO|Aula 36]]
- Próxima aula: [[38 - aula37 - LAÇO DE REPETIÇÃO - WHILE|Aula 38]]

## Ideia central

"Atribuir é guardar, operar é transformar."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Em Python, operadores de atribuição servem para guardar valores dentro de variáveis.

O operador básico é:

=  → Atribuição simples

Exemplo:
contador = 0

Significa:
"Guarde o valor 0 dentro da variável chamada contador."

----------------------------------------

Operadores de atribuição com operação:

+=   → soma e atribui
-=   → subtrai e atribui
*=   → multiplica e atribui
/=   → divide e atribui
//=  → divisão inteira e atribui
**=  → potência e atribui
%=   → resto da divisão e atribui

Esses operadores são atalhos.

Exemplo:

contador += 1

É o mesmo que escrever:

contador = contador + 1

Ou seja:
Pegue o valor atual da variável,
faça a operação,
e guarde o resultado nela mesma.

----------------------------------------

Analisando o código enviado:

contador = 0
contador += 1
print(contador)

Passo a passo mental:

1) contador começa valendo 0
2) contador += 1 → agora vale 1
3) print(contador) → exibiria 1 na tela

Importante:
+= não cria uma nova variável.
Ele apenas modifica o valor atual.

Esse padrão é muito usado para:
- contadores
- acumuladores
- controle de repetição
- soma de valores
