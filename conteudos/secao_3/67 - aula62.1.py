"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# Cálculo do Segundo Dígito Verificador do CPF

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Agora vai até 11, inclui o primeiro também — repete o processo e valida no fim."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
📌 DIFERENÇA ENTRE PRIMEIRO E SEGUNDO DÍGITO

O cálculo do segundo dígito é MUITO parecido com o primeiro,
mas com duas diferenças importantes:

1. Agora usamos 10 dígitos (os 9 + o primeiro dígito)
2. O peso começa em 11 (e vai até 2)

--------------------------------------------------

📌 PASSO A PASSO

CPF: 746.824.890-70
Base + primeiro dígito: 7468248907

Pesos:
11 10 9 8 7 6 5 4 3 2

Multiplicações:

7 × 11 = 77
4 × 10 = 40
6 × 9  = 54
8 × 8  = 64
2 × 7  = 14
4 × 6  = 24
8 × 5  = 40
9 × 4  = 36
0 × 3  = 0
7 × 2  = 14

Soma:
363

Multiplica por 10:
363 × 10 = 3630

Resto da divisão por 11:
3630 % 11 = 0

Regra final:
- Se > 9 → 0
- Senão → valor

✔ Resultado final: 0

--------------------------------------------------

📌 LÓGICA COMPLETA DO CPF

1. Calcula o primeiro dígito
2. Adiciona esse dígito ao final
3. Calcula o segundo dígito com peso maior

--------------------------------------------------

📌 ERRO COMUM

Muita gente esquece de incluir o primeiro dígito no segundo cálculo.

Isso invalida totalmente o resultado.

--------------------------------------------------

📌 RESUMO

- Usa 10 dígitos (inclui o primeiro)
- Peso começa em 11
- Mesmo processo matemático
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Complete o código para calcular o SEGUNDO dígito do CPF
usando o primeiro dígito já calculado.
"""

# cpf = '74682489070'

# nove_digitos = cpf[:9]  # pega os 9 primeiros

# # =========================
# # CÁLCULO DO PRIMEIRO DÍGITO
# # =========================
# soma_1 = 0
# peso_1 = 10

# for digito in nove_digitos:
#     soma_1 += int(digito) * peso_1  # multiplica e soma
#     peso_1 -= 1  # decrementa peso

# digito_1 = (soma_1 * 10) % 11  # regra do CPF
# digito_1 = digito_1 if digito_1 <= 9 else 0  # ajuste

# # =========================
# # CÁLCULO DO SEGUNDO DÍGITO
# # =========================

# dez_digitos = nove_digitos + str(digito_1)  # adiciona o primeiro dígito

# soma_2 = 0
# peso_2 = 11

# for digito in dez_digitos:
#     soma_2 += int(digito) * peso_2  # multiplica e soma
#     peso_2 -= 1  # decrementa peso

# digito_2 = (soma_2 * 10) % 11  # regra
# digito_2 = digito_2 if digito_2 <= 9 else 0  # ajuste

# print(digito_2)

"""
Explicação:

- Primeiro calculamos o dígito 1
- Depois adicionamos ele à base
- Repetimos o processo com peso iniciando em 11
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Explique por que o segundo dígito depende do primeiro.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Calcule manualmente o segundo dígito para:

CPF base: 123456789
(Use o primeiro dígito que você calcular antes)
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie um pseudocódigo que valide um CPF completo (11 dígitos).
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Explique por que esse algoritmo dificulta a geração de CPFs falsos.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil
# Porque ele usa o primeiro dígito no cálculo, criando uma dependência.
# Isso aumenta a segurança do CPF.

# Exercício 2 - Médio
# (depende do cálculo anterior)
# Após encontrar o primeiro dígito:
# repetir o processo com peso 11 e incluir o dígito 1 no final

# Exercício 3 - Difícil
# Ler CPF
# Separar os 9 primeiros dígitos
# Calcular dígito 1
# Adicionar ao final
# Calcular dígito 2
# Comparar com os dois últimos dígitos do CPF
# Se iguais → válido

# Exercício 4 - Difícil
# Porque cria uma verificação matemática encadeada,
# dificultando combinações aleatórias válidas.
