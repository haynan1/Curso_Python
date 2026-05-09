# Aula 21 - ENTENDENDO COMPARAÇÃO DE STRINGS NO PYTHON

## Fonte

- Python editável: `conteudos/secao_3/21 - aula20.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/21 - aula20.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/02 - Decisões|Decisões]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[20 - aula19 - OPERADORES DE COMPARAÇÃO (RELACIONAIS)|Aula 20]]
- Próxima aula: [[22 - aula21 - OPERADORES LÓGICOS - FOCO NO AND|Aula 22]]

## Ideia central

Se é texto, compara letra.
Se é número, converta primeiro.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

No arquivo enviado :contentReference[oaicite:0]{index=0} você fez uma comparação direta
entre dois valores usando input().

O problema principal é o seguinte:

A função input() SEMPRE retorna uma STRING.

Isso significa que quando você faz:

    if primeiro_valor > segundo_valor:

Você não está comparando números.
Você está comparando texto (ordem alfabética).

Exemplo:

"9" > "10"  → True  ❌ (errado numericamente)
Porque o Python compara caractere por caractere:
"9" vem depois de "1" na tabela ASCII.

Se a intenção é comparar números, é obrigatório converter:

int()  → números inteiros
float() → números decimais

Sobre a diferença entre as duas versões:

Sua versão:
    if primeiro_valor > segundo_valor:

Versão do professor:
    if primeiro_valor >= segundo_valor:

A diferença está no operador:

>   → maior
>=  → maior OU igual

A versão do professor também usa f-strings com a sintaxe:
    {variavel=}

Isso imprime o nome da variável junto com o valor.

Exemplo:
    x = 5
    print(f"{x=}")

Saída:
    x=5

Isso é muito útil para debug.
