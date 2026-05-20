"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# LISTAS EM PYTHON (TIPO LIST)
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
Lista é mutável, guarda de tudo e muda fácil!
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Em Python, listas (list) são estruturas de dados MUTÁVEIS, ou seja,
podem ser alteradas depois de criadas.

Características principais:

✔ Guardam múltiplos valores
✔ Aceitam diferentes tipos de dados (int, str, float, bool, listas...)
✔ São indexadas (posições começam do 0)
✔ Permitem fatiamento (slicing)
✔ São mutáveis (podem ser modificadas)

----------------------------------------

📌 Índices

Cada elemento tem uma posição:

[ 0, 1, 2, 3, 4 ]
[ -5,-4,-3,-2,-1 ]

Positivos: começam do início
Negativos: começam do final

----------------------------------------

📌 Mutabilidade

Diferente de strings, listas podem ser alteradas:

lista[2] = "Novo valor"

----------------------------------------

📌 Métodos úteis

append()  → adiciona no final
insert()  → adiciona em posição específica
pop()     → remove último ou índice
del       → remove item
clear()   → limpa tudo
extend()  → adiciona vários elementos
+         → concatena listas

----------------------------------------

📌 Booleano de lista

Lista vazia → False
Lista com valores → True
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Dada a lista abaixo, altere o valor 'Luiz Otávio' para 'Maria'
e mostre o tipo do elemento na posição 2.
"""

# Lista original
# lista = [123, True, 'Luiz Otávio', 1.2, []]

# Alterando o valor usando índice negativo (-3)
# lista[-3] = 'Maria'

# Exibindo a lista completa
# print(lista)

# Exibindo o valor e tipo do índice 2
# print(lista[2], type(lista[2]))

"""
Explicação:

- lista[-3] acessa o terceiro elemento de trás pra frente
- Esse elemento era 'Luiz Otávio'
- Foi substituído por 'Maria'
- lista[2] agora contém 'Maria'
- type(lista[2]) mostra que ainda é do tipo string (str)
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie uma lista com 3 números.
Depois, altere o segundo número para 999.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie uma lista com 5 elementos.
Use índice negativo para alterar o último elemento para 'Fim'.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie uma lista com diferentes tipos de dados.
Depois:
1. Adicione um novo valor usando append
2. Remova o primeiro elemento
3. Mostre o tamanho da lista
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Crie duas listas:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

Depois:
1. Junte as duas listas
2. Adicione o número 7 no final
3. Remova o número 3
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil
# lista = [10, 20, 30]
# lista[1] = 999
# print(lista)

# Exercício 2 - Médio
# lista = [1, 2, 3, 4, 5]
# lista[-1] = 'Fim'
# print(lista)

# Exercício 3 - Difícil
# lista = [1, 'Python', True, 3.14]
# lista.append('Novo')
# del lista[0]
# print(len(lista))

# Exercício 4 - Difícil
# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]
# lista = lista1 + lista2
# lista.append(7)
# lista.remove(3)
# print(lista)