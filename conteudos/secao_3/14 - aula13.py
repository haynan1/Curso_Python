'''Mostrando um exemplo de f-string'''

nome = "Haynan Kerlin"
altura = 1.78
peso = 68
imc = peso / (altura * altura)

#print(nome, "tem", altura, "de altura, pesa", peso, "kilos e seu IMC é", imc)

linha_1 = f"{nome}, tem {altura} de altura pesa {peso} kilos e seu IMC é {imc}"
print(linha_1)

'''f-string é para formatar os textos, observe como foi colocado na aula 12 e agora como foi colocado na aula 13, veja que precisa da variável existir, para buscar o valor dela.'''


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# F-STRINGS (FORMATAÇÃO DE STRINGS)
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Colocou f na frente?
Chaves pegam a variável automaticamente."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
O que é f-string?

F-string é uma forma moderna e mais organizada
de formatar textos no Python.

Ela permite inserir variáveis diretamente
dentro da string usando { }.

Sintaxe:

f"texto {variavel}"

IMPORTANTE:
A variável precisa já existir antes da f-string.
Senão, dará erro.

Comparação:

FORMA ANTIGA (aula 12):
print(nome, "tem", altura, "de altura...")

FORMA COM F-STRING (aula 13):
f"{nome} tem {altura} de altura..."

Muito mais limpo e organizado.

No arquivo temos:

linha_1 = f"{nome}, tem {altura} de altura pesa {peso} kilos e seu IMC é {imc}"

O que acontece?

1) O Python identifica o f antes da string.
2) Ele procura tudo que está entre { }.
3) Substitui pelo valor da variável.

Vantagens da f-string:

• Código mais legível
• Mais organizado
• Permite formatar números
• Permite colocar expressões dentro das chaves

Exemplo com expressão:

f"{peso / (altura ** 2)}"

Regra mental:

f + "texto {variavel}" = texto formatado automaticamente
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie:

nome = "Carlos"
idade = 25

Mostre uma frase usando f-string:

"Carlos tem 25 anos."
"""

# nome = "Carlos"                           # Criando variável nome
# idade = 25                                # Criando variável idade
# frase = f"{nome} tem {idade} anos."       # Criando f-string
# print(frase)                              # Exibindo resultado

"""
Explicação do código resolvido:

1) Definimos as variáveis.
2) Usamos f antes das aspas.
3) Colocamos variáveis entre { }.
4) O Python substituiu automaticamente os valores.

Simples, limpo e profissional.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie:

produto = "Notebook"
preco = 3500

Mostre:

"O Notebook custa 3500 reais."
Usando f-string.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie:

altura = 1.75
peso = 70

Calcule o IMC dentro da própria f-string
sem criar variável separada para IMC.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie:

nota1 = 8
nota2 = 7
nota3 = 9

Calcule a média dentro da f-string
e mostre:

"Sua média foi X"
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Crie:

nome = "Ana"
saldo = 1234.5678

Mostre o saldo formatado com 2 casas decimais
usando f-string.

Dica:
Use :.2f dentro das chaves.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# produto = "Notebook"                              # Produto
# preco = 3500                                      # Preço
# print(f"O {produto} custa {preco} reais.")        # F-string formatada

# Exercício 2 - Médio

# altura = 1.75                                     # Altura
# peso = 70                                         # Peso
# print(f"IMC: {peso / (altura ** 2)}")             # Cálculo direto na f-string

# Exercício 3 - Difícil

# nota1 = 8                                         # Nota 1
# nota2 = 7                                         # Nota 2
# nota3 = 9                                         # Nota 3
# print(f"Sua média foi {(nota1 + nota2 + nota3) / 3}")  # Média dentro da f-string

# Exercício 4 - Difícil

# nome = "Ana"                                      # Nome
# saldo = 1234.5678                                 # Saldo
# print(f"{nome}, seu saldo é {saldo:.2f}")         # Formatando 2 casas decimais
