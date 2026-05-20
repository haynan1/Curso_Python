"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# Cálculo do Primeiro Dígito Verificador do CPF

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Multiplica, soma, vezes 10, divide por 11 — passou de 9, vira zero então."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
📌 O QUE É O DÍGITO VERIFICADOR DO CPF?

O CPF possui 11 dígitos:
- Os 9 primeiros são o número base
- Os 2 últimos são dígitos verificadores

Esses dígitos servem para validar se o CPF é verdadeiro.

--------------------------------------------------

📌 PASSO A PASSO DO PRIMEIRO DÍGITO

Dado:
CPF: 746.824.890-70
Base: 746824890

1. Pegamos os 9 primeiros dígitos

2. Criamos uma contagem regressiva de 10 até 2

3. Multiplicamos cada dígito pelo peso correspondente:

   7 × 10 = 70
   4 × 9  = 36
   6 × 8  = 48
   8 × 7  = 56
   2 × 6  = 12
   4 × 5  = 20
   8 × 4  = 32
   9 × 3  = 27
   0 × 2  = 0

4. Somamos tudo:
   70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

5. Multiplicamos por 10:
   301 × 10 = 3010

6. Pegamos o resto da divisão por 11:
   3010 % 11 = 7

7. Regra final:
   - Se resultado > 9 → vira 0
   - Senão → mantém o valor

✔ Resultado final: 7

--------------------------------------------------

📌 RESUMO

- Multiplica pelos pesos (10 até 2)
- Soma tudo
- Multiplica por 10
- Faz % 11
- Ajusta (se > 9 → 0)

Esse resultado é o primeiro dígito verificador.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Calcule o primeiro dígito do CPF:

123.456.789-??

Usando o método explicado.
"""

# cpf = "123456789"

# soma = 0  # variável acumuladora

# peso = 10  # começa em 10

# for digito in cpf:
#     soma += int(digito) * peso  # multiplica e soma
#     peso -= 1  # diminui o peso

# resultado = (soma * 10) % 11  # aplica regra

# if resultado > 9:
#     resultado = 0  # ajuste final

# print(resultado)

"""
Explicação:

- Percorremos cada dígito
- Multiplicamos pelo peso decrescente
- Somamos tudo
- Aplicamos a regra matemática do CPF
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Explique por que usamos pesos decrescentes (10 até 2) no cálculo do CPF.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Dado o CPF base:

987654321

Calcule manualmente o primeiro dígito verificador.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie um algoritmo (em pseudocódigo) que calcule o primeiro dígito
de qualquer CPF.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Explique o que aconteceria se não existisse a regra:

"Se o resultado for maior que 9, ele vira 0"
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil
# Os pesos decrescentes garantem que cada posição do número tenha
# uma importância diferente, evitando CPFs inválidos passarem.

# Exercício 2 - Médio
# 9×10=90
# 8×9=72
# 7×8=56
# 6×7=42
# 5×6=30
# 4×5=20
# 3×4=12
# 2×3=6
# 1×2=2
# Soma = 330
# 330×10 = 3300
# 3300 % 11 = 0
# Resultado final = 0

# Exercício 3 - Difícil
# Ler CPF (9 dígitos)
# soma = 0
# peso = 10
# Para cada dígito:
#     soma += dígito * peso
#     peso--
# resultado = (soma * 10) % 11
# Se resultado > 9:
#     resultado = 0

# Exercício 4 - Difícil
# Alguns CPFs inválidos poderiam ser considerados válidos,
# pois valores acima de 9 quebrariam o padrão esperado
# de um único dígito (0-9).

