"""
DocString
Python = linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""

print(1234)

#Aspas simples
print('Haynan Kerlin')
print(1, 'Haynan "Kerlin"')

#Aspas duplas
print("Haynan Kerlin")
print(2, "Haynan 'Kerlin'")

#Escape = ela anula o proximo caracter na leitura do python.
print("Haynan \"Kerlin")

#r
print(r"Haynan \"Kerlin\"")



'''
========================================
MATERIAL DE SUPORTE - JAMES IA ↓↓↓
========================================
'''

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# STRINGS, ASPAS E ESCAPE NO PYTHON

# ========================================
# FRASE MNEMÔNICA
# ========================================

'''
Strings são textos entre aspas, e a barra invertida (\\) pode mudar a leitura do Python.
'''

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

'''
Em Python, usamos o tipo STR (string) para representar textos.

Uma STRING é qualquer sequência de caracteres que esteja entre aspas.

Existem três formas principais de escrever strings:

1 - Aspas simples
'Texto aqui'

2 - Aspas duplas
"Texto aqui"

3 - Aspas triplas (usadas mais para textos grandes ou DocStrings)
"""Texto"""
ou
''' + "'''Texto'''" + '''

Python permite usar aspas simples ou duplas para facilitar quando
precisamos colocar aspas dentro do texto.

Exemplo lógico:

Se o texto tem aspas duplas dentro, podemos usar aspas simples fora.

'Ele disse "Olá"'

Ou o contrário:

"Ele disse 'Olá'"

---

ESCAPE (\\)

A barra invertida é chamada de ESCAPE.

Ela diz para o Python:

"Ignore o significado especial do próximo caractere."

Exemplo:

\\"  -> permite usar aspas duplas dentro de aspas duplas
\\'  -> permite usar aspas simples dentro de aspas simples

Exemplo lógico:

"Haynan \\"Kerlin\\""

Sem o escape o Python entenderia que a string terminou.

---

STRING RAW (r)

Quando colocamos a letra r antes da string:

r"texto"

O Python NÃO interpreta caracteres especiais.

Ou seja:

\\ continua sendo apenas \\

Exemplo:

r"Haynan \\"Kerlin\\""

Nesse caso o Python mostra exatamente os caracteres.

---

TIPAGEM DO PYTHON

Python possui tipagem:

• DINÂMICA → você não precisa declarar o tipo da variável
• FORTE → Python não mistura tipos automaticamente

Exemplo:

texto = "Olá"
numero = 10

Cada variável guarda um tipo diferente.

---

RESUMO

String = texto
Aspas = delimitam a string
Escape (\\) = altera interpretação
r = string literal (raw string)
'''

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

'''
Crie prints que mostrem:

1) Seu nome usando aspas simples
2) Seu nome usando aspas duplas
3) Um texto contendo aspas dentro
4) Um exemplo usando escape
5) Um exemplo usando raw string
'''

# Exibe um número
# print(1234)

# Exibe uma string usando aspas simples
# print('Haynan Kerlin')

# Exibe número e texto juntos
# print(1, 'Haynan "Kerlin"')

# Exibe string usando aspas duplas
# print("Haynan Kerlin")

# Exibe aspas simples dentro de aspas duplas
# print(2, "Haynan 'Kerlin'")

# Exemplo usando escape para permitir aspas dentro da string
# print("Haynan \"Kerlin\"")

# Exemplo usando RAW STRING
# print(r"Haynan \"Kerlin\"")

'''
Explicação do código resolvido:

print() é uma função usada para mostrar informações na tela.

No primeiro exemplo mostramos um número.

Depois mostramos textos (strings) usando aspas simples e aspas duplas.

Quando queremos colocar aspas dentro de uma string
podemos usar:

• aspas diferentes
ou
• escape (\\)

No último exemplo usamos r antes da string,
o que faz o Python ignorar interpretações especiais.
'''

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

'''
Exercício 1 - Fácil

Crie três prints:

1) Um print com seu nome
2) Um print com sua idade
3) Um print com a frase:

Meu nome é "SEU NOME"
'''

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

'''
Exercício 2 - Médio

Mostre a frase abaixo utilizando escape:

Python é uma linguagem "poderosa"
'''

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

'''
Exercício 3 - Difícil

Crie um print que mostre exatamente:

C:\\Users\\Aluno\\Python

Utilize RAW STRING.
'''

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

'''
Exercício 4 - Difícil

Mostre na tela a frase:

Ele disse: "Python é incrível!"

Use apenas aspas duplas e utilize ESCAPE.
'''

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# print('Seu Nome')
# print(20)
# print('Meu nome é "Seu Nome"')

# Exercício 2 - Médio

# print("Python é uma linguagem \"poderosa\"")

# Exercício 3 - Difícil

# print(r"C:\\Users\\Aluno\\Python")

# Exercício 4 - Difícil

# print("Ele disse: \"Python é incrível!\"")
