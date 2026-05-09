# Aula 60 - Imprecisão de Ponto Flutuante e Decimal

## Fonte

- Python editável: `conteudos/secao_3/60 - aula55.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/60 - aula55.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Dados, strings e estruturas]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[59 - aula54 - Lista Interativa com Tratamento de Erros|Aula 59]]
- Próxima aula: [[61 - aula56 - Manipulação de Strings com split() e join()|Aula 61]]

## Ideia central

"Float aproxima, Decimal calcula."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Computadores NÃO armazenam números decimais exatamente como vemos.

Eles utilizam o padrão IEEE 754 (ponto flutuante), que representa números
em binário. O problema é que alguns números decimais simples, como 0.1,
não têm representação exata em binário.

Exemplo clássico:

0.1 + 0.2 != 0.3

Isso acontece porque:
- 0.1 vira algo como 0.100000000000000005...
- 0.2 vira algo como 0.200000000000000011...

Resultado:
0.30000000000000004

Para resolver isso, usamos o módulo decimal, que permite trabalhar com
precisão exata em base decimal.

IMPORTANTE:
Sempre passe números como STRING ao usar Decimal.

ERRADO:
Decimal(0.1)

CERTO:
Decimal('0.1')

Por quê?
Porque Decimal(0.1) já recebe o erro do float antes de converter.

Funções úteis:
- round(): arredonda valores
- formatação f-string: controla casas decimais
