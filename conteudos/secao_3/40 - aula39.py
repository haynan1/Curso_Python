"""
Iterando strings com while
"""

# #       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
# #      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ''
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'


#========================================================


#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

nome = "Haynan Kerlin"

indice = 0
novo_nome = ""
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f"*{letra}"
    indice += 1

novo_nome += "*"
print(novo_nome)




"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# ITERANDO STRINGS COM WHILE EM PYTHON

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
Enquanto houver posição na string,
o índice caminha e a letra vem.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
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
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um algoritmo que percorra uma string usando WHILE
e crie uma nova string adicionando um "*" antes de cada letra.

Exemplo:

Entrada:
Python

Saída esperada:
*P*y*t*h*o*n*
"""

# string original
# nome = "Python"

# índice começa em 0
# indice = 0

# nova string vazia
# novo_nome = ""

# enquanto o índice for menor que o tamanho da string
# while indice < len(nome):

    # pegamos a letra na posição atual
    # letra = nome[indice]

    # adicionamos "*" + letra na nova string
    # novo_nome += f"*{letra}"

    # aumentamos o índice
    # indice += 1

# adiciona o último *
# novo_nome += "*"

# mostra o resultado
# print(novo_nome)

"""
Explicação do código resolvido.

1) Criamos a string original chamada "nome".

2) Criamos um índice iniciando em 0.
Esse índice indica qual posição da string estamos lendo.

3) Criamos uma string vazia chamada "novo_nome".
Ela irá armazenar o resultado final.

4) O WHILE continua executando enquanto o índice
for menor que o tamanho da string.

5) A cada repetição pegamos a letra atual usando:

nome[indice]

6) Depois concatenamos na nova string:

"*"+letra

7) Incrementamos o índice para avançar na string.

8) No final adicionamos um "*" extra para fechar o padrão.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Percorra a string:

"Python"

e crie uma nova string onde cada letra tenha
um "-" antes dela.

Saída esperada:

-P-y-t-h-o-n-
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Percorra a string:

"Programacao"

e crie uma nova string colocando "#" antes
de cada letra.

Saída esperada:

#P#r#o#g#r#a#m#a#c#a#o#
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Percorra a string:

"Haynan"

Mas só adicione "*" nas letras que estão
em posições PARES.

Exemplo de índices:

0 H
1 a
2 y
3 n
4 a
5 n

Saída esperada:

*Ha*yn*an
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Percorra a string:

"Python"

E construa uma nova string invertida.

Saída esperada:

nohtyP

Use WHILE para fazer a inversão.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# nome = "Python"
# indice = 0
# nova = ""

# while indice < len(nome):
#     letra = nome[indice]      # pega a letra atual
#     nova += f"-{letra}"       # adiciona "-" antes da letra
#     indice += 1               # avança para próxima posição

# nova += "-"                   # fecha com "-"
# print(nova)


# Exercício 2 - Médio

# nome = "Programacao"
# indice = 0
# nova = ""

# while indice < len(nome):
#     letra = nome[indice]      # letra atual
#     nova += f"#{letra}"       # concatena "#"
#     indice += 1               # incrementa índice

# nova += "#"
# print(nova)


# Exercício 3 - Difícil

# nome = "Haynan"
# indice = 0
# nova = ""

# while indice < len(nome):

#     letra = nome[indice]

#     # verifica se o índice é par
#     if indice % 2 == 0:
#         nova += f"*{letra}"
#     else:
#         nova += letra

#     indice += 1

# print(nova)


# Exercício 4 - Difícil

# nome = "Python"

# começa do último índice
# indice = len(nome) - 1

# nova = ""

# enquanto o índice for maior ou igual a zero
# while indice >= 0:

#     letra = nome[indice]   # pega a letra
#     nova += letra          # adiciona na nova string
#     indice -= 1            # volta uma posição

# print(nova)
