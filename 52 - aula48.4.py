"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# LISTAS EM PYTHON (LIST)
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Lista guarda, muda e cresce — índice acessa, método fortalece."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Em Python, a LISTA (list) é uma estrutura de dados MUTÁVEL, ou seja,
podemos alterar seus valores depois de criada.

Ela é usada para armazenar vários dados em uma única variável.

Exemplo:
lista = [1, 2, 3]

Características importantes:

1. MUTÁVEL:
Podemos alterar, adicionar ou remover elementos.

2. ACEITA QUALQUER TIPO:
Pode conter números, strings, booleanos, até outras listas.

3. INDEXAÇÃO:
Cada elemento tem uma posição (índice), começando do 0.

Exemplo:
lista[0] → primeiro elemento

4. FATIAMENTO:
Permite pegar partes da lista:
lista[1:3]

========================
PRINCIPAIS OPERAÇÕES (CRUD)
========================

C → Create (Criar)
R → Read (Ler)
U → Update (Atualizar)
D → Delete (Deletar)

Exemplo:
lista[i] = valor

========================
MÉTODOS IMPORTANTES
========================

append(valor)
→ adiciona no FINAL

insert(indice, valor)
→ adiciona em posição específica

pop(indice)
→ remove elemento (último por padrão)

del lista[indice]
→ deleta diretamente

clear()
→ limpa toda lista

extend(lista)
→ adiciona vários elementos de outra lista

+ (concatenação)
→ junta duas listas (gera nova lista)

========================
DIFERENÇA IMPORTANTE
========================

+ (concatenação):
Cria uma NOVA lista

extend():
MODIFICA a lista original
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Dadas duas listas:

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

Faça:
1. Crie uma nova lista com +
2. Use extend para juntar lista_b em lista_a
3. Mostre o resultado final de lista_a
"""

# Criando lista_a
# lista_a = [1, 2, 3]

# Criando lista_b
# lista_b = [4, 5, 6]

# Concatenando (gera nova lista)
# lista_c = lista_a + lista_b

# Estendendo lista_a (modifica ela)
# lista_a.extend(lista_b)

# Exibindo resultado final
# print(lista_a)

"""
Explicação:

1. lista_c = lista_a + lista_b
→ cria uma nova lista com os elementos das duas

2. lista_a.extend(lista_b)
→ altera a lista_a original, adicionando os valores de lista_b

3. Resultado final:
lista_a = [1, 2, 3, 4, 5, 6]

Ou seja:
+ → cria nova lista
extend → modifica a existente
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie uma lista com 3 números.
Adicione um quarto número usando append.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie uma lista com 5 elementos.
Remova o terceiro elemento usando pop().
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie duas listas.
Use + para criar uma terceira lista.
Depois use extend para modificar a primeira lista.
Explique a diferença nos resultados.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Crie uma lista com 6 elementos.
Remova dois elementos usando del.
Depois limpe toda a lista com clear().
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil
# lista = [1, 2, 3]        # cria lista inicial
# lista.append(4)          # adiciona 4 no final
# print(lista)             # resultado: [1, 2, 3, 4]

# Exercício 2 - Médio
# lista = [10, 20, 30, 40, 50]   # lista inicial
# lista.pop(2)                   # remove índice 2 (valor 30)
# print(lista)                   # resultado: [10, 20, 40, 50]

# Exercício 3 - Difícil
# lista1 = [1, 2, 3]             # primeira lista
# lista2 = [4, 5, 6]             # segunda lista
# lista3 = lista1 + lista2       # nova lista criada
# lista1.extend(lista2)          # modifica lista1
# print(lista3)                  # [1, 2, 3, 4, 5, 6]
# print(lista1)                  # [1, 2, 3, 4, 5, 6]
# Diferença:
# + cria nova lista
# extend altera a original

# Exercício 4 - Difícil
# lista = [1, 2, 3, 4, 5, 6]     # lista inicial
# del lista[1]                   # remove segundo elemento
# del lista[2]                   # remove novo terceiro elemento
# lista.clear()                  # limpa toda lista
# print(lista)                   # resultado: []
