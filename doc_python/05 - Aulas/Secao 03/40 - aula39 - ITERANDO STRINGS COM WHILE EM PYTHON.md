# Aula 40 - ITERANDO STRINGS COM WHILE EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/40 - aula39.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/40 - aula39.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[39 - aula38 - LAÇOS DE REPETIÇÃO - WHILE (ENQUANTO)|Aula 39]]
- Próxima aula: [[41 - aula40 - Calculadora com WHILE + Validação de Entrada + Try-Except|Aula 41]]

## Ideia central

Enquanto houver posição na string,
o índice caminha e a letra vem.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Em Python, uma STRING é um tipo ITERÁVEL.

Isso significa que podemos acessar cada caractere da string
usando sua POSIÇÃO (índice).

Exemplo:

nome = "Python"

Posições:

P -> índice 0
y -> índice 1
t -> índice 2
h -> índice 3
o -> índice 4
n -> índice 5

Para acessar usamos:

nome[0]
nome[1]
nome[2]

Para percorrer uma string usando WHILE precisamos de três coisas:

1) Um contador (índice)
2) Uma condição de parada
3) Atualização do contador

Estrutura geral:

indice = 0

while indice < len(string):
    letra = string[indice]
    indice += 1

FUNÇÃO len()

len() retorna o tamanho da string.

Exemplo:

nome = "Python"
len(nome) -> 6

CONSTRUÇÃO DE UMA NOVA STRING

Strings em Python são IMUTÁVEIS.

Ou seja, não podemos modificar diretamente uma string existente.

Por isso criamos uma NOVA STRING e vamos concatenando caracteres.

Exemplo:

nova = ""
nova += "P"
nova += "y"

Resultado:
"Py"

USO DO F-STRING

f"{variavel}"

Serve para inserir variáveis dentro de strings.

Exemplo:

letra = "A"

f"*{letra}" -> "*A"

OBJETIVO DO ALGORITMO

Transformar:

Haynan Kerlin

em:

*H*a*y*n*a*n* *K*e*r*l*i*n*

Ou seja, colocar um * antes de cada caractere.
