# Aula 54 - Estrutura FOR com LISTAS em Python

## Fonte

- Python editável: `conteudos/secao_3/54 - aula49.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/54 - aula49.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/04 - Coleções|Coleções]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[53 - aula48.5 - CUIDADOS COM DADOS MUTÁVEIS|Aula 53]]
- Próxima aula: [[55 - aula50 - Percorrendo Listas com Índices (range + len)|Aula 55]]

## Ideia central

FOR percorre, item por item, sem você precisar contar.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O laço FOR em Python é utilizado para percorrer elementos de uma sequência,
como listas, strings, tuplas, etc.

Quando usamos:

for nome in lista:

Estamos dizendo:

"Para cada elemento dentro da lista, atribua esse valor à variável 'nome'
e execute o bloco de código abaixo."

No seu exemplo:

lista = ['Maria', 'Helena', 'Luiz']

Essa lista possui 3 elementos, todos do tipo string (str).

O FOR vai funcionar assim internamente:

1ª volta → nome = 'Maria'
2ª volta → nome = 'Helena'
3ª volta → nome = 'Luiz'

A cada volta do laço, o Python executa o print.

Sobre o type(nome):
A função type() mostra o tipo de dado da variável.
Como todos os elementos da lista são textos, o tipo será sempre <class 'str'>.

Resumo:
- FOR percorre automaticamente todos os itens
- Cada item é atribuído a uma variável temporária (nome)
- O bloco interno é executado para cada item
