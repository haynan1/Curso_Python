'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim.
'''

contador = 0

while contador <= 100:
    contador += 1 #Cuidado com essa linha

    if contador == 6:
        print("Não vou mostrar o 6.")
        continue

    if contador >= 10 and contador <= 27:
        print("Não vou mostrar o", contador)
        continue

    print(contador)

    if contador == 40:
        break # Termina o laço, quebra ele.


print("Acabou")




"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# LAÇO DE REPETIÇÃO - WHILE
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
WHILE repete ENQUANTO for verdadeiro.
Se nunca deixar de ser verdadeiro... vira pesadelo.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
O laço WHILE é uma estrutura de repetição usada quando
não sabemos exatamente quantas vezes o código vai executar.

Ele funciona assim:

while condição:
    bloco de código

Enquanto a condição for verdadeira (True),
o bloco continuará executando.

⚠️ Muito cuidado:
Se a condição nunca se tornar falsa,
criamos um LOOP INFINITO.

----------------------------------------

Palavras importantes:

• contador → variável usada para controlar repetições
• continue → pula para a próxima iteração do laço
• break → encerra o laço imediatamente

----------------------------------------

Fluxo do while:

1) Verifica a condição
2) Se for True → executa o bloco
3) Volta para o início
4) Repete até a condição ser False
ou encontrar um break

----------------------------------------

Sobre o "continue":

Quando o Python encontra "continue",
ele ignora o restante do código dentro do laço
e volta para o início da repetição.

----------------------------------------

Sobre o "break":

Quando o Python encontra "break",
ele interrompe completamente o laço,
mesmo que a condição ainda seja verdadeira.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Analise o código abaixo e entenda o funcionamento do while,
do continue e do break.
"""

# contador = 0
#
# while contador <= 100:
#     contador += 1  # Incrementa o contador antes de qualquer verificação
#
#     # Se o contador for igual a 6
#     if contador == 6:
#         print("Não vou mostrar o 6.")
#         continue  # Pula o restante do código e volta para o while
#
#     # Se o contador estiver entre 10 e 27
#     if contador >= 10 and contador <= 27:
#         print("Não vou mostrar o", contador)
#         continue  # Pula para a próxima repetição
#
#     # Se não caiu em nenhuma condição acima
#     print(contador)
#
#     # Se o contador chegar a 40
#     if contador == 40:
#         break  # Encerra o laço imediatamente
#
# print("Acabou")

"""
Explicação do fluxo:

1) O contador começa em 0.
2) Ele é incrementado logo no início do laço.
3) Quando chega em 6:
   - Não imprime o número.
   - Mostra mensagem.
   - Usa continue.
4) Entre 10 e 27:
   - Não mostra os números.
   - Apenas imprime mensagem.
5) Quando chega em 40:
   - O break encerra o laço.
6) O print("Acabou") é executado após o fim do while.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie um programa que:

1) Comece com contador = 0
2) Enquanto contador for menor ou igual a 5
3) Mostre o valor do contador
4) Incremente de 1 em 1
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie um programa que:

1) Comece em 0
2) Conte até 20
3) Não mostre os números múltiplos de 3
4) Mostre apenas os demais números
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie um programa que:

1) Conte de 1 até 50
2) Quando encontrar o número 25, pare o laço
3) Não mostre números pares
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Crie um programa que:

1) Peça um número ao usuário (simulado em variável)
2) Enquanto o número for diferente de 0:
   - Mostre o número
   - Diminua 1
3) Quando chegar em 0, mostre "Fim"
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# contador = 0
# while contador <= 5:          # Enquanto for menor ou igual a 5
#     print(contador)           # Mostra o valor atual
#     contador += 1             # Incrementa 1

# Exercício 2 - Médio

# contador = 0
# while contador <= 20:                     # Enquanto for menor ou igual a 20
#     contador += 1                         # Incrementa primeiro
#     if contador % 3 == 0:                 # Verifica se é múltiplo de 3
#         continue                          # Pula os múltiplos de 3
#     print(contador)                       # Mostra os demais números

# Exercício 3 - Difícil

# contador = 0
# while contador < 50:                      # Enquanto for menor que 50
#     contador += 1                         # Incrementa
#     if contador == 25:                    # Se for 25
#         break                             # Interrompe o laço
#     if contador % 2 == 0:                 # Se for par
#         continue                          # Pula números pares
#     print(contador)                       # Mostra apenas ímpares

# Exercício 4 - Difícil

# numero = 5                                # Número simulado
# while numero != 0:                        # Enquanto for diferente de 0
#     print(numero)                         # Mostra o número
#     numero -= 1                           # Diminui 1
# print("Fim")                              # Executado após o laço
