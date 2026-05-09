# Aula 11 - CONCATENAÇÃO E REPETIÇÃO DE STRINGS

## Fonte

- Python editável: `conteudos/secao_3/11 - aula10.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/11 - aula10.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[10 - aula09 - OPERADORES ARITMÉTICOS EM PYTHON|Aula 10]]
- Próxima aula: [[12 - aula11 - ORDEM DE PRECEDÊNCIA DOS OPERADORES|Aula 12]]

## Ideia central

"Com + eu junto.
Com * eu multiplico texto."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Neste conteúdo aprendemos dois comportamentos
importantes do operador + e do operador * com STRINGS.

1) CONCATENAÇÃO (+)

Quando usamos + entre strings (str),
o Python junta os textos.

Exemplo:
"A" + "B" + "C"
Resultado: "ABC"

Também podemos juntar palavras com espaço:

"Haynan" + " " + "Kerlin"

Perceba que o espaço precisa estar dentro de " ".

IMPORTANTE:
O operador + pode:
- Somar números
- Concatenar textos

Mas:
int + str → ERRO
Os tipos precisam ser compatíveis.

2) REPETIÇÃO DE STRING (*)

Quando multiplicamos uma string por um número inteiro,
o Python repete o texto.

"A" * 10
Resultado: "AAAAAAAAAA"

3 * "haynan"
Resultado: "haynanhaynanhaynan"

Regra mental:

str + str → junta
str * int → repete
int * str → também repete
str * str → ERRO

Isso é muito usado para:
• Criar linhas decorativas
• Gerar padrões
• Formatar saídas
