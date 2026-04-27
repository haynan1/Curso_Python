"""
Introdução ao empacotamento e desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)



'''Teste meu'''

print('\n', 10 * '---')

nomes = nome1, nome2, nome3 = ['Maria', 'Haynan', 'Gabrielly']

print(nomes)
print(nome2)




"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# Empacotamento e Desempacotamento de Listas

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Desempacotar é distribuir, * é guardar o resto."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Em Python, podemos "desempacotar" uma lista diretamente em variáveis.

Exemplo geral:

a, b, c = [1, 2, 3]

Cada variável recebe um valor da lista, na ordem.

Agora entra um conceito muito importante:

O operador * (asterisco)

Ele serve para capturar o "resto" dos elementos.

Exemplo:

a, *resto = [1, 2, 3, 4]

- a recebe 1
- resto recebe [2, 3, 4]

No seu caso:

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']

Vamos analisar:

- _ ignora 'Maria'
- _ ignora 'Helena'
- nome recebe 'Luiz'
- *resto recebe o que sobrar → nesse caso, nada → []

IMPORTANTE:

O "_" (underscore) é uma convenção para dizer:
"esse valor existe, mas eu não vou usar".

Saída do código:
Luiz
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Dada uma lista com 4 nomes, capture:

- Ignore os dois primeiros
- Guarde o terceiro em uma variável
- Guarde o restante em outra variável
"""

# lista de nomes
# lista = ['Ana', 'Bruno', 'Carlos', 'Diana']

# ignorando os dois primeiros, pegando o terceiro e o resto
# _, _, terceiro, *resto = lista

# exibindo os resultados
# print(terceiro)
# print(resto)

"""
Explicação do código resolvido:

- "_" ignora valores que não queremos usar.
- "terceiro" recebe o terceiro elemento da lista.
- "*resto" captura tudo que sobra após o terceiro elemento.
- Mesmo que sobre apenas um item, ele ainda será uma lista.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Dada a lista:

['A', 'B', 'C']

Capture:
- A primeira letra em uma variável
- O restante usando *
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Dada a lista:

[10, 20, 30, 40]

Capture:
- Ignore o primeiro valor
- Guarde o segundo
- Guarde o restante com *
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Dada a lista:

['Python', 'Java', 'C', 'JavaScript', 'Go']

Capture:
- O primeiro em uma variável
- O último em outra
- O restante no meio com *
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Dada a lista:

[1, 2, 3, 4, 5, 6]

Capture:
- Ignore o primeiro e o último
- Guarde todos os valores do meio usando *
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# lista = ['A', 'B', 'C']
# primeira, *resto = lista
# print(primeira)
# print(resto)

# Exercício 2 - Médio

# lista = [10, 20, 30, 40]
# _, segundo, *resto = lista
# print(segundo)
# print(resto)

# Exercício 3 - Difícil

# lista = ['Python', 'Java', 'C', 'JavaScript', 'Go']
# primeiro, *meio, ultimo = lista
# print(primeiro)
# print(meio)
# print(ultimo)

# Exercício 4 - Difícil

# lista = [1, 2, 3, 4, 5, 6]
# _, *meio, _ = lista
# print(meio)
