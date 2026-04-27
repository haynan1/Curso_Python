# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')




"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# Desempacotamento com * (Unpacking)

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"O asterisco abre caixas: ele espalha valores onde você quiser."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
📌 O QUE É DESEMPACOTAMENTO?

Desempacotamento (unpacking) é quando você "abre" uma estrutura
(iterável como lista, tupla ou string) e usa seus valores separadamente.

O operador responsável por isso é o * (asterisco).

--------------------------------------------------

📌 EXEMPLO SIMPLES

lista = [1, 2, 3]

print(*lista)

Saída:
1 2 3

Ou seja:
O * tira os elementos de dentro da lista e passa um por um.

--------------------------------------------------

📌 FUNCIONA COM:

✔ Listas
✔ Tuplas
✔ Strings
✔ Qualquer iterável

Exemplo com string:

string = "ABC"
print(*string)

Saída:
A B C

--------------------------------------------------

📌 USO EM FUNÇÕES

A função print aceita vários argumentos separados por vírgula.

Então:

print(*lista)

é equivalente a:

print(1, 2, 3)

--------------------------------------------------

📌 PARÂMETRO sep

sep = separador entre os valores

Exemplo:

print(*lista, sep='-')

Saída:
1-2-3

--------------------------------------------------

📌 CASO DO SEU CÓDIGO

Você tem:

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

E faz:

print(*salas, sep='\n')

O que acontece:

1. O * desempacota a lista principal
2. Cada sublista vira um argumento separado
3. sep='\n' coloca cada argumento em uma nova linha

--------------------------------------------------

📌 RESULTADO FINAL

['Maria', 'Helena']
['Elaine']
['Luiz', 'João', 'Eduarda']

--------------------------------------------------

📌 RESUMO

- * desempacota iteráveis
- Muito usado em print e chamadas de função
- Ajuda a escrever código mais limpo e flexível
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Dada a lista:

dados = ['João', 25, 'Brasil']

Imprima os valores separados por " | " usando desempacotamento.
"""

# dados = ['João', 25, 'Brasil']
# print(*dados, sep=' | ')

"""
Explicação:

- O * desempacota a lista
- O sep define o separador personalizado
- Resultado: João | 25 | Brasil
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Dada a string:

texto = "Python"

Imprima cada letra separada por espaço usando desempacotamento.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Dada a tupla:

numeros = (10, 20, 30, 40)

Imprima os números separados por vírgula usando sep.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Dada a lista:

dados = ['Ana', 'Carlos', 'João']

Imprima cada nome em uma linha diferente usando apenas
desempacotamento e parâmetros do print.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Dada a lista de listas:

grupos = [
    ['A', 'B'],
    ['C', 'D'],
    ['E', 'F']
]

Imprima:

A B
C D
E F

Usando desempacotamento.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil
# texto = "Python"
# print(*texto)

# Exercício 2 - Médio
# numeros = (10, 20, 30, 40)
# print(*numeros, sep=',')

# Exercício 3 - Difícil
# dados = ['Ana', 'Carlos', 'João']
# print(*dados, sep='\n')

# Exercício 4 - Difícil
# grupos = [
#     ['A', 'B'],
#     ['C', 'D'],
#     ['E', 'F']
# ]
# for grupo in grupos:
#     print(*grupo)
