'''
senha_salva = '123'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print("Aquele laço acima pode ter repetições infinitas.")

'''
'''Outra forma de trabalhar com repetições'''




texto = "Python"
novo_texto = ""

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')







"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# WHILE E FOR EM PYTHON (LAÇOS DE REPETIÇÃO)

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
WHILE pergunta: "Ainda precisa repetir?"

FOR pergunta: "Quantos elementos existem para percorrer?"
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Em programação, muitas vezes precisamos repetir uma ação várias vezes.
Para isso utilizamos estruturas chamadas LAÇOS DE REPETIÇÃO.

As duas mais comuns em Python são:

1) WHILE
2) FOR


----------------------------------------
WHILE
----------------------------------------

O WHILE executa um bloco de código ENQUANTO uma condição for verdadeira.

Estrutura:

while condição:
    código


Exemplo conceitual:

while senha_errada:
    pedir_senha()

Ou seja:

"Enquanto a senha digitada for diferente da senha correta, continue pedindo."

Isso cria um LOOP.

Se a condição nunca se tornar falsa, o loop será infinito.


----------------------------------------
EXEMPLO DO SEU CÓDIGO (WHILE)
----------------------------------------

senha_salva = '123'
senha_digitada = ''
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(...)
    repeticoes += 1

O que acontece:

1) A senha correta é "123".
2) Enquanto a senha digitada for diferente da salva...
3) O programa continua pedindo a senha.
4) Um contador registra quantas tentativas foram feitas.


----------------------------------------
FOR
----------------------------------------

O FOR é usado para percorrer elementos de uma sequência.

Sequências comuns:

- Strings
- Listas
- Tuplas
- Range


Exemplo:

for letra in "Python":
    print(letra)


O Python pega cada caractere da palavra "Python"
e executa o código para cada um.


----------------------------------------
EXEMPLO DO SEU CÓDIGO (FOR)
----------------------------------------

texto = "Python"
novo_texto = ""

for letra in texto:
    novo_texto += f'*{letra}'

Resultado final:

*P*y*t*h*o*n*

Cada letra recebe um "*" antes dela.


----------------------------------------
RESUMO

WHILE
→ usado quando não sabemos quantas repetições serão necessárias.

FOR
→ usado quando sabemos que vamos percorrer elementos de algo.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um programa que percorra a palavra "CODE"
e monte uma nova palavra colocando "-" antes de cada letra.

Saída esperada:

-C-O-D-E-
"""

# palavra original
# texto = "CODE"

# variável que armazenará o novo texto
# novo_texto = ""

# loop percorrendo cada letra
# for letra in texto:

# adiciona "-" antes da letra
# novo_texto += f"-{letra}"

# após o loop adicionamos o último "-"
# novo_texto += "-"

# mostramos o resultado
# print(novo_texto)


"""
Explicação do código resolvido.

1) Criamos uma variável chamada texto contendo "CODE".

2) Criamos uma variável vazia chamada novo_texto.

3) O FOR percorre cada letra da palavra.

4) A cada repetição adicionamos "-letra".

5) No final adicionamos o último "-".

6) O resultado final é:

-C-O-D-E-
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Percorra a palavra "JAVA" usando um FOR
e imprima cada letra em uma linha.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie um programa que percorra a palavra "Python"
e construa uma nova string colocando "#" antes de cada letra.

Saída esperada:

#P#y#t#h#o#n#
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie um sistema de senha usando WHILE.

A senha correta é: "python123"

Enquanto o usuário errar a senha,
o programa deve continuar pedindo novamente.

No final mostre quantas tentativas foram feitas.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Percorra a palavra "PROGRAMAR"
e construa uma nova string colocando "*" antes
e depois de cada letra.

Saída esperada:

*P**R**O**G**R**A**M**A**R*
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# palavra a ser percorrida
# texto = "JAVA"

# percorre cada letra
# for letra in texto:

# imprime a letra
# print(letra)



# Exercício 2 - Médio

# texto original
# texto = "Python"

# variável que armazenará o novo texto
# novo_texto = ""

# percorre cada letra
# for letra in texto:

# adiciona "#" antes da letra
# novo_texto += f"#{letra}"

# adiciona o último "#"
# novo_texto += "#"

# mostra resultado
# print(novo_texto)



# Exercício 3 - Difícil

# senha correta
# senha_salva = "python123"

# senha digitada começa vazia
# senha_digitada = ""

# contador de tentativas
# tentativas = 0

# enquanto a senha digitada for diferente da correta
# while senha_digitada != senha_salva:

# pede a senha ao usuário
# senha_digitada = input("Digite a senha: ")

# aumenta o contador
# tentativas += 1

# quando sair do loop significa que acertou
# print("Senha correta!")

# mostra quantas tentativas foram feitas
# print("Tentativas:", tentativas)



# Exercício 4 - Difícil

# palavra original
# texto = "PROGRAMAR"

# variável que guardará o resultado
# novo_texto = ""

# percorre cada letra
# for letra in texto:

# adiciona "*" antes e depois da letra
# novo_texto += f"*{letra}*"

# mostra o resultado
# print(novo_texto)
