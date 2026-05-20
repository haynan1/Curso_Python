'''
Iterável -> str, range, etc (__inter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
'''
# texto = iter('Haynan') #__iter__()
# print(next(texto)) #__next__()


'''For letra in texto'''

texto = 'Haynan' #Iterável
iteratador = iter(texto) #Iterador

while True:
    try:
        print(next(iteratador))
    except StopIteration:
        break



'''Outra forma'''



for letra in texto:
    print(letra)



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# ITERÁVEIS E ITERADORES EM PYTHON
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
Iterável é a coleção.
Iterador é quem faz a entrega.
next pega o próximo.
iter cria o entregador.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Vamos entender de forma simples:

🔹 ITERÁVEL
É qualquer objeto que pode ser percorrido.
Exemplos: string, lista, tupla, range...

Exemplo:
texto = "Haynan"

Aqui, "texto" é ITERÁVEL porque podemos percorrer letra por letra.

---

🔹 ITERADOR
É o objeto que sabe como percorrer o iterável.
Ele entrega UM valor por vez.

Criamos um iterador com:
iter(iterável)

Exemplo:
iterador = iter(texto)

---

🔹 next()
Serve para pegar o próximo valor do iterador.

Exemplo:
next(iterador)

Ele vai retornando letra por letra.

---

🔹 StopIteration
Quando os valores acabam, o Python lança esse erro.

Por isso usamos try/except.

---

🔹 FOR por trás dos panos

O for faz EXATAMENTE isso:

1. Cria um iterador
2. Chama next()
3. Para quando dá StopIteration

Ou seja:
for letra in texto:

é equivalente ao while com next()

---

Resumo mental:

for = automático
while + next = manual
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um código que percorre a palavra "Python" usando iterador manual (while + next)
e imprime cada letra.
"""

# Criando a string (iterável)
# texto = "Python"

# Criando o iterador
# iterador = iter(texto)

# Loop infinito
# while True:
#     try:
#         # Pega a próxima letra
#         letra = next(iterador)
#         
#         # Mostra a letra
#         print(letra)
#     
#     except StopIteration:
#         # Quando acabar, para o loop
#         break

"""
Explicação:

1. Criamos o iterador com iter()
2. Usamos next() para pegar cada letra
3. Quando não há mais letras, ocorre StopIteration
4. Usamos except para encerrar o loop

Isso simula exatamente o funcionamento do for.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie um iterador manual para a palavra "ABC"
e imprima cada letra usando next().
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie um iterador para uma lista [10, 20, 30]
e imprima os valores usando while + next.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Sem usar for, percorra um range de 0 até 5
usando iterador manual.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Crie um código que conta quantos elementos existem
em uma string usando apenas iterador manual (sem len e sem for).
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# texto = "ABC"                      # Criando a string
# iterador = iter(texto)            # Criando o iterador
# while True:                       # Loop infinito
#     try:
#         print(next(iterador))     # Imprime próxima letra
#     except StopIteration:         # Quando acabar
#         break                     # Para o loop

# Exercício 2 - Médio

# lista = [10, 20, 30]              # Lista iterável
# iterador = iter(lista)            # Criando iterador
# while True:
#     try:
#         print(next(iterador))     # Mostra próximo valor
#     except StopIteration:
#         break

# Exercício 3 - Difícil

# numeros = range(6)                # Range de 0 a 5
# iterador = iter(numeros)          # Criando iterador
# while True:
#     try:
#         print(next(iterador))     # Mostra número
#     except StopIteration:
#         break

# Exercício 4 - Difícil

# texto = "Haynan"                  # String
# iterador = iter(texto)            # Criando iterador
# contador = 0                      # Inicializando contador
# while True:
#     try:
#         next(iterador)            # Apenas consome o valor
#         contador += 1             # Conta +1
#     except StopIteration:
#         break
# print(contador)                   # Mostra total de caracteres
