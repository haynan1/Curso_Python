'''
Exercício 
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:

    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Se nome contém (ou não) espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "Desculpe, você deixou campos vazios."

'''
# H  a  y  n  a  n
# 0  1  2  3  4  5
#-6 -5 -4 -3 -2 -1
nome = input("Digite seu nome: ")
idade = int(input("Qual sua idade?: "))
#idade = input("Qual sua idade?: ") #Sem validação de número

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    
    if ' ' in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços.")

    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# VALIDAÇÃO DE DADOS + STRINGS + CONDIÇÕES
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
Entrada validada evita dor de cabeça.
String bem usada mostra sua força.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Neste exercício trabalhamos três conceitos importantes:

1) input()
Recebe dados do usuário sempre como STRING.

2) Estrutura condicional (if / else)
Permite tomar decisões no código.

3) Manipulação de strings:
- Fatiamento [::-1] para inverter
- Operador "in" para verificar se contém algo
- len() para contar caracteres
- Índices [0] e [-1] para acessar primeira e última letra

⚠️ Ponto MUITO importante:

Quando usamos:

idade = int(input(...))

Se o usuário não digitar nada ou digitar algo que não seja número,
o programa gera ERRO antes mesmo de chegar no if.

Além disso:

if nome and idade:

Essa condição só será verdadeira se:
- nome não for string vazia ""
- idade não for 0

Ou seja:
Se a pessoa tiver 0 anos (hipoteticamente),
o programa cairia no else.

Uma validação mais segura seria verificar
se nome != "" e idade foi digitada corretamente.

Também é importante lembrar:
Espaço conta como caractere no len().
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Peça ao usuário para digitar seu nome e idade.
Se ambos forem digitados, exiba:

- Nome
- Nome invertido
- Se contém espaços
- Quantidade de letras
- Primeira letra
- Última letra

Caso contrário, exiba mensagem de erro.
"""

# nome = input("Digite seu nome: ")                 # Recebe o nome (string)
# idade = input("Qual sua idade?: ")               # Recebe idade como string para evitar erro imediato

# if nome and idade:                               # Verifica se ambos não estão vazios
#     print(f"Seu nome é {nome}")                  # Exibe o nome digitado
#     print(f"Seu nome invertido é {nome[::-1]}")  # Inverte usando passo -1

#     if ' ' in nome:                              # Verifica se existe espaço dentro do nome
#         print("Seu nome contém espaços.")
#     else:
#         print("Seu nome não contém espaços.")

#     print(f"Seu nome tem {len(nome)} letras")    # Conta os caracteres
#     print(f"A primeira letra do seu nome é {nome[0]}")  # Índice 0
#     print(f"A última letra do seu nome é {nome[-1]}")   # Índice -1
# else:
#     print("Desculpe, você deixou campos vazios.")

"""
Explicação do código resolvido:

1) Removemos o int() para evitar erro caso o usuário não digite número.
2) Usamos if nome and idade para validar se não estão vazios.
3) nome[::-1] inverte a string.
4) ' ' in nome verifica se há espaço.
5) len(nome) conta os caracteres.
6) nome[0] pega a primeira letra.
7) nome[-1] pega a última letra.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Peça ao usuário para digitar uma palavra.

Mostre:
- A palavra digitada
- A palavra invertida
- Quantos caracteres ela possui
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Peça ao usuário para digitar um nome completo.

Mostre:
- Se contém espaço
- Quantas letras tem (sem contar espaços)
- O nome todo em letras maiúsculas
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Peça ao usuário para digitar uma frase.

Mostre:
- A frase invertida
- Apenas o primeiro e último caractere
- A frase pulando de 2 em 2 caracteres
- Quantidade total de caracteres
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Peça ao usuário para digitar nome e idade.

Valide:
- Se nome está vazio
- Se idade é número
- Se idade é maior que 0

Se tudo estiver correto, mostre os dados formatados.
Caso contrário, mostre mensagem de erro.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# palavra = input("Digite uma palavra: ")
# if palavra:
#     print(palavra)
#     print(palavra[::-1])
#     print(len(palavra))
# else:
#     print("Campo vazio.")

# Exercício 2 - Médio

# nome = input("Digite seu nome completo: ")
# if nome:
#     print("Contém espaço?" , ' ' in nome)
#     print("Letras sem espaço:", len(nome.replace(" ", "")))
#     print(nome.upper())
# else:
#     print("Campo vazio.")

# Exercício 3 - Difícil

# frase = input("Digite uma frase: ")
# if frase:
#     print(frase[::-1])
#     print(frase[0], frase[-1])
#     print(frase[::2])
#     print(len(frase))
# else:
#     print("Campo vazio.")

# Exercício 4 - Difícil

# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")

# if not nome:
#     print("Nome vazio.")
# elif not idade.isdigit():
#     print("Idade inválida.")
# elif int(idade) <= 0:
#     print("Idade deve ser maior que zero.")
# else:
#     print(f"Nome: {nome}")
#     print(f"Idade: {idade}")
