'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

# print(1234)
# print(456)
# int('a') #Erro

# '''O que eu pensei e fiz'''

# numero = int(input("Vou dobrar o número que você digitar: "))
# print(f"O dobro de {numero} é {numero * 2}")

# '''O que eu pensei e fiz'''


numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# INTRODUÇÃO AO TRY / EXCEPT
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
TRY tenta.
EXCEPT trata.
Se der erro, o programa não mata.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
O que é try/except?

Em Python, usamos try/except para tratar erros.

Quando o programa executa um código que pode dar problema,
usamos:

try -> tentar executar algo
except -> executar algo caso dê erro

Isso evita que o programa "quebre".

Exemplo clássico de erro:

int('a')

Isso gera um ValueError porque não é possível converter
uma letra em número.

Sem tratamento de erro:
O programa para de funcionar.

Com try/except:
O programa continua funcionando normalmente.

Estrutura básica:

try:
    código que pode dar erro
except:
    código executado se der erro

No seu exemplo:

O usuário digita algo.
Tentamos converter para float.
Se conseguir -> mostramos o dobro.
Se não conseguir -> avisamos que não é número.

IMPORTANTE:
Nunca deixe o except vazio em projetos reais.
O ideal é especificar o tipo de erro:

except ValueError:

Mas para iniciantes, entender o conceito já é o primeiro passo.
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um programa que peça um número ao usuário e mostre
o triplo desse número.

Se o usuário digitar algo que não seja número,
o programa deve informar que ocorreu um erro.
"""

# numero_str = input("Digite um número: ")  # Pede ao usuário um valor e salva como string

# try:
#     numero_float = float(numero_str)      # Tenta converter para número decimal
#     triplo = numero_float * 3             # Calcula o triplo
#     print(f"O triplo de {numero_float} é {triplo}")  # Mostra o resultado
# except:
#     print("Erro: isso não é um número válido.")      # Executa se houver erro na conversão

"""
Explicação do código resolvido:

1) input sempre retorna texto (string).
2) float() tenta converter para número decimal.
3) Se o usuário digitar algo inválido (ex: "abc"),
   o Python gera um erro.
4) O bloco except captura esse erro.
5) O programa continua rodando normalmente.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Peça para o usuário digitar um número e mostre a metade dele.

Caso o usuário digite algo inválido, mostre:
"Valor inválido!"
"""

# print('\n',28 * '--', "\n")

# numero = float(input("Digite um número: "))

# try:
#     divisor = numero // 2
#     print(f"O número {numero} dividido pela metade é {divisor} !!!")
#     print("Parabéns, avance para o próximo degrau !")
# except:
#     print("Valor inválido!")


# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Peça dois números ao usuário e mostre a soma deles.

Se algum dos dois valores não for número,
mostre:
"Um dos valores digitados é inválido."
"""

# print('\n',28 * '--', "\n")

# numero_1 = input("Digite um número qualquer: ")
# numero_2 = input("Digite mais um número: ")

# try:
#     conversao_1 = float(numero_1)
#     conversao_2 = float(numero_2)

#     soma = (conversao_1 + conversao_2)
    
#     print(f"A soma de {numero_1} + {numero_2} é igual a {soma}")

# except:
#     print("Um dos valores digitados é inválido!!!")

# print("Avace, guerreiro !!!")


# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Peça ao usuário um número e tente dividir 100 por esse número.

Trate dois possíveis erros:
1) Valor não numérico.
2) Divisão por zero.

Mostre mensagens diferentes para cada erro.
"""

print("\n", 28 * '--','\n')

numero = input("Digite um número: ")

try:
    numero_para_dividir = float(numero)
    
    resultado = 100 / numero_para_dividir
    
    print(f"Esta é a divisão de 100 por {numero_para_dividir}, e seu resultado é {resultado} !!!")

except ValueError:
    print("Digite um número válido, diferente de zero.")
except ZeroDivisionError:
    print("Você não pode dividir zero.")


# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Peça ao usuário sua idade.

Se for número válido:
- Mostre quantos anos faltam para completar 100 anos.

Se não for número:
- Mostre mensagem de erro.

Se a idade for negativa:
- Mostre mensagem dizendo que idade não pode ser negativa.
"""

idade = input("Digite sua idade: ")

try:
    ...
except ValueError:
    print("Erro: este não é um número válido.")

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# numero = input("Digite um número: ")          # Pede um valor
# try:
#     numero = float(numero)                   # Tenta converter
#     print(numero / 2)                        # Mostra a metade
# except:
#     print("Valor inválido!")                 # Se der erro


# Exercício 2 - Médio

# num1 = input("Digite o primeiro número: ")   # Primeiro valor
# num2 = input("Digite o segundo número: ")    # Segundo valor
# try:
#     num1 = float(num1)                       # Converte primeiro
#     num2 = float(num2)                       # Converte segundo
#     print(num1 + num2)                       # Mostra soma
# except:
#     print("Um dos valores digitados é inválido.")  # Se erro


# Exercício 3 - Difícil

# numero = input("Digite um número: ")         # Entrada do usuário
# try:
#     numero = float(numero)                   # Tenta converter
#     resultado = 100 / numero                 # Tenta dividir
#     print(resultado)                         # Mostra resultado
# except ValueError:
#     print("Você digitou algo que não é número.")   # Erro de conversão
# except ZeroDivisionError:
#     print("Não é possível dividir por zero.")      # Erro matemático


# Exercício 4 - Difícil

# idade = input("Digite sua idade: ")          # Entrada
# try:
#     idade = int(idade)                       # Converte para inteiro
#     if idade < 0:                            # Verifica se é negativa
#         print("Idade não pode ser negativa.")
#     else:
#         print(f"Faltam {100 - idade} anos para você completar 100 anos.")
# except:
#     print("Erro: idade inválida.")
