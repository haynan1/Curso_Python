"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# Estrutura FOR com LISTAS em Python

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
FOR percorre, item por item, sem você precisar contar.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
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
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Percorra uma lista de números e mostre cada número junto com seu tipo.
"""

# lista de números
# numeros = [10, 20, 30]

# percorrendo a lista
# for numero in numeros:
#     # exibindo o valor e o tipo
#     print(numero, type(numero))

"""
Explicação do código resolvido:

- Criamos uma lista chamada 'numeros' com valores inteiros.
- O FOR percorre cada elemento da lista.
- A variável 'numero' recebe cada valor da lista.
- O print mostra o valor e o tipo (int).
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie uma lista com 3 frutas e use o FOR para imprimir cada uma delas.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie uma lista com números e use o FOR para imprimir o dobro de cada número.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie uma lista com nomes e mostre apenas aqueles que possuem mais de 5 letras.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Crie uma lista de números e conte quantos são pares usando o FOR.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil
# frutas = ['Maçã', 'Banana', 'Uva']
# for fruta in frutas:
#     print(fruta)

# Exercício 2 - Médio
# numeros = [1, 2, 3, 4, 5]
# for numero in numeros:
#     print(numero * 2)

# Exercício 3 - Difícil
# nomes = ['Ana', 'Mariana', 'Carlos', 'João']
# for nome in nomes:
#     if len(nome) > 5:
#         print(nome)

# Exercício 4 - Difícil
# numeros = [1, 2, 3, 4, 5, 6]
# contador = 0
# for numero in numeros:
#     if numero % 2 == 0:
#         contador += 1
# print(contador)
