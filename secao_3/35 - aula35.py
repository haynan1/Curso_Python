'''
Repetições
while (enquanto)
Executa uma ação enquanto um condição for verdadeira.
Loop infinito -> Quando um código não tem fim.
'''

contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print("Acabou a etapa 1 !")

print(30 * "-")

variavel = 10

while variavel >= 10 and variavel <= 20:
    print(variavel)
    variavel = variavel + 1

print("Acabou a etapa 2 !")






"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# WHILE - ESTRUTURA DE REPETIÇÃO
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
WHILE repete enquanto for VERDADEIRO.
Se nunca parar de ser verdadeiro… vira loop infinito.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
O laço de repetição WHILE é usado quando queremos repetir um bloco de código
enquanto uma condição for verdadeira.

Estrutura básica:

while condição:
    bloco de código

A cada repetição:
1) O Python verifica a condição.
2) Se for True → executa o bloco.
3) Volta e verifica novamente.
4) Se for False → o loop termina.

IMPORTANTE:
Se a condição nunca se tornar falsa, teremos um LOOP INFINITO.

Um loop infinito acontece quando:
- A variável de controle não é atualizada.
- A condição nunca deixa de ser verdadeira.
- Esquecemos de alterar algo dentro do loop.

Sempre precisamos de:
✔ Uma variável de controle
✔ Uma condição
✔ Uma atualização dessa variável

Sem atualização → trava.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Analise o código abaixo e explique o que ele faz:

contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print("Acabou a etapa 1 !")
"""

# contador = 0                 # Criamos a variável contador começando em 0

# while contador <= 10:        # Enquanto contador for menor ou igual a 10...
#     contador = contador + 1  # Somamos 1 ao contador
#     print(contador)          # Mostramos o valor atualizado

# print("Acabou a etapa 1 !")  # Mensagem exibida após o fim do loop

"""
Explicação:

O contador começa valendo 0.
Enquanto ele for menor ou igual a 10, o programa:

1) Soma 1 ao contador
2) Mostra o valor

Ele imprime os números de 1 até 11.
Isso acontece porque o incremento acontece antes do print.

Quando o contador chega a 11,
a condição (contador <= 10) se torna falsa.
Então o loop termina.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie um programa que imprima os números de 0 até 5 usando while.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie um programa que imprima os números de 20 até 10 (ordem decrescente).
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Recrie o seguinte trecho explicado abaixo e diga quantas vezes ele executa:

variavel = 10

while variavel >= 10 and variavel <= 20:
    print(variavel)
    variavel = variavel + 1

Explique por que o loop para.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Crie um exemplo de LOOP INFINITO.
Depois explique (em comentário) por que ele nunca para.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# numero = 0                 # começa em 0
# while numero <= 5:         # enquanto for menor ou igual a 5
#     print(numero)          # imprime o número
#     numero = numero + 1    # incrementa 1 para evitar loop infinito

# Exercício 2 - Médio

# numero = 20                # começa em 20
# while numero >= 10:        # enquanto for maior ou igual a 10
#     print(numero)          # imprime o número
#     numero = numero - 1    # decrementa 1 para descer até 10

# Exercício 3 - Difícil

# variavel = 10                              # inicia em 10
# while variavel >= 10 and variavel <= 20:   # condição dupla
#     print(variavel)                        # imprime o valor atual
#     variavel = variavel + 1                # soma 1 a cada repetição

# Explicação:
# O loop executa 11 vezes.
# Ele começa em 10 e termina em 20.
# Quando variavel se torna 21,
# a condição variavel <= 20 fica falsa,
# encerrando o loop.

# Exercício 4 - Difícil

# numero = 1              # inicia com 1
# while numero > 0:       # condição sempre verdadeira
#     print(numero)       # imprime 1
#     # não alteramos a variável

# Explicação:
# Como numero nunca é alterado,
# ele continuará sendo maior que 0 para sempre.
# A condição nunca se torna falsa.
# Isso gera um LOOP INFINITO.
