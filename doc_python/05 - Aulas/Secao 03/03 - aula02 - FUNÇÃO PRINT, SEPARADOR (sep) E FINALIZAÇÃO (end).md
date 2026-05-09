# Aula 03 - FUNÇÃO PRINT, SEPARADOR (sep) E FINALIZAÇÃO (end)

## Fonte

- Python editável: `conteudos/secao_3/03 - aula02.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/03 - aula02.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[02 - aula01 - DOCSTRINGS E COMENTÁRIOS EM PYTHON|Aula 02]]
- Próxima aula: [[04 - aula03 - STRINGS, ASPAS E ESCAPE NO PYTHON|Aula 04]]

## Ideia central

print mostra, sep separa, end decide como termina.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

A função print() é usada para exibir informações na tela.

Ela é uma das funções mais usadas em Python e possui alguns
comportamentos padrão importantes.

----------------------------------------
ESTRUTURA BÁSICA
----------------------------------------

print(valor1, valor2, valor3)

Exemplo conceitual:

print(12, 34)

Saída esperada:

12 34

O Python automaticamente coloca um espaço entre os valores.

----------------------------------------
ARGUMENTOS NÃO NOMEADOS
----------------------------------------

Os valores dentro do print são chamados de argumentos.

Exemplo:

print(12, 34, 56)

Nesse caso temos três argumentos que serão exibidos.

----------------------------------------
PARÂMETRO sep (SEPARATOR)
----------------------------------------

O parâmetro sep define qual será o separador entre
os valores exibidos.

Por padrão o separador é um espaço.

Exemplo conceitual padrão:

print(56, 78)

Isso é equivalente a:

print(56, 78, sep=" ")

Exemplo alterando o separador:

print("Banana", "Maçã", "Pera", sep="---")

Saída conceitual:

Banana---Maçã---Pera

Ou seja, qualquer texto pode ser usado como separador.

----------------------------------------
PARÂMETRO...
