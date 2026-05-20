'''
Operadores Lógicos
and (e) or (ou) not (não)

============Focando em and=======================
and - Todas as condições precisam ser veradeiras.
Se qualquer valor for considerado Falso, a expressão 
inteira será avaliada naquele valor
São considerados falsy (que você já viu)
0 0.0 '' False
Também existe o tipo None que é
usado para representar um não valor
==================================================
'''


# Sistema de exemplificação.

entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"
#if True:
# ...
if entrada == "E" and senha_digitada == senha_permitida:
    print("Sua entrada foi efetuada com sucesso !")
else:
    print("Sair")



#Avaliação de curto circuito.
print(True and False and True)
print(True and 0 and True)
print(bool('')) # Uma string vazia é tratada como False


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# OPERADORES LÓGICOS - FOCO NO AND
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
AND é exigente:
Se UM falhar, tudo para.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Operadores Lógicos são usados para combinar condições.

Os principais operadores são:

and  -> e
or   -> ou
not  -> não

Hoje o foco é no operador AND.

==================================================
COMO O AND FUNCIONA?
==================================================

O operador AND exige que TODAS as condições sejam verdadeiras.

Exemplo simples:

True and True   -> True
True and False  -> False
False and True  -> False
False and False -> False

Ou seja:

Se qualquer parte da expressão for falsa,
o resultado inteiro será falso.

==================================================
FALSY (Valores considerados falsos)
==================================================

No Python, alguns valores são considerados False
mesmo que não sejam o tipo bool.

São chamados de FALSY:

0
0.0
'' (string vazia)
False
None

Qualquer outro valor normalmente é considerado True.

==================================================
AVALIAÇÃO DE CURTO-CIRCUITO
==================================================

O AND funciona com algo chamado "curto-circuito".

Ele avalia da esquerda para a direita.
Se encontrar um valor falso, ele para ali mesmo.

Exemplo:

True and 0 and True

O Python avalia:

True -> continua
0 -> é FALSO
Ele PARA aqui.

O resultado final será 0.

IMPORTANTE:
O AND não retorna necessariamente True ou False.
Ele retorna o valor que interrompe a expressão
ou o último valor se todos forem verdadeiros.

Exemplos:

True and True and 5   -> retorna 5
True and 0 and 10     -> retorna 0
True and '' and 10    -> retorna ''

Isso é muito importante para entender validações.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Sistema simples de login usando AND.

O usuário deve digitar:
[E] para entrar
A senha correta: 123456

Se as duas condições forem verdadeiras,
a entrada será permitida.
"""

# Solicita ao usuário que digite E ou S
# entrada = input("[E]ntrar [S]air: ")

# Solicita a senha
# senha_digitada = input("Senha: ")

# Define a senha correta
# senha_permitida = "123456"

# Verifica se:
# 1) O usuário digitou "E"
# 2) A senha digitada é igual à senha permitida
# if entrada == "E" and senha_digitada == senha_permitida:
#     print("Sua entrada foi efetuada com sucesso!")
# else:
#     print("Sair")

"""
EXPLICAÇÃO:

entrada == "E"
Verifica se o usuário quer entrar.

senha_digitada == senha_permitida
Verifica se a senha está correta.

O AND exige que as DUAS condições sejam verdadeiras.

Se qualquer uma falhar:
- digitou S
- digitou senha errada

O acesso será negado.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie um programa que:

Peça um número ao usuário.
Se o número for maior que 10
E menor que 20,
mostre: "Número válido".

Caso contrário, mostre:
"Número inválido".
"""

numero = input('Digite um número: ')

try:
    numero_valido = int(numero)
    if numero_valido > 10 and numero_valido < 20:
        print(f'Número válido, o seu número é {numero}')
    else:
        print('Número invalido.')
except ValueError:
    print('Esse dado enviado não é valido, tente novamente !')


# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Peça ao usuário:

Idade
Possui carteira de motorista? (S/N)

Permita dirigir apenas se:
Idade >= 18
E possuir carteira igual a "S"

Caso contrário, mostre:
"Não pode dirigir".
"""

print(10 * '===')

idade = input('Digite sua idade: ')
cnh = input('Possui carteira de motorista?(S/N): ')


try:
    idade_int = int(idade)
    if idade_int >= 18 and cnh == 'S':
        print('Seja bem vindo a empresa, vocẽ pode dirigir.')
    else:
        print('Complete 18 anos, e tenha CNH, te aguardarmos ansiosamente.')
except ValueError:
    print('Digite caracteres válidos, tente novamente responder a pesquisa.')


# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Peça ao usuário:

Usuário
Senha

Considere válido apenas se:

Usuário for "admin"
E
Senha for "python123"

Caso contrário, mostrar:
"Acesso negado".

Use AND na validação.
"""

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')


if usuario == 'admin' and senha == 'python123':
    print('Seja bem vindo!')
else:
    print('Tente novamente')



# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Peça três números ao usuário.

Mostre:

"Todos são positivos"

Somente se os três números forem maiores que zero.
Use AND para fazer a verificação.
"""

numero1 = int(input('1 - Digite um número: '))
numero2 = int(input('2 - Digite um número: '))
numero3 = int(input('3 - Digite um número: '))

if numero1 > 0 and numero2 > 0 and numero3 > 0:
    print('Números positivos, ou seja maior que zero.')
else:
    print('Número negativo.')


# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# numero = int(input("Digite um número: "))
# if numero > 10 and numero < 20:
#     print("Número válido")
# else:
#     print("Número inválido")


# Exercício 2 - Médio

# idade = int(input("Digite sua idade: "))
# carteira = input("Possui carteira? (S/N): ")
# if idade >= 18 and carteira == "S":
#     print("Pode dirigir")
# else:
#     print("Não pode dirigir")


# Exercício 3 - Difícil

# usuario = input("Usuário: ")
# senha = input("Senha: ")
# if usuario == "admin" and senha == "python123":
#     print("Acesso permitido")
# else:
#     print("Acesso negado")


# Exercício 4 - Difícil

# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))
# n3 = float(input("Digite o terceiro número: "))
# if n1 > 0 and n2 > 0 and n3 > 0:
#     print("Todos são positivos")
# else:
#     print("Nem todos são positivos")
