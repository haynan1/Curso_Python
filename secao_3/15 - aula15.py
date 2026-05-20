''' Função input - breve explicação'''

#nome = input("Qual seu nome?: ")
#print(f"O meu nome é {nome=}")
#Se quiser ver o nome e valor da varialvel é apenas colocar um igual, como acima.

numero_1 = input("Digite um número: ")
numero_2 = input("Digite outro número: ")

#Esse código não tem checagem de números, o que pode quebrar, se por uma letra, por exemplo. Vamos aprender isso nas próximas aulas.

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f"A soma dos números é: {int_numero_1 + int_numero_2}")



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# FUNÇÃO input() E CONVERSÃO DE TIPOS
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Input sempre devolve texto.
Se quiser número, converta certo."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
O que é a função input()?

input() é usada para receber dados do usuário
através do teclado.

Exemplo:

nome = input("Qual seu nome?: ")

IMPORTANTE:
O input SEMPRE retorna uma STRING (str).

Mesmo que a pessoa digite 10,
o Python recebe "10".

Por isso precisamos converter quando queremos número.

No arquivo vemos:

numero_1 = input("Digite um número: ")
numero_2 = input("Digite outro número: ")

Depois:

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

Aqui ocorre a conversão de string para inteiro.

Se o usuário digitar algo que não seja número,
como "abc",
o programa vai gerar erro.

Isso acontece porque:
int("abc") não é válido.

Sobre o recurso:

print(f"O meu nome é {nome=}")

Quando usamos {variavel=},
o Python mostra:

nome='valor'

Isso é útil para debug.

Fluxo mental:

input → retorna str
int() → converte para número
agora podemos calcular
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um programa que:

1) Peça dois números ao usuário
2) Converta para inteiro
3) Mostre a multiplicação usando f-string
"""

# numero1 = input("Digite o primeiro número: ")      # Recebendo primeiro valor (str)
# numero2 = input("Digite o segundo número: ")       # Recebendo segundo valor (str)
# n1 = int(numero1)                                  # Convertendo para inteiro
# n2 = int(numero2)                                  # Convertendo para inteiro
# print(f"A multiplicação é: {n1 * n2}")             # Exibindo resultado

"""
Explicação do código resolvido:

1) input captura texto.
2) int() transforma texto em número.
3) Agora podemos multiplicar.
4) f-string organiza a saída.

Sempre lembre:
Sem conversão → não faz cálculo corretamente.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Peça ao usuário seu nome.
Mostre:

"Olá, NOME!"
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Peça ao usuário um número.
Converta para inteiro.
Mostre o dobro desse número.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Peça dois números.
Converta para float.
Mostre a divisão entre eles.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Peça um número.
Mostre se ele é par ou ímpar.
(Dica: use módulo %)
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# nome = input("Digite seu nome: ")            # Recebendo nome
# print(f"Olá, {nome}!")                       # Exibindo saudação

# Exercício 2 - Médio

# numero = input("Digite um número: ")         # Recebendo número (str)
# numero_int = int(numero)                     # Convertendo para inteiro
# print(numero_int * 2)                        # Mostrando dobro

# Exercício 3 - Difícil

# numero1 = input("Digite o primeiro número: ")  # Recebendo valor
# numero2 = input("Digite o segundo número: ")   # Recebendo valor
# n1 = float(numero1)                            # Convertendo para float
# n2 = float(numero2)                            # Convertendo para float
# print(n1 / n2)                                 # Exibindo divisão

# Exercício 4 - Difícil

# numero = input("Digite um número: ")         # Recebendo valor
# numero_int = int(numero)                     # Convertendo para inteiro
# par = numero_int % 2 == 0                    # Verificando se é par
# print(par)                                   # Exibindo True ou False
