# Aula 02 - DOCSTRINGS E COMENTÁRIOS EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/02 - aula01.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/02 - aula01.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[01 - arquivo_de_testes_0 - 01 - arquivo_de_testes_0|Aula 01]]
- Próxima aula: [[03 - aula02 - FUNÇÃO PRINT, SEPARADOR (sep) E FINALIZAÇÃO (end)|Aula 03]]

## Ideia central

DocString explica, comentário lembra.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Em Python existem duas formas principais de escrever informações dentro
do código sem afetar o funcionamento do programa:

1) Comentários
2) DocStrings

----------------------------------------
COMENTÁRIOS (#)
----------------------------------------

Comentários são usados para explicar o que o código faz.

Eles começam com o símbolo:

#

Tudo que estiver após esse símbolo na linha será ignorado
pelo interpretador do Python.

Exemplo conceitual:

# Isso é um comentário
# O Python simplesmente ignora esta linha

Também é possível colocar comentários no final de uma linha:

print(123)  # Comentário explicando o que acontece

Nesse caso, apenas o comentário é ignorado.

----------------------------------------
DOCSTRINGS
----------------------------------------

DocStrings são blocos de texto delimitados por:

''' texto '''
ou
\"\"\" texto \"\"\"

Eles são usados principalmente para documentar:

- funções
- classes
- módulos

Exemplo conceitual:

\"\"\"
Esta função soma dois números.
\"\"\"

A diferença importante é:

DocStrings NÃO são exatamente comentários.

Eles são na verdade STRINGS (textos) válidos em Python.

Ou seja:

O Python EXECUTA essa string, mas como ela não está...
