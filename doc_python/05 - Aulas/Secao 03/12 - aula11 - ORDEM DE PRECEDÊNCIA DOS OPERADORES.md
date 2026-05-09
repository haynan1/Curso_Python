# Aula 12 - ORDEM DE PRECEDÊNCIA DOS OPERADORES

## Fonte

- Python editável: `conteudos/secao_3/12 - aula11.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/12 - aula11.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[11 - aula10 - CONCATENAÇÃO E REPETIÇÃO DE STRINGS|Aula 11]]
- Próxima aula: [[13 - aula12 - CÁLCULO DE IMC + USO DE EXPRESSÕES|Aula 13]]

## Ideia central

"Parênteses primeiro.
Potência depois.
Multiplica e divide.
Soma e subtrai por fim."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Na matemática (e no Python), existe uma ORDEM
em que os cálculos são executados.

Isso se chama PRECEDÊNCIA DE OPERADORES.

A ordem correta é:

1) ( )  → Parênteses
2) **   → Exponenciação
3) * / // % → Multiplicação e divisões
4) + -  → Soma e subtração

Vamos analisar o exemplo do arquivo:

conta_1 = 1 + 1 ** 5 + 5

Passo 1 → Resolver a potência:
1 ** 5 = 1

Agora a conta vira:
1 + 1 + 5

Passo 2 → Resolver da esquerda para a direita:
1 + 1 = 2
2 + 5 = 7

Resultado final:
7

IMPORTANTE:

Mesmo que a soma esteja antes no código,
a potência é resolvida primeiro.

Se quisermos mudar a ordem,
usamos parênteses.

Exemplo:

(1 + 1) ** 5 + 5

Agora primeiro resolve:
(1 + 1) = 2

Depois:
2 ** 5 = 32

Depois:
32 + 5 = 37

Resultado completamente diferente.

Regra mental:

Sem parênteses → siga a hierarquia.
Com parênteses → eles mandam.
