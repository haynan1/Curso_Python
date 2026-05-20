'''
Operador Lógico "not"
Usado para inverter expressões
not True = False
not False = True
'''

print(not True) #False
print(not False) #True



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# OPERADOR LÓGICO NOT
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
NOT é o botão de inverter:
Se é True, vira False.
Se é False, vira True.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
O operador lógico "not" é usado para inverter valores booleanos.

Ele trabalha com apenas uma expressão (operador unário).

Funcionamento básico:

not True  → False
not False → True

Ou seja:

• Se a expressão for verdadeira (True), o "not" transforma em False.
• Se a expressão for falsa (False), o "not" transforma em True.

O operador "not" é muito utilizado em:

1) Estruturas condicionais (if)
2) Validações
3) Inversões de lógica
4) Verificação de ausência de valor

Exemplo conceitual:

Se uma variável chamada "ativo" for True,
"not ativo" significa "não está ativo".

É uma maneira simples e poderosa de inverter decisões no código.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie duas variáveis booleanas:

uma chamada ligado = True
outra chamada aberto = False

Depois, mostre o valor invertido de cada uma usando o operador not.
"""

# Criando a variável ligado com valor True
# ligado = True

# Criando a variável aberto com valor False
# aberto = False

# Exibindo o valor invertido de ligado
# print(not ligado)

# Exibindo o valor invertido de aberto
# print(not aberto)

"""
Explicação do código resolvido:

1) Criamos duas variáveis booleanas.
2) Utilizamos o operador "not" antes do nome da variável.
3) O Python inverte automaticamente o valor lógico.
4) Nenhum valor original é alterado — apenas o resultado exibido é invertido.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie uma variável chamada ativo com valor True.
Mostre na tela o valor invertido dessa variável.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie uma variável chamada tem_permissao com valor False.

Use o operador not dentro de um print para mostrar:

"O usuário NÃO tem permissão"

Dica: Use not dentro de uma estrutura condicional (if).
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie uma variável chamada senha_correta com valor False.

Use uma estrutura if para verificar:

Se NÃO for senha correta, mostrar:
"Acesso negado"

Caso contrário, mostrar:
"Acesso permitido"
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Crie duas variáveis:

usuario_logado = True
conta_bloqueada = False

Permita acesso somente se:

O usuário estiver logado
E a conta NÃO estiver bloqueada

Mostre:
"Acesso liberado"

Caso contrário:
"Acesso negado"

Dica: Use not junto com operador lógico and.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# ativo = True
# print(not ativo)

# Exercício 2 - Médio

# tem_permissao = False
# if not tem_permissao:
#     print("O usuário NÃO tem permissão")

# Exercício 3 - Difícil

# senha_correta = False
# if not senha_correta:
#     print("Acesso negado")
# else:
#     print("Acesso permitido")

# Exercício 4 - Difícil

# usuario_logado = True
# conta_bloqueada = False

# if usuario_logado and not conta_bloqueada:
#     print("Acesso liberado")
# else:
#     print("Acesso negado")
