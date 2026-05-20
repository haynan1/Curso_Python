'''
Operadores in e not in
Strings são iteráveis
 0 1 2 3 4 5
 o t á v i o
-6-5-4-3-2-1
'''

nome = "Otávio"
# print(nome[2])
# print(nome[-4])
# print("vio" in nome)
# print("zero" in nome)
# print(10 * "-")
# print("vio" not in nome)
# print("zero" not in nome)

nome = input("Digite seu nome: ")
encontrar = input("digite o que deseja encontrar:")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")



'''Outra forma de fazer, é fazer ao contrário'''



nome = input("Digite seu nome: ")
encontrar = input("digite o que deseja encontrar:")

if encontrar not in nome:
    print(f"{encontrar} não está em {nome}")
else:
    print(f"{encontrar} está em {nome}")



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# OPERADORES in E not in (STRINGS)
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
IN pergunta: "Está dentro?"
NOT IN pergunta: "Não está dentro?"
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
🔎 OPERADORES in e not in

Os operadores in e not in são usados para verificar se um valor
está contido dentro de outro valor iterável.

📌 O que é um iterável?
É qualquer estrutura que pode ser percorrida elemento por elemento.
Exemplos:
- Strings
- Listas
- Tuplas
- Dicionários
- Conjuntos

📌 Strings são iteráveis!

Exemplo:

nome = "Otávio"

Cada caractere possui um índice:

 0  1  2  3  4  5
 O  t  á  v  i  o
-6 -5 -4 -3 -2 -1

Podemos acessar caracteres usando índices positivos ou negativos.

📌 Operador in

Ele verifica se uma sequência existe dentro da string.

Exemplo:
"vio" in "Otávio" → True
"zero" in "Otávio" → False

📌 Operador not in

Faz exatamente o contrário.

"vio" not in "Otávio" → False
"zero" not in "Otávio" → True

📌 Comparação é sensível a maiúsculas e minúsculas!

"o" in "Otávio" → True
"O" in "Otávio" → True
"otávio" in "Otávio" → False

Se quiser ignorar maiúsculas/minúsculas,
podemos usar .lower().

Esses operadores são muito usados para:
- Verificar textos
- Validar entradas do usuário
- Criar filtros
- Sistemas de busca simples
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um programa que peça ao usuário seu nome
e depois peça um trecho de texto para procurar.
O programa deve informar se o trecho está contido no nome.
"""

# nome = input("Digite seu nome: ")  # Recebe o nome digitado pelo usuário
# encontrar = input("Digite o que deseja encontrar: ")  # Recebe o texto que será buscado

# if encontrar in nome:  # Verifica se o texto digitado está dentro do nome
#     print(f"{encontrar} está em {nome}")  # Mostra mensagem positiva
# else:  # Caso contrário
#     print(f"{encontrar} não está em {nome}")  # Mostra mensagem negativa

"""
🔎 Explicação do código:

1) input() recebe dados digitados pelo usuário.
2) A variável 'encontrar' guarda o texto que será buscado.
3) O operador 'in' verifica se existe correspondência.
4) O if decide qual mensagem será exibida.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Peça ao usuário uma palavra.
Verifique se a letra "a" está presente nela.
Mostre uma mensagem informando o resultado.
"""

palavra = input('Digite uma palavra: ')
encontrar_letra = input('O que deseja encontrar: ')

if encontrar_letra in palavra:
    print(f'{encontrar_letra} está dentro da palavra/frase {palavra}.')
else:
    print(f'Essa letra {encontrar_letra} não está contida em {palavra}.')



# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Peça ao usuário uma frase.
Verifique se a palavra "python" está presente,
ignorando maiúsculas e minúsculas.
"""

frase = input('Digite uma frase: ')
frase1 = frase.lower() 
#Quando chamar uma função lembre de colocar os parentes,
#para torna-la executável.

if 'python' in frase1:
    print('A palavra python está presente!')
else:
    print('Não está presente a palavra python na frase.')


# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Peça ao usuário um e-mail.
Verifique se ele contém o caractere "@"
e também se contém ".com".

Informe se o e-mail parece válido ou não.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Peça ao usuário uma palavra.
Verifique se ela NÃO contém números.
Use os operadores in ou not in junto com um laço.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# palavra = input("Digite uma palavra: ")  # Recebe a palavra
# if "a" in palavra:  # Verifica se a letra "a" está presente
#     print("A letra 'a' está presente.")
# else:  # Caso não esteja
#     print("A letra 'a' não está presente.")

# Exercício 2 - Médio

# frase = input("Digite uma frase: ")  # Recebe a frase
# frase = frase.lower()  # Converte tudo para minúsculo
# if "python" in frase:  # Verifica se contém "python"
#     print("A palavra 'python' está presente.")
# else:  # Caso contrário
#     print("A palavra 'python' não está presente.")

# Exercício 3 - Difícil

# email = input("Digite seu e-mail: ")  # Recebe o e-mail
# if "@" in email and ".com" in email:  # Verifica se contém ambos
#     print("E-mail parece válido.")
# else:  # Caso contrário
#     print("E-mail inválido.")

# Exercício 4 - Difícil

# palavra = input("Digite uma palavra: ")  # Recebe a palavra
# tem_numero = False  # Variável de controle

# for caractere in palavra:  # Percorre cada caractere da palavra
#     if caractere in "0123456789":  # Verifica se é número
#         tem_numero = True  # Marca que encontrou número

# if tem_numero:  # Se encontrou número
#     print("A palavra contém números.")
# else:  # Se não encontrou
#     print("A palavra NÃO contém números.")