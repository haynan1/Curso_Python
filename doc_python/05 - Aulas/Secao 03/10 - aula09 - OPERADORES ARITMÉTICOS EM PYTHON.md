# Aula 10 - OPERADORES ARITMÉTICOS EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/10 - aula09.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/10 - aula09.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[09 - aula08 - VARIÁVEIS + CÁLCULOS + EXIBIÇÃO FORMATADA|Aula 09]]
- Próxima aula: [[11 - aula10 - CONCATENAÇÃO E REPETIÇÃO DE STRINGS|Aula 11]]

## Ideia central

"+ soma
- diminui
* multiplica
/ divide (float vem à tona)
// corta decimal
** potência especial
% resto é essencial"

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Neste conteúdo aprendemos os OPERADORES ARITMÉTICOS.

Eles são símbolos que realizam cálculos matemáticos.

1) Adição (+)
10 + 10 → 20

2) Subtração (-)
10 - 5 → 5

3) Multiplicação (*)
10 * 10 → 100

4) Divisão (/)
10 / 3 → 3.3333...
IMPORTANTE:
A divisão com / SEMPRE retorna float.

5) Divisão Inteira (//)
10 // 3 → 3
Remove a parte decimal.

6) Exponenciação (**)
2 ** 10 → 1024
Significa 2 elevado a 10.

7) Módulo (%)
Retorna o RESTO da divisão.
25 % 5 → 0
10 % 8 → 2

POR QUE O MÓDULO É IMPORTANTE?

Ele é muito usado para verificar:

• Se um número é par
Número par → numero % 2 == 0

• Se um número é múltiplo de outro
numero % divisor == 0

Exemplo do arquivo:

10 % 8 == 0 → False
16 % 8 == 0 → True
10 % 2 == 0 → True
15 % 2 == 0 → False
16 % 2 == 0 → True

Regra mental:

Se o resto for 0 → é divisível.
Se o resto não for 0 → não é divisível.
