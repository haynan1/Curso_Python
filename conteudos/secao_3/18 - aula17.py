# Condicionais no Python

# if / elif     / else
# Se /se não se / se não

# está escrito false, mas geralmente não fica dessa forma.
condicao1 = True 
condicao2 = False
condicao3 = True
condicao4 = False


if condicao1:
    print("Código para a condição 1")
    print("Pode ter quantas linhas de código eu quiser dentro de cada condição.")
elif condicao2:
    print("Código para a condição 2")
elif condicao3:
    print("Código para a condição 3")
elif condicao4:
    print("Código para a condição 4")
else:
    print("Nenhuma condição foi satisfeita.")


if 10 == 10:
    print("Outro bloco de if")

print("Fora do if")


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# CONDICIONAIS NO PYTHON (if / elif / else)
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
IF testa.
ELIF testa outra.
ELSE resolve o que sobra.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Condicionais são estruturas de decisão.

Elas permitem que o programa escolha qual bloco de código executar
com base em uma condição verdadeira (True) ou falsa (False).

Estrutura básica:

if condição:
    bloco

elif outra_condição:
    outro_bloco

else:
    bloco_final

Regras importantes:

1) O Python executa apenas o primeiro bloco verdadeiro.
2) Se uma condição for verdadeira, as próximas não são verificadas.
3) O else é opcional.
4) A indentação define o bloco de execução.
5) Um novo if inicia um novo bloco independente.

No arquivo enviado, temos vários exemplos importantes:

- Uso de variáveis booleanas.
- Cadeia de elif.
- Um segundo if separado do primeiro.
- Código fora do if (executado sempre).

Isso é fundamental para entender fluxo de execução.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie três variáveis booleanas:
usuario_logado
usuario_admin
usuario_bloqueado

Regras:
- Se estiver bloqueado, mostrar "Acesso negado".
- Senão, se for admin, mostrar "Acesso total".
- Senão, se estiver logado, mostrar "Acesso parcial".
- Senão, mostrar "Faça login".
"""

# usuario_logado = True
# usuario_admin = False
# usuario_bloqueado = False

# if usuario_bloqueado:
#     print("Acesso negado")
# elif usuario_admin:
#     print("Acesso total")
# elif usuario_logado:
#     print("Acesso parcial")
# else:
#     print("Faça login")

"""
Explicação do código resolvido:

Primeiro verificamos se o usuário está bloqueado.
Essa condição vem primeiro porque ela impede qualquer outro acesso.

Depois verificamos se ele é administrador.
Se for verdadeiro, o restante não é testado.

Depois verificamos se está apenas logado.

Caso nenhuma condição seja satisfeita,
o else executa como alternativa final.

Ordem das condições altera completamente o resultado.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie uma variável chamada numero.

Se o número for maior que 0, mostre:
"Número positivo"

Caso contrário, mostre:
"Número negativo ou zero"
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie uma variável chamada idade.

Se idade for menor que 12:
"Criança"

Se for menor que 18:
"Adolescente"

Se for menor que 60:
"Adulto"

Caso contrário:
"Idoso"
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie duas variáveis:
nota
frequencia

Regras:
Se nota for maior ou igual a 7 E frequência maior ou igual a 75:
"Aprovado"

Se nota for maior ou igual a 5 E frequência maior ou igual a 75:
"Recuperação"

Caso contrário:
"Reprovado"
"""

print('\n',10 * '---')

nota = 5
frequencia = 74

if nota >= 7 and frequencia >= 75:
    print('Aprovado.')
elif nota <= 7 and frequencia >= 75:
    print('Recuperação.')
else:
    print('Reprovado.')



# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Simule um sistema de caixa eletrônico.

Crie:
saldo
valor_saque

Regras:
Se valor_saque for maior que saldo:
"Saldo insuficiente"

Se valor_saque for igual ao saldo:
"Saque total realizado"

Se valor_saque for menor que saldo:
"Saque realizado"

Caso valor_saque seja menor ou igual a zero:
"Valor inválido"
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# numero = 5
# if numero > 0:
#     print("Número positivo")
# else:
#     print("Número negativo ou zero")


# Exercício 2 - Médio

# idade = 25
# if idade < 12:
#     print("Criança")
# elif idade < 18:
#     print("Adolescente")
# elif idade < 60:
#     print("Adulto")
# else:
#     print("Idoso")


# Exercício 3 - Difícil

# nota = 6
# frequencia = 80
# if nota >= 7 and frequencia >= 75:
#     print("Aprovado")
# elif nota >= 5 and frequencia >= 75:
#     print("Recuperação")
# else:
#     print("Reprovado")


# Exercício 4 - Difícil

# saldo = 1000
# valor_saque = 500

# if valor_saque <= 0:
#     print("Valor inválido")
# elif valor_saque > saldo:
#     print("Saldo insuficiente")
# elif valor_saque == saldo:
#     print("Saque total realizado")
# else:
#     print("Saque realizado")
