# Aula 20 - OPERADORES DE COMPARAÇÃO (RELACIONAIS)

## Fonte

- Python editável: `conteudos/secao_3/20 - aula19.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/20 - aula19.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/02 - Decisões|Decisões]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[19 - aula18 - FLUXO DE EXECUÇÃO EM CONDICIONAIS|Aula 19]]
- Próxima aula: [[21 - aula20 - ENTENDENDO COMPARAÇÃO DE STRINGS NO PYTHON|Aula 21]]

## Ideia central

Comparou? Virou True ou False.
Relacional sempre responde boolean.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Operadores de comparação são usados para comparar valores.

Eles sempre retornam um valor booleano:
True  → Verdadeiro
False → Falso

Lista dos operadores:

>   maior que
>=  maior ou igual
<   menor que
<=  menor ou igual
==  igual
!=  diferente

Exemplos práticos:

2 > 1       → True
2 >= 2      → True
1 < 2       → True
2 <= 2      → True
'a' == 'a'  → True
'a' != 'b'  → True

Sempre que usamos um operador relacional,
o resultado será avaliado como True ou False.

Esse resultado pode ser:
- Guardado em uma variável
- Usado dentro de um if
- Usado em expressões lógicas (and / or)

No arquivo enviado, cada comparação foi armazenada
em uma variável:

maior = 2 > 1
menor = 1 < 2

Isso significa que as variáveis agora armazenam
valores booleanos.

Ou seja:
Não estamos guardando o cálculo.
Estamos guardando o resultado da comparação.
