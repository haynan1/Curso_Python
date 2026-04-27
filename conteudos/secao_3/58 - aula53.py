"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# enumerate() - Índice + Valor ao mesmo tempo

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"enumerate junta índice e valor num só passo."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
O enumerate() é uma função do Python usada para percorrer iteráveis
(como listas, tuplas, strings), retornando:

👉 índice + valor ao mesmo tempo

Estrutura:

for indice, valor in enumerate(lista):
    ...

Cada item gerado pelo enumerate é uma tupla:

(indice, valor)

----------------------------------------

SEU CÓDIGO

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

Resultado interno do enumerate(lista):

[(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]

----------------------------------------

FORMA MAIS COMUM (DESEMPACOTANDO)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

Aqui:
- indice → posição
- nome → valor da lista
- lista[indice] → mesma coisa que nome

Ou seja:
nome == lista[indice]

----------------------------------------

FORMA 2 (SEM DESEMPACOTAR)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

Aqui você recebe a tupla inteira e depois separa.

----------------------------------------

FORMA 3 (LOOP DENTRO DA TUPLA)

for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(valor)

Aqui você percorre cada tupla (índice e valor separadamente).

----------------------------------------

VANTAGEM DO enumerate()

Evita usar:
range(len(lista))

Deixa o código:
- Mais limpo
- Mais legível
- Mais "Pythonico"

----------------------------------------

EXTRA

Você pode começar de outro número:

enumerate(lista, start=1)

Isso faria começar do índice 1 ao invés de 0.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Dada uma lista de frutas, exiba:
índice + fruta usando enumerate()
"""

# lista de frutas
# frutas = ['Maçã', 'Banana', 'Uva']

# percorrendo com enumerate
# for indice, fruta in enumerate(frutas):
    # exibindo índice e valor
    # print(indice, fruta)

"""
Explicação do código resolvido:

- enumerate(frutas) gera (0, 'Maçã'), (1, 'Banana'), (2, 'Uva')
- O for já desempacota automaticamente
- Não precisamos usar range nem len
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie uma lista com 3 cores.

Use enumerate para exibir:
índice + cor
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie uma lista com 4 números.

Use enumerate para exibir:
índice + número + número ao quadrado
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie uma lista com nomes.

Exiba apenas os nomes que estão em índices ímpares
usando enumerate.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Crie uma lista com 5 números.

Use enumerate(start=1) para exibir:
posição + número + "PAR" ou "ÍMPAR"
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# cores = ['Vermelho', 'Azul', 'Verde']
# for i, cor in enumerate(cores):
    # print(i, cor)

# Exercício 2 - Médio

# numeros = [2, 4, 6, 8]
# for i, num in enumerate(numeros):
    # quadrado = num ** 2
    # print(i, num, quadrado)

# Exercício 3 - Difícil

# nomes = ['Ana', 'Bruno', 'Carlos', 'Diana']
# for i, nome in enumerate(nomes):
    # if i % 2 != 0:
        # print(i, nome)

# Exercício 4 - Difícil

# numeros = [1, 2, 3, 4, 5]
# for i, num in enumerate(numeros, start=1):
    # if num % 2 == 0:
        # tipo = "PAR"
    # else:
        # tipo = "ÍMPAR"
    # print(i, num, tipo)
    