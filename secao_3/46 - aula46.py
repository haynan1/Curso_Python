for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1,3):
        print(i,j)
else:
    print('For completo com sucesso!')





"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# BREAK, CONTINUE E ELSE NO FOR
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
Continue pula.
Break interrompe.
Else só roda se NÃO quebrar.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Vamos entender o comportamento do seu código:

🔹 CONTINUE
Quando o Python encontra "continue", ele:
- PULA o restante do bloco atual
- Vai para a próxima iteração do loop

No seu código:
if i == 2:
    continue

👉 Ou seja:
Quando i for 2, ele NÃO executa o for interno.

---

🔹 BREAK
Quando o Python encontra "break", ele:
- INTERROMPE completamente o loop

No seu código:
if i == 8:
    break

👉 Ou seja:
Quando i for 8, o loop para imediatamente.

---

🔹 ELSE NO FOR
O else no for é pouco conhecido.

Ele SÓ executa se o loop terminar naturalmente (sem break).

✔ Terminou normal → executa o else
❌ Teve break → NÃO executa o else

---

🔹 FLUXO DO SEU CÓDIGO

Loop de i: 0 até 9

i = 0 → roda normal
i = 1 → roda normal
i = 2 → cai no continue (pula o resto)
i = 3 → roda normal
i = 4 → roda normal
i = 5 → roda normal
i = 6 → roda normal
i = 7 → roda normal
i = 8 → cai no break → PARA TUDO

Como teve break:
👉 O else NÃO executa

---

🔹 FOR INTERNO

for j in range(1,3):

👉 j vai ser:
1 e 2

Então cada i válido imprime:
(i, 1) e (i, 2)

---

Resumo final:

continue → ignora o resto da rodada
break → mata o loop
else → só roda se NÃO houver break
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Reescreva o código explicando cada linha com comentários.
"""

# for i in range(10):                 # Loop de 0 até 9
#     if i == 2:                      # Se i for 2
#         print('i é 2, pulando...')  # Mensagem
#         continue                    # Pula para próxima iteração
#
#     if i == 8:                      # Se i for 8
#         print('i é 8, seu else não executará')  # Mensagem
#         break                       # Interrompe o loop
#
#     for j in range(1,3):            # Loop interno (1 e 2)
#         print(i, j)                 # Mostra i e j
#
# else:                              # Só executa se NÃO houver break
#     print('For completo com sucesso!')

"""
Explicação:

- O loop roda normalmente até i == 8
- Quando chega em 8, o break encerra tudo
- Por isso, o else não é executado
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie um for de 0 a 5.
Quando o número for 3, use continue.
Imprima os demais valores.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie um for de 0 a 5.
Quando encontrar o número 4, use break.
Adicione um else para mostrar uma mensagem caso o loop termine normalmente.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie um loop que percorre números de 0 a 10.
Pare o loop quando encontrar um número divisível por 7.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Simule um sistema que percorre uma lista de nomes.
Se encontrar "admin", pare o loop.
Caso não encontre, mostre "Nenhum admin encontrado" usando else.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# for i in range(6):          # Loop de 0 a 5
#     if i == 3:              # Se for 3
#         continue            # Pula
#     print(i)                # Mostra os outros

# Exercício 2 - Médio

# for i in range(6):          # Loop de 0 a 5
#     if i == 4:              # Se for 4
#         break               # Interrompe
#     print(i)                # Mostra valores
# else:
#     print("Terminou normal")  # Só aparece sem break

# Exercício 3 - Difícil

# for i in range(11):         # 0 a 10
#     if i % 7 == 0 and i != 0:  # Divisível por 7 (exceto 0)
#         break               # Para o loop
#     print(i)                # Mostra número

# Exercício 4 - Difícil

# nomes = ["joao", "maria", "admin", "ana"]  # Lista
# for nome in nomes:                         # Percorrendo lista
#     if nome == "admin":                    # Encontrou admin
#         print("Admin encontrado")          # Mensagem
#         break                             # Para o loop
# else:
#     print("Nenhum admin encontrado")      # Só se não houver break
