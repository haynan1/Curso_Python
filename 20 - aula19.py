'''
Operadores de comparação (relacionais)
OP      significado         exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       Menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
'''
#Sempre que usar os comparadores vai ter um resultado boolean: False ou True.

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(maior)



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# OPERADORES DE COMPARAÇÃO (RELACIONAIS)
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
Comparou? Virou True ou False.
Relacional sempre responde boolean.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Operadores de comparação são usados para comparar valores.

Eles sempre retornam um valor booleano:
True  → Verdadeiro
False → Falso

Lista dos operadores:

>   maior que
>=  maior ou igual
<   menor que
<=  menor ou igual
==  igual
!=  diferente

Exemplos práticos:

2 > 1       → True
2 >= 2      → True
1 < 2       → True
2 <= 2      → True
'a' == 'a'  → True
'a' != 'b'  → True

Sempre que usamos um operador relacional,
o resultado será avaliado como True ou False.

Esse resultado pode ser:
- Guardado em uma variável
- Usado dentro de um if
- Usado em expressões lógicas (and / or)

No arquivo enviado, cada comparação foi armazenada
em uma variável:

maior = 2 > 1
menor = 1 < 2

Isso significa que as variáveis agora armazenam
valores booleanos.

Ou seja:
Não estamos guardando o cálculo.
Estamos guardando o resultado da comparação.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie duas variáveis:

numero1 = 10
numero2 = 20

Faça as seguintes comparações:
- numero1 é maior que numero2?
- numero1 é menor que numero2?
- numero1 é igual a numero2?

Armazene cada resultado em uma variável.
"""

# numero1 = 10
# numero2 = 20

# resultado_maior = numero1 > numero2
# resultado_menor = numero1 < numero2
# resultado_igual = numero1 == numero2

# print(resultado_maior)
# print(resultado_menor)
# print(resultado_igual)

"""
Explicação:

numero1 > numero2 → 10 > 20 → False
numero1 < numero2 → 10 < 20 → True
numero1 == numero2 → 10 == 20 → False

Cada comparação retorna um valor booleano.
Esses valores podem ser reutilizados depois.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie duas variáveis:

a = 5
b = 5

Verifique:
- a é igual a b?
- a é diferente de b?

Armazene os resultados em variáveis.
"""

a = 5 
b = 5

if a == b:
    print("A é igual a B, muito bem !")
else:
    print('Diferente !')

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie uma variável idade = 18.

Verifique:
- idade é maior que 16?
- idade é maior ou igual a 18?
- idade é menor que 21?

Armazene os resultados.
"""

idade = 18

# idade = int(input('Digite sua idade:'))

if idade > 16:
    print(f'Esse número é maior de que 16: {idade}')

if idade >= 18:
    print('Você é maior de idade.')

if idade < 21:
    print(f'Idade menor que 21, sendo igual a {idade}')
else:
    print('Esse número é maior de 21.')


'''Outra forma'''

print(5 * '----')
print('Outra dorma de fazer')
print(5 * '----')

idade = 18

maior_que_16 = idade > 16
maior_ou_igual_a_18 = idade >= 18
menor_de_21 = idade < 21

print(maior_ou_igual_a_18, maior_que_16, menor_de_21)

'''Dessa forma verificamos a condicional'''

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie duas variáveis:

usuario = "admin"
senha = "1234"

Verifique:
- usuario é igual a "admin"?
- senha é diferente de "0000"?
- usuario é diferente de "guest"?

Armazene os resultados.
"""

usuario = 'admin'
senha = '1234'

if usuario == 'admin':
    print(f'Sim, o usuário é igual a admin')

if senha != '0000':
    print('Sim, a senha é diferente de 0000')

if usuario != 'guest':
    print('Sim, é diferente !')


verificacao_de_admin = 'admin' == 'admin'
verificacao_de_numero = '1234' != '0000'
verificacao_de_usuario = 'admin' != 'guest'

print(verificacao_de_admin,verificacao_de_numero,verificacao_de_usuario)

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Crie duas variáveis:

x = 15
y = 10

Crie uma variável chamada comparacao_final
que armazene o resultado da comparação:

x >= y

Depois crie outra chamada comparacao_dupla
que armazene:

x <= y
"""

x = 15
y = 10

comparacao_final = x >= y
comparacao_dupla = x <= y

print(comparacao_final,comparacao_dupla)

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# a = 5
# b = 5

# igual = a == b
# diferente = a != b


# Exercício 2 - Médio

# idade = 18

# maior_que_16 = idade > 16
# maior_ou_igual_18 = idade >= 18
# menor_que_21 = idade < 21

# print(maior_que_16,maior_ou_igual_18,menor_que_21)

# Exercício 3 - Difícil

# usuario = "admin"
# senha = "1234"

# usuario_correto = usuario == "admin"
# senha_diferente = senha != "0000"
# usuario_nao_guest = usuario != "guest"


# Exercício 4 - Difícil

# x = 15
# y = 10

# comparacao_final = x >= y
# comparacao_dupla = x <= y