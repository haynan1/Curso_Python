# Aula 57 - Tuplas em Python (Listas Imutáveis)

## Fonte

- Python editável: `conteudos/secao_3/57 - aula52.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/57 - aula52.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/04 - Coleções|Coleções]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[56 - aula51 - Empacotamento e Desempacotamento de Listas|Aula 56]]
- Próxima aula: [[58 - aula53 - enumerate() - Índice + Valor ao mesmo tempo|Aula 58]]

## Ideia central

"Lista muda, tupla nunca."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

A tupla é muito parecida com a lista, porém com uma diferença fundamental:

👉 Ela é IMUTÁVEL

Ou seja:
- Você NÃO pode alterar
- NÃO pode adicionar
- NÃO pode remover elementos

Exemplo de tupla:
nomes = ('Maria', 'Helena', 'Luiz')

Diferença visual:
- Lista → usa []
- Tupla → usa ()

----------------------------------------

ACESSANDO ELEMENTOS

Assim como listas, usamos índices:

nomes[0] → 'Maria'
nomes[1] → 'Helena'
nomes[2] → 'Luiz'

Também podemos usar índices negativos:

nomes[-1] → último elemento → 'Luiz'

----------------------------------------

CONVERSÕES

Você pode converter entre lista e tupla:

tuple(lista) → transforma em tupla
list(tupla) → transforma em lista

Isso é útil quando você precisa modificar algo:

1) Converte para lista
2) Faz alterações
3) Converte de volta para tupla

----------------------------------------

SEU CÓDIGO

nomes = ('Maria', 'Helena', 'Luiz')

print(nomes[-1]) → Luiz
print(nomes) → ('Maria', 'Helena', 'Luiz')

----------------------------------------

QUANDO USAR TUPLAS?

- Quando os dados NÃO devem mudar
- Para maior segurança
- Para representar dados fixos (ex: coordenadas, dias da semana)

Tuplas são mais leves e rápidas que listas...
