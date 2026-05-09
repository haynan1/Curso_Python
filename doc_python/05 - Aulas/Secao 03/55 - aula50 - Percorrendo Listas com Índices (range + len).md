# Aula 55 - Percorrendo Listas com Índices (range + len)

## Fonte

- Python editável: `conteudos/secao_3/55 - aula50.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/55 - aula50.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/04 - Coleções|Coleções]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[54 - aula49 - Estrutura FOR com LISTAS em Python|Aula 54]]
- Próxima aula: [[56 - aula51 - Empacotamento e Desempacotamento de Listas|Aula 56]]

## Ideia central

"len mede, range cria, índice acessa."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Quando trabalhamos com listas em Python, muitas vezes precisamos acessar
os elementos junto com seus índices (posição).

Para isso, usamos três coisas principais:

1) len(lista)
- Retorna a quantidade de elementos da lista.

2) range(n)
- Gera uma sequência de números de 0 até n-1.

3) lista[indice]
- Acessa o elemento naquela posição.

Fluxo do seu código:

- A lista começa com 3 nomes.
- Depois você usa append() para adicionar "João".
- Então a lista passa a ter 4 elementos.
- len(lista) retorna 4.
- range(4) gera: 0, 1, 2, 3
- O for percorre esses índices.
- A cada índice, você acessa o valor correspondente na lista.

Isso permite imprimir:

índice + valor + tipo

Esse padrão é muito usado quando precisamos saber a posição de cada item.
