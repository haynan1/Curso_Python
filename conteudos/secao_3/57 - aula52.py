"""
Tipo tupla - Uma lista imutável
"""

nomes = 'Maria', 'Helena', 'Luiz'
#Pode ser sem os parenteses também. para estar formando uma Tupla.


nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)






"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# Tuplas em Python (Listas Imutáveis)

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Lista muda, tupla nunca."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
A tupla é muito parecida com a lista, porém com uma diferença fundamental:

👉 Ela é IMUTÁVEL

Ou seja:
- Você NÃO pode alterar
- NÃO pode adicionar
- NÃO pode remover elementos

Exemplo de tupla:
nomes = ('Maria', 'Helena', 'Luiz')

Diferença visual:
- Lista → usa []
- Tupla → usa ()

----------------------------------------

ACESSANDO ELEMENTOS

Assim como listas, usamos índices:

nomes[0] → 'Maria'
nomes[1] → 'Helena'
nomes[2] → 'Luiz'

Também podemos usar índices negativos:

nomes[-1] → último elemento → 'Luiz'

----------------------------------------

CONVERSÕES

Você pode converter entre lista e tupla:

tuple(lista) → transforma em tupla
list(tupla) → transforma em lista

Isso é útil quando você precisa modificar algo:

1) Converte para lista
2) Faz alterações
3) Converte de volta para tupla

----------------------------------------

SEU CÓDIGO

nomes = ('Maria', 'Helena', 'Luiz')

print(nomes[-1]) → Luiz
print(nomes) → ('Maria', 'Helena', 'Luiz')

----------------------------------------

QUANDO USAR TUPLAS?

- Quando os dados NÃO devem mudar
- Para maior segurança
- Para representar dados fixos (ex: coordenadas, dias da semana)

Tuplas são mais leves e rápidas que listas em alguns casos.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie uma tupla com 4 números.

Exiba:
- O primeiro elemento
- O último elemento
"""

# criando a tupla
# numeros = (10, 20, 30, 40)

# acessando o primeiro elemento
# primeiro = numeros[0]

# acessando o último elemento
# ultimo = numeros[-1]

# exibindo os resultados
# print(primeiro)
# print(ultimo)

"""
Explicação do código resolvido:

- Tuplas usam ()
- Índice 0 → primeiro elemento
- Índice -1 → último elemento
- Não é possível alterar os valores depois de criada
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie uma tupla com 3 cores.

Exiba a cor do meio.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie uma tupla com 5 números.

Exiba:
- O segundo número
- O penúltimo número
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie uma tupla com nomes.

Converta essa tupla para lista,
adicione um novo nome,
e depois converta de volta para tupla.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Crie uma tupla com 4 números.

Percorra a tupla e exiba:
índice + valor
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# cores = ('vermelho', 'azul', 'verde')
# print(cores[1])

# Exercício 2 - Médio

# numeros = (1, 2, 3, 4, 5)
# print(numeros[1])
# print(numeros[-2])

# Exercício 3 - Difícil

# nomes = ('Ana', 'Bruno', 'Carlos')
# lista = list(nomes)
# lista.append('Diana')
# nomes = tuple(lista)
# print(nomes)

# Exercício 4 - Difícil

# numeros = (10, 20, 30, 40)
# for i in range(len(numeros)):
    # print(i, numeros[i])
    