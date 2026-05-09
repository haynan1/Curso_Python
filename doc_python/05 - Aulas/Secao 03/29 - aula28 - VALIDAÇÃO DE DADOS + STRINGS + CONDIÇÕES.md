# Aula 29 - VALIDAÇÃO DE DADOS + STRINGS + CONDIÇÕES

## Fonte

- Python editável: `conteudos/secao_3/29 - aula28.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/29 - aula28.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Strings, formatação e validação inicial]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[28 - aula27 - FATIAMENTO DE STRINGS (SLICING)|Aula 28]]
- Próxima aula: [[30 - aula29 - INTRODUÇÃO AO TRY - EXCEPT|Aula 30]]

## Ideia central

Entrada validada evita dor de cabeça.
String bem usada mostra sua força.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Neste exercício trabalhamos três conceitos importantes:

1) input()
Recebe dados do usuário sempre como STRING.

2) Estrutura condicional (if / else)
Permite tomar decisões no código.

3) Manipulação de strings:
- Fatiamento [::-1] para inverter
- Operador "in" para verificar se contém algo
- len() para contar caracteres
- Índices [0] e [-1] para acessar primeira e última letra

⚠️ Ponto MUITO importante:

Quando usamos:

idade = int(input(...))

Se o usuário não digitar nada ou digitar algo que não seja número,
o programa gera ERRO antes mesmo de chegar no if.

Além disso:

if nome and idade:

Essa condição só será verdadeira se:
- nome não for string vazia ""
- idade não for 0

Ou seja:
Se a pessoa tiver 0 anos (hipoteticamente),
o programa cairia no else.

Uma validação mais segura seria verificar
se nome != "" e idade foi digitada corretamente.

Também é importante lembrar:
Espaço conta como caractere no len().
