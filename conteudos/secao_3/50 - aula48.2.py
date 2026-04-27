"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)



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
Lista é mutável: posso mudar sem criar outra igual.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Listas em Python são estruturas de dados MUTÁVEIS, ou seja,
você pode alterar seus valores após a criação.

Principais características:
- Permitem armazenar vários valores
- Aceitam tipos diferentes (int, str, float, etc.)
- São indexadas (cada item tem uma posição)
- Suportam fatiamento (slice)

Exemplo de índice:
lista = [10, 20, 30, 40]
          0   1   2   3

Principais operações (CRUD):

CREATE (Criar):
- append(valor) → adiciona no final
- insert(posição, valor) → adiciona em posição específica
- extend(lista) → adiciona vários valores

READ (Ler):
- lista[i] → acessa elemento pelo índice

UPDATE (Atualizar):
- lista[i] = novo_valor → altera valor

DELETE (Apagar):
- pop() → remove último ou por índice
- del lista[i] → remove pelo índice
- clear() → limpa toda a lista

Sobre o método pop():
- pop() → remove o último elemento
- pop(indice) → remove o elemento do índice informado
- Retorna o valor removido (isso é MUITO importante)

Agora vamos analisar o código enviado.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Dado o código abaixo, explique o resultado final da lista e o valor removido:

lista = [10, 20, 30, 40]

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)

print(lista, 'Removido,', ultimo_valor)
"""

# Código resolvido totalmente comentado

# lista inicial
# lista = [10, 20, 30, 40]

# adiciona 50 no final
# lista = [10, 20, 30, 40, 50]

# remove o último valor (50)
# lista = [10, 20, 30, 40]

# adiciona 60 no final
# lista = [10, 20, 30, 40, 60]

# adiciona 70 no final
# lista = [10, 20, 30, 40, 60, 70]

# remove o índice 3 (valor 40)
# lista = [10, 20, 30, 60, 70]
# ultimo_valor = 40

# saída final:
# [10, 20, 30, 60, 70] Removido, 40

"""
Explicação do código resolvido:

1. Começamos com a lista [10, 20, 30, 40]
2. append(50) adiciona no final
3. pop() remove o último (50)
4. append(60) e append(70) adicionam novos valores
5. pop(3) remove o elemento da posição 3 (que é 40)
6. O valor removido é armazenado em "ultimo_valor"

Resultado final:
Lista → [10, 20, 30, 60, 70]
Removido → 40
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie uma lista com os valores [1, 2, 3].

Adicione o número 4 no final.

Mostre a lista final.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie uma lista [10, 20, 30, 40].

Remova o número 20 usando índice.

Mostre a lista final.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie uma lista [5, 10, 15, 20, 25].

Remova o elemento do índice 2 usando pop()
e guarde em uma variável.

Mostre:
- A lista final
- O valor removido
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Crie uma lista vazia.

Adicione os números 1 até 5 usando append.

Depois:
- Remova o primeiro elemento
- Remova o último elemento

Mostre a lista final.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil
# lista = [1, 2, 3]              # cria lista
# lista.append(4)               # adiciona 4
# print(lista)                  # [1, 2, 3, 4]

# Exercício 2 - Médio
# lista = [10, 20, 30, 40]      # cria lista
# del lista[1]                  # remove índice 1 (20)
# print(lista)                  # [10, 30, 40]

# Exercício 3 - Difícil
# lista = [5, 10, 15, 20, 25]   # cria lista
# removido = lista.pop(2)       # remove índice 2 (15)
# print(lista)                  # [5, 10, 20, 25]
# print(removido)               # 15

# Exercício 4 - Difícil
# lista = []                    # lista vazia
# lista.append(1)               # adiciona 1
# lista.append(2)               # adiciona 2
# lista.append(3)               # adiciona 3
# lista.append(4)               # adiciona 4
# lista.append(5)               # adiciona 5
# del lista[0]                  # remove primeiro elemento (1)
# lista.pop()                   # remove último elemento (5)
# print(lista)                  # [2, 3, 4]
