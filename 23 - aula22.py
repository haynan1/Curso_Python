'''
Operadores Lógicos
and (e) or (ou) not (não)

============Focando em or=======================
or - Qualquer condição verdadeira avalia
toda a expressão como verdadeira.
Se qualquer valor for considerado verdadeiro, a 
expressão inteira será avaliada naquele valor.
São considerados falsy (que você já viu)
0 0.0 '' False
Também existe o tipo None que é
usado para representar um não valor
==================================================
'''

# Sistema de exemplificação.

# entrada = input("[E]ntrar [S]air: ")
# senha_digitada = input("Senha: ")

# senha_permitida = "123456"

# if (entrada == "E" or entrada == 'e') and senha_digitada == senha_permitida:
#     print("Sua entrada foi efetuada com sucesso !")
# else:
#     print("Sair")


#Avaliação de curto circuito.
#Vai retornar o primeiro valor verdadeiro encontrado.
print(0 or False or 0 or 'abc')
print(0 or 10 == 10 or 0)

#Exemplo
senha = input("Senha: ") or "Sem senha"
print(senha)



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# OPERADOR LÓGICO OR EM PYTHON
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
No OR, basta um ser verdadeiro para tudo ser verdadeiro.
Ele devolve o primeiro valor verdadeiro que encontrar.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
OPERADORES LÓGICOS EM PYTHON

and  -> Todas as condições precisam ser verdadeiras.
or   -> Basta uma condição ser verdadeira.
not  -> Inverte o valor lógico.

============================
FOCO TOTAL NO OPERADOR OR
============================

O operador OR funciona da seguinte forma:

Se QUALQUER valor for verdadeiro (truthy),
a expressão inteira será considerada verdadeira.

Mas existe um detalhe MUITO importante:

O Python não retorna apenas True ou False.
Ele retorna o PRIMEIRO VALOR VERDADEIRO encontrado.

Isso se chama:
AVALIAÇÃO DE CURTO-CIRCUITO (Short-Circuit)

O Python avalia da esquerda para a direita.
Quando encontra um valor verdadeiro,
ele para imediatamente e retorna esse valor.

============================
VALORES FALSY (considerados falsos)
============================

São considerados falsos:

0
0.0
''
False
None

Qualquer outro valor é considerado TRUE (truthy).

============================
EXEMPLO CONCEITUAL
============================

0 or False or 0 or 'abc'

O Python avalia:

0 -> Falso
False -> Falso
0 -> Falso
'abc' -> Verdadeiro

Então ele retorna: 'abc'

============================
USO PRÁTICO
============================

Muito usado para definir valores padrão:

senha = input("Senha: ") or "Sem senha"

Se o usuário digitar algo → esse valor será usado.
Se o usuário apenas pressionar ENTER → retorna string vazia (falsy),
então o OR retorna "Sem senha".
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um sistema que peça ao usuário uma senha.
Caso ele não digite nada, o sistema deve definir automaticamente
a senha como "Sem senha".
Depois exiba a senha final.
"""

# Código resolvido totalmente comentado

# Solicita a senha ao usuário
# senha = input("Senha: ")

# Se o usuário não digitar nada (string vazia),
# o operador OR define o valor padrão "Sem senha"
# senha_final = senha or "Sem senha"

# Exibe o resultado final
# print(senha_final)

"""
EXPLICAÇÃO DO CÓDIGO

1) input() retorna uma string.
2) Se o usuário pressionar ENTER, o valor será '' (string vazia).
3) String vazia é considerada FALSY.
4) O operador OR retorna o primeiro valor verdadeiro.
5) Se a senha for vazia, retorna "Sem senha".
6) Caso contrário, retorna o que o usuário digitou.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Mostre na tela o resultado da seguinte expressão:

0 or False or 10 or ''

Explique mentalmente qual será o valor retornado.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Peça para o usuário digitar um nome.
Caso ele não digite nada, o sistema deve usar o nome "Visitante".
Depois mostre uma mensagem de boas-vindas com o nome final.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie um sistema que peça:

1) Usuário
2) Senha

Se o usuário for "admin" OU "Admin"
E a senha for "1234"
Mostre: "Acesso liberado"
Caso contrário, mostre: "Acesso negado"
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Sem usar if, crie uma variável chamada status que receba:

"Ativo" se o valor for True
"Desativado" se o valor for False

Utilize apenas operadores lógicos.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# O Python avalia:
# 0 -> Falsy
# False -> Falsy
# 10 -> Truthy (primeiro verdadeiro encontrado)
# Portanto o resultado será:
# 10

# print(0 or False or 10 or '')

# Exercício 2 - Médio

# nome = input("Digite seu nome: ")
# nome_final = nome or "Visitante"
# print(f"Bem-vindo, {nome_final}!")

# Exercício 3 - Difícil

# usuario = input("Usuário: ")
# senha = input("Senha: ")

# if (usuario == "admin" or usuario == "Admin") and senha == "1234":
#     print("Acesso liberado")
# else:
#     print("Acesso negado")

# Exercício 4 - Difícil

# valor = True  # ou False

# status = valor and "Ativo" or "Desativado"

# print(status)

# Explicação:
# Se valor for True:
# True and "Ativo" -> retorna "Ativo"
# "Ativo" or "Desativado" -> retorna "Ativo"
#
# Se valor for False:
# False and "Ativo" -> retorna False
# False or "Desativado" -> retorna "Desativado"
