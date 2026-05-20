#Exercício, faça as variáveis para exibir o que foi proposto abaixo.

#print("Nome:", nome)
#print("Sobrenome:", sobrenome)
#print("Idade", idade)
#print("Ano de nascimento", ano_nascimento)
#print("É maior de idade?:", maior_de_idade)
#print("Altura em metros:", altura_metros)


''' Resposta '''

nome = "Haynan"
sobrenome = "Kerlin"
idade = 20
ano_nascimento = 2025 - idade
maior_de_idade = idade >= 18
altura_metros = 1.78

print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_nascimento)
print("É maior de idade?:", maior_de_idade)
print("Altura em metros:", altura_metros)


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# VARIÁVEIS + CÁLCULOS + EXIBIÇÃO FORMATADA
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Variável guarda.
Operador calcula.
Print mostra."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Neste exercício trabalhamos três pilares fundamentais:

1) Criação de variáveis
2) Operações matemáticas
3) Exibição organizada com print()

O que está acontecendo no código?

nome = "Haynan"
→ Tipo: str (texto)

idade = 20
→ Tipo: int (número inteiro)

ano_nascimento = 2025 - idade
→ Aqui temos uma EXPRESSÃO.
O Python primeiro resolve a conta.
Depois armazena o resultado na variável.

maior_de_idade = idade >= 18
→ Isso é uma COMPARAÇÃO.
O resultado será True ou False.
O operador >= significa "maior ou igual".

altura_metros = 1.78
→ Tipo: float (número decimal)

Depois usamos print() para exibir tudo organizado.

print("Nome:", nome)

O Python separa os valores por espaço automaticamente
quando usamos vírgula.

Fluxo mental completo:

DADOS → CÁLCULO → COMPARAÇÃO → EXIBIÇÃO

Isso é base da programação.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie variáveis para:

nome = "Ana"
idade = 30
ano_atual = 2025

Crie:
ano_nascimento usando cálculo
maior_de_idade verificando se idade >= 18

Mostre todas as informações.
"""

# nome = "Ana"                          # Criando variável nome
# idade = 30                            # Criando variável idade
# ano_atual = 2025                      # Definindo ano atual
# ano_nascimento = ano_atual - idade    # Calculando ano de nascimento
# maior_de_idade = idade >= 18          # Verificando se é maior de idade
# print("Nome:", nome)                  # Exibindo nome
# print("Idade:", idade)                # Exibindo idade
# print("Ano de nascimento:", ano_nascimento)  # Exibindo ano calculado
# print("É maior de idade?:", maior_de_idade)  # Exibindo resultado booleano

"""
Explicação do código resolvido:

1) Criamos variáveis simples.
2) Fizemos um cálculo matemático.
3) Fizemos uma comparação lógica.
4) Exibimos tudo de forma organizada.

Importante:
A variável pode armazenar tanto valores fixos
quanto resultados de expressões.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie variáveis:

nome = "Carlos"
altura = 1.80

Mostre as duas informações usando print().
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie:

idade = 25
ano_atual = 2025

Calcule o ano de nascimento.
Mostre o resultado.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie:

salario = 2500
aumento = 300

Crie uma variável novo_salario.
Mostre o resultado.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Crie:

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

Calcule a média.
Crie uma variável aprovado que verifique
se média >= 7.
Mostre tudo.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# nome = "Carlos"               # Criando variável nome
# altura = 1.80                 # Criando variável altura
# print("Nome:", nome)          # Exibindo nome
# print("Altura:", altura)      # Exibindo altura

# Exercício 2 - Médio

# idade = 25                    # Definindo idade
# ano_atual = 2025              # Definindo ano atual
# ano_nascimento = ano_atual - idade  # Calculando nascimento
# print("Ano de nascimento:", ano_nascimento)

# Exercício 3 - Difícil

# salario = 2500                # Salário inicial
# aumento = 300                 # Valor do aumento
# novo_salario = salario + aumento  # Somando aumento
# print("Novo salário:", novo_salario)

# Exercício 4 - Difícil

# nota1 = 7.5                   # Primeira nota
# nota2 = 8.0                   # Segunda nota
# nota3 = 6.5                   # Terceira nota
# media = (nota1 + nota2 + nota3) / 3  # Cálculo da média
# aprovado = media >= 7         # Verificando aprovação
# print("Média:", media)        # Exibindo média
# print("Aprovado?:", aprovado) # Exibindo resultado booleano
