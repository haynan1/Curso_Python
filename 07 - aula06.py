#Conversão de tipos, coerção
#Type convertion, typecasting, coercion
#É um ato de converter um tipo em outro
#tipos imutáveis e primitivos:
#str, int, float e bool.

print( 1 + 1 ) # Ele soma os valores e te devolve um resultado.
print("a" + "b") # concatenou por conta de são str, e não números, os numeros ele somou.

print(int("1"), type(int("1")))
print(int("1") + 1)
print(type(float("1.5") + 1))

print(bool(" ")) # O espaço também é caracterizado como caracter e considerado True.
print(str(11) + "b")

#Isso é para fazer a conversão de um tipo para outro.


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# CONVERSÃO DE TIPOS EM PYTHON
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Se o tipo não combina, o Python reclama.
Converta primeiro, depois calcula."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
CONVERSÃO DE TIPOS (Type Casting / Type Conversion)

Converter tipos é o ato de transformar um dado de um tipo para outro.

Em Python, os tipos primitivos imutáveis mais comuns são:

- str  → texto
- int  → número inteiro
- float → número decimal
- bool → verdadeiro ou falso

Por que isso é importante?

Porque o Python não permite misturar tipos incompatíveis em certas operações.

Exemplo:
int + int → soma
str + str → concatenação
int + str → ERRO

O Python pode fazer dois tipos de conversão:

1) Conversão explícita (manual)
   Quando usamos funções como:
   int()
   float()
   str()
   bool()

2) Coerção (automática)
   Quando o Python ajusta o tipo sozinho.
   Exemplo:
   float + int → resultado será float

Exemplos importantes do seu código original:

1 + 1 → soma = 2
"a" + "b" → concatenação = "ab"

int("1") → transforma texto em número
float("1.5") → transforma texto decimal em número decimal

bool(" ") → retorna True
Qualquer string NÃO vazia é considerada True.
Somente:
"" (string vazia)
0
0.0
None
False
São considerados False.

str(11) + "b" → converte 11 para texto e concatena.

Resumo mental:

NÚMERO + NÚMERO → soma
TEXTO + TEXTO → junta
MISTUROU? → converta antes
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um programa que receba o número "10" como string,
converta para inteiro, some com 5 e depois transforme
o resultado final em string novamente.
"""

# numero_texto = "10"            # Criamos uma variável com valor texto
# numero_inteiro = int(numero_texto)  # Convertendo string para inteiro
# soma = numero_inteiro + 5      # Somando 5 ao número convertido
# resultado_final = str(soma)    # Convertendo o resultado para string
# print(resultado_final)         # Exibindo o resultado final

"""
Explicação do código resolvido:

1) Criamos uma string "10".
2) Convertimos para inteiro usando int().
3) Realizamos a soma normalmente.
4) Convertimos novamente para string usando str().
5) Exibimos o resultado.

Fluxo mental:
str → int → cálculo → str
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie uma variável chamada valor com o conteúdo "25".
Converta para inteiro e some com 5.
Mostre o tipo do resultado final.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie uma variável chamada numero com o valor "3.5".
Converta para float.
Multiplique por 2.
Mostre o tipo do resultado.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie uma variável chamada entrada com o valor "" (string vazia).
Converta para bool e mostre o resultado.
Explique por que isso acontece.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Crie duas variáveis:
a = "10"
b = 5

Converta corretamente para realizar a soma
e exiba o resultado como string.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# valor = "25"                  # Criando string
# valor_convertido = int(valor) # Convertendo para inteiro
# resultado = valor_convertido + 5  # Somando 5
# print(type(resultado))         # Mostrando tipo (int)

# Exercício 2 - Médio

# numero = "3.5"                # Criando string
# numero_convertido = float(numero) # Convertendo para float
# resultado = numero_convertido * 2  # Multiplicando por 2
# print(type(resultado))         # Mostrando tipo (float)

# Exercício 3 - Difícil

# entrada = ""                  # String vazia
# resultado = bool(entrada)     # Convertendo para booleano
# print(resultado)              # Resultado será False
# Explicação:
# String vazia é considerada False em Python.

# Exercício 4 - Difícil

# a = "10"                      # String
# b = 5                         # Inteiro
# soma = int(a) + b             # Convertendo a para inteiro
# resultado = str(soma)         # Convertendo resultado para string
# print(resultado)              # Exibindo resultado final