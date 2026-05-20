'''
Ordem de execução do cálculo.

1. (n + n)
2. **
3. * / // %
4. + -

'''

conta_1 = 1 + 1 ** 5 + 5 # 7
print(conta_1)


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# ORDEM DE PRECEDÊNCIA DOS OPERADORES
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Parênteses primeiro.
Potência depois.
Multiplica e divide.
Soma e subtrai por fim."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Na matemática (e no Python), existe uma ORDEM
em que os cálculos são executados.

Isso se chama PRECEDÊNCIA DE OPERADORES.

A ordem correta é:

1) ( )  → Parênteses
2) **   → Exponenciação
3) * / // % → Multiplicação e divisões
4) + -  → Soma e subtração

Vamos analisar o exemplo do arquivo:

conta_1 = 1 + 1 ** 5 + 5

Passo 1 → Resolver a potência:
1 ** 5 = 1

Agora a conta vira:
1 + 1 + 5

Passo 2 → Resolver da esquerda para a direita:
1 + 1 = 2
2 + 5 = 7

Resultado final:
7

IMPORTANTE:

Mesmo que a soma esteja antes no código,
a potência é resolvida primeiro.

Se quisermos mudar a ordem,
usamos parênteses.

Exemplo:

(1 + 1) ** 5 + 5

Agora primeiro resolve:
(1 + 1) = 2

Depois:
2 ** 5 = 32

Depois:
32 + 5 = 37

Resultado completamente diferente.

Regra mental:

Sem parênteses → siga a hierarquia.
Com parênteses → eles mandam.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Calcule corretamente:

resultado = 2 + 3 * 4

Explique passo a passo a ordem de execução.
"""

# resultado = 2 + 3 * 4        # Criando expressão
# print(resultado)             # Exibindo resultado

"""
Explicação do código resolvido:

Ordem:

1) Multiplicação primeiro:
3 * 4 = 12

2) Depois soma:
2 + 12 = 14

Resultado final:
14

Se fosse:
(2 + 3) * 4

Primeiro:
2 + 3 = 5

Depois:
5 * 4 = 20
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Calcule mentalmente:

5 + 2 * 3

Depois escreva o código.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Calcule:

10 - 2 ** 3

Explique a ordem de execução.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Calcule:

8 + 4 / 2 * 3

Explique cada etapa da ordem.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Compare os resultados:

1) 2 + 2 * 2
2) (2 + 2) * 2

Explique por que são diferentes.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# resultado = 5 + 2 * 3   # Multiplicação primeiro: 2 * 3 = 6
# # Depois soma: 5 + 6 = 11
# print(resultado)        # 11

# Exercício 2 - Médio

# resultado = 10 - 2 ** 3   # Potência primeiro: 2 ** 3 = 8
# # Depois subtração: 10 - 8 = 2
# print(resultado)          # 2

# Exercício 3 - Difícil

# resultado = 8 + 4 / 2 * 3
# # Divisão primeiro: 4 / 2 = 2.0
# # Depois multiplicação: 2.0 * 3 = 6.0
# # Depois soma: 8 + 6.0 = 14.0
# print(resultado)          # 14.0

# Exercício 4 - Difícil

# resultado1 = 2 + 2 * 2      # Multiplicação primeiro: 2 * 2 = 4
# # Depois soma: 2 + 4 = 6
# print(resultado1)           # 6

# resultado2 = (2 + 2) * 2    # Parênteses primeiro: 2 + 2 = 4
# # Depois multiplicação: 4 * 2 = 8
# print(resultado2)           # 8
