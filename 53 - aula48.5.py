"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


'''Outra forma de fazer, mas difente do exemplo mostrado acima.'''

print('\n',5 * '----')
lista_a = lista_b = ['Luiz', 'Maria', 1, True, 1.2]
print(lista_a)
print(lista_b)

"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# CUIDADOS COM DADOS MUTÁVEIS
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Lista compartilhada muda em dupla, cópia separada evita a confusão."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Em Python, existe uma diferença MUITO IMPORTANTE entre:

1. ATRIBUIÇÃO (=)
2. CÓPIA (.copy())

========================
1. ATRIBUIÇÃO (=)
========================

Quando fazemos:

lista_b = lista_a

NÃO estamos criando uma nova lista.

Estamos apenas criando outra variável que aponta para o MESMO espaço na memória.

Ou seja:
lista_a e lista_b são a MESMA lista.

Se alterar uma, altera a outra.

========================
2. CÓPIA (.copy())
========================

Quando usamos:

lista_b = lista_a.copy()

Agora sim criamos uma NOVA lista.

Ela tem os mesmos valores, mas ocupa outro espaço na memória.

Ou seja:
Alterar lista_a NÃO afeta lista_b.

========================
RESUMO SIMPLES
========================

=  → aponta para o mesmo objeto (perigoso com mutáveis)
copy() → cria um novo objeto (seguro)

========================
IMPORTANTE
========================

Listas são MUTÁVEIS, então esse cuidado é essencial.

Tipos imutáveis (int, str, float, bool) não sofrem esse problema.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Dada a lista:

lista_a = ['Luiz', 'Maria', 1, True, 1.2]

Faça:
1. Crie uma cópia usando .copy()
2. Altere o primeiro valor de lista_a
3. Mostre as duas listas
"""

# Criando lista original
# lista_a = ['Luiz', 'Maria', 1, True, 1.2]

# Criando uma cópia independente
# lista_b = lista_a.copy()

# Alterando o primeiro elemento da lista_a
# lista_a[0] = 'Qualquer coisa'

# Exibindo lista_a (modificada)
# print(lista_a)

# Exibindo lista_b (permanece igual)
# print(lista_b)

"""
Explicação:

1. lista_b = lista_a.copy()
→ cria uma nova lista independente

2. lista_a[0] = 'Qualquer coisa'
→ altera apenas lista_a

3. Resultado:

lista_a = ['Qualquer coisa', 'Maria', 1, True, 1.2]
lista_b = ['Luiz', 'Maria', 1, True, 1.2]

Ou seja:
As listas são diferentes na memória.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie uma lista com 3 nomes.
Atribua ela a outra variável usando =.
Altere um valor e observe o resultado.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Repita o exercício anterior, mas usando .copy().
Explique a diferença.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie uma lista com números.
Crie duas variáveis:
uma usando = e outra usando .copy().

Altere a lista original e observe quais mudam.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Explique com suas palavras:

Qual a diferença entre:
lista_b = lista_a
e
lista_b = lista_a.copy()
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil
# lista1 = ['Ana', 'João', 'Carlos']   # lista original
# lista2 = lista1                     # aponta para mesma lista
# lista1[0] = 'Pedro'                 # altera lista1
# print(lista2)                       # também muda → ['Pedro', 'João', 'Carlos']

# Exercício 2 - Médio
# lista1 = ['Ana', 'João', 'Carlos']  # lista original
# lista2 = lista1.copy()              # cria cópia
# lista1[0] = 'Pedro'                 # altera lista1
# print(lista2)                       # NÃO muda → ['Ana', 'João', 'Carlos']
# Diferença:
# = compartilha memória
# copy cria nova lista

# Exercício 3 - Difícil
# lista = [1, 2, 3]                   # lista original
# lista_ref = lista                  # referência (mesma memória)
# lista_copy = lista.copy()          # cópia independente
# lista[0] = 999                     # altera original
# print(lista_ref)                   # muda → [999, 2, 3]
# print(lista_copy)                  # não muda → [1, 2, 3]

# Exercício 4 - Difícil
# lista_b = lista_a
# → mesma lista na memória (alterações afetam ambas)
# lista_b = lista_a.copy()
# → nova lista independente (alterações não afetam a outra)
