'''
For + Range
range -> range(start, stop, step)
'''

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)





"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# FOR + RANGE EM PYTHON

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
Range cria a sequência.
For percorre a sequência.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Em Python, o comando `range()` é usado para gerar uma sequência de números.

Ele é muito utilizado junto com o laço `for`, que percorre cada elemento
dessa sequência.

A estrutura do range é:

range(início, fim, passo)

Onde:

início (start)
É o número inicial da sequência.

fim (stop)
É o limite final da sequência.
IMPORTANTE: o número final NÃO é incluído.

passo (step)
Define de quanto em quanto a sequência irá aumentar.

Exemplo:

range(0, 100, 8)

Isso significa:

Comece em 0
Vá até antes de 100
Pulando de 8 em 8

A sequência gerada será:

0
8
16
24
32
40
48
56
64
72
80
88
96

O laço `for` é responsável por percorrer essa sequência.

Estrutura:

for variável in sequência:
    ação

Cada vez que o loop roda, a variável recebe o próximo valor da sequência.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um programa que imprima números de 0 até 50 pulando de 5 em 5.
"""

# criando uma sequência usando range
# começa em 0, termina antes de 50, pulando de 5 em 5
# numeros = range(0, 50, 5)

# percorrendo cada número da sequência
# for numero in numeros:

    # exibindo o número atual
    # print(numero)

"""
Explicação do código:

range(0, 50, 5)
gera a sequência:

0, 5, 10, 15, 20, 25, 30, 35, 40, 45

O laço for percorre cada número dessa sequência.

A cada repetição:
- a variável "numero" recebe o próximo valor
- o print mostra esse valor na tela
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie um programa que imprima números de 0 até 20
pulando de 2 em 2 usando range.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie um programa que imprima números de 10 até 100
pulando de 10 em 10.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie um programa que mostre todos os números
de 1 até 50 que sejam múltiplos de 7.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Crie um programa que imprima números de 100 até 0
diminuindo de 10 em 10.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# criando sequência de 0 até 20 pulando de 2
# numeros = range(0, 21, 2)

# percorrendo cada número
# for numero in numeros:

    # exibindo o número
    # print(numero)


# Exercício 2 - Médio

# criando sequência começando em 10 até 100
# pulando de 10 em 10
# numeros = range(10, 101, 10)

# percorrendo a sequência
# for numero in numeros:

    # exibindo o número
    # print(numero)


# Exercício 3 - Difícil

# criando sequência de 1 até 50
# numeros = range(1, 51)

# percorrendo a sequência
# for numero in numeros:

    # verificando se é múltiplo de 7
    # if numero % 7 == 0:

        # exibindo o número
        # print(numero)


# Exercício 4 - Difícil

# criando sequência regressiva
# começa em 100, vai até antes de 0
# diminuindo de 10 em 10
# numeros = range(100, -1, -10)

# percorrendo os números
# for numero in numeros:

    # exibindo o número
    # print(numero)












''' Sobre a variável automática no python - conteúdo bônus'''

"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# Variável de Iteração no Laço FOR em Python

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
No FOR eu não conto sozinho.
O Python caminha pela sequência
e me entrega cada valor.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Quando utilizamos o laço FOR em Python, existe uma variável que recebe
automaticamente cada valor de uma sequência. Essa variável é chamada
de variável de iteração.

Ela é responsável por armazenar temporariamente o valor atual que está
sendo percorrido dentro da sequência.

O FOR percorre estruturas chamadas iteráveis. Exemplos de iteráveis:

- range()
- listas
- strings
- tuplas
- dicionários

Durante cada repetição do laço, o Python pega o próximo elemento da
sequência e atribui automaticamente à variável de iteração.

Estrutura geral do FOR:

for variavel in sequencia:
    bloco_de_codigo

Fluxo mental do funcionamento:

1) Python pega o primeiro elemento da sequência
2) Atribui à variável de iteração
3) Executa o bloco do FOR
4) Pega o próximo elemento
5) Repete até acabar a sequência

Exemplo conceitual:

Sequência:
[10, 20, 30]

Fluxo de execução:

variavel = 10
variavel = 20
variavel = 30

Importante entender:

A variável de iteração NÃO acumula valores.
Ela apenas recebe um valor novo a cada repetição.

Outro ponto importante:

Você não precisa controlar incremento manual como ocorre no WHILE.

No WHILE precisamos fazer:

i = i + 1

No FOR isso não existe, pois o Python controla o avanço na sequência.

Comparação mental:

WHILE → você controla o contador
FOR → o Python percorre a sequência

Exemplo clássico com range:

range(5)

Gera os números:

0, 1, 2, 3, 4

O FOR então faz algo equivalente a:

numero = 0
numero = 1
numero = 2
numero = 3
numero = 4

Mas isso acontece automaticamente.

Por isso dizemos que a variável do FOR é uma
"variável automática de iteração".
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um laço FOR que percorra os números de 1 até 5
e mostre cada número na tela.

Utilize a função range().
"""

# Cria um laço FOR
# A variável "numero" será a variável de iteração
# O range(1,6) gera os valores: 1,2,3,4,5
# A cada repetição o Python atribui um desses valores a "numero"

# for numero in range(1,6):
#     print(numero)

"""
Explicação do código resolvido.

range(1,6) cria uma sequência que começa em 1 e termina em 5.

Fluxo interno:

numero = 1
numero = 2
numero = 3
numero = 4
numero = 5

A cada passo o Python executa o bloco do FOR,
mostrando o valor atual da variável de iteração.

Perceba que não precisamos fazer incremento manual
como aconteceria em um WHILE.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie um laço FOR que mostre os números de 0 até 4
utilizando a função range().
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie um laço FOR que percorra a lista abaixo
e mostre cada fruta na tela.

lista = ["maçã", "banana", "laranja", "uva"]
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie um laço FOR que mostre apenas os números pares
entre 0 e 10 utilizando range().
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Crie um laço FOR que percorra a string abaixo
e mostre cada letra separadamente.

palavra = "PYTHON"
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# Cria o laço FOR
# A variável "numero" receberá automaticamente
# os valores gerados por range(5)
# range(5) gera: 0,1,2,3,4

# for numero in range(5):
#     print(numero)


# Exercício 2 - Médio

# Cria a lista de frutas
# lista = ["maçã", "banana", "laranja", "uva"]

# O FOR percorre cada elemento da lista
# A variável "fruta" recebe cada item da lista
# automaticamente a cada repetição

# for fruta in lista:
#     print(fruta)


# Exercício 3 - Difícil

# range(0,11,2) começa em 0
# vai até 10
# avançando de 2 em 2

# Isso gera:
# 0,2,4,6,8,10

# for numero in range(0,11,2):
#     print(numero)


# Exercício 4 - Difícil

# Strings também são iteráveis
# O FOR percorre cada caractere da palavra

# palavra = "PYTHON"

# A variável "letra" recebe
# cada caractere da string

# for letra in palavra:
#     print(letra)
