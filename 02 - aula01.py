"""

Docstring 
Posso escrever o que eu quiser, mas ele não é ignorado pelo python, ele vai ser executado, mas ele não apresenta erros.

"""

''' Usar para escrever suas notas dentro do código '''
#Docstrings, utiliza-se ''' corpo do texto ''' e pode ser utilizado também """ corpo do texto """


# Permite escrever um comentário, na linha que ele está.
# = cerquilha ou hastag.
# Posso colocar em qualquer lugar.

print(123) #Na frente.

#Abaixo.



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# DOCSTRINGS E COMENTÁRIOS EM PYTHON

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
DocString explica, comentário lembra.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
Em Python existem duas formas principais de escrever informações dentro
do código sem afetar o funcionamento do programa:

1) Comentários
2) DocStrings

----------------------------------------
COMENTÁRIOS (#)
----------------------------------------

Comentários são usados para explicar o que o código faz.

Eles começam com o símbolo:

#

Tudo que estiver após esse símbolo na linha será ignorado
pelo interpretador do Python.

Exemplo conceitual:

# Isso é um comentário
# O Python simplesmente ignora esta linha

Também é possível colocar comentários no final de uma linha:

print(123)  # Comentário explicando o que acontece

Nesse caso, apenas o comentário é ignorado.

----------------------------------------
DOCSTRINGS
----------------------------------------

DocStrings são blocos de texto delimitados por:

''' texto '''
ou
\"\"\" texto \"\"\"

Eles são usados principalmente para documentar:

- funções
- classes
- módulos

Exemplo conceitual:

\"\"\"
Esta função soma dois números.
\"\"\"

A diferença importante é:

DocStrings NÃO são exatamente comentários.

Eles são na verdade STRINGS (textos) válidos em Python.

Ou seja:

O Python EXECUTA essa string, mas como ela não está sendo
armazenada em nenhuma variável ou usada em nenhum lugar,
ela simplesmente é descartada.

Por isso:

- Não gera erro
- Não interfere no código
- Serve como documentação

----------------------------------------
RESUMO IMPORTANTE
----------------------------------------

# Comentário

- Começa com #
- Python ignora completamente
- Usado para explicações rápidas

\"\"\" DocString \"\"\"

- É uma string válida
- Python lê mas descarta
- Usada para documentação maior
- Muito comum em funções e classes

----------------------------------------
EXEMPLO VISUAL
----------------------------------------

# Comentário simples

\"\"\" 
DocString explicativa
que pode ocupar várias linhas
\"\"\"

print(123)  # comentário ao lado
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um pequeno exemplo de código contendo:

1) Uma DocString explicando o programa
2) Dois comentários explicando partes do código
3) Um comando print exibindo um número
"""

# """ 
# Programa de exemplo para demonstrar
# o uso de comentários e DocStrings.
# """

# Comentário explicando que vamos imprimir um número
# print(123)

# Comentário dizendo que o programa terminou
# print("Fim do programa")

"""
Explicação do código resolvido.

A primeira parte é uma DocString que descreve o objetivo
do programa.

Depois usamos comentários (#) para explicar o que cada
linha faria.

O código está todo comentado para fins didáticos, ou seja,
nada será executado.

Isso permite estudar o código sem executá-lo.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Escreva um código que contenha:

1) Uma DocString com o texto:
"Programa de teste"

2) Um comentário explicando que o código irá mostrar um número.

3) Um print exibindo o número 10.
"""

'''Programa teste'''
#Vamos exibir um número
print('Olhe o número a seguir:',2005)


# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie um código com:

1) Uma DocString explicando que o programa demonstra comentários.

2) Um comentário antes de cada print.

3) Dois prints mostrando:

100
200
"""

'''Essa séra a DocString, ela utilizamos # para fazer comentários dentro do código.'''

#Olhe esse print
print(100)

#Mais um print
print(200)

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie um pequeno "programa documentado".

Ele deve conter:

1) Uma DocString de várias linhas explicando que o programa
demonstra a diferença entre DocString e comentários.

2) Três comentários espalhados no código.

3) Três prints mostrando:

1
2
3
"""

'''
Uma DocString utiliza-se aspas simples ou duplas, tendo da mesma 3 menções antes e 3 após o código, ja o comentário utilizamos #.
'''

#Primeiro número
print(1)

#Segundo número
print(2)

#Terceiro número
print(3)

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Escreva um exemplo educacional contendo:

1) Uma DocString explicando o programa.
2) Um print com o número 500.
3) Um comentário ao lado do print.
4) Um comentário abaixo explicando que o programa terminou.
"""

''' DocString, os comentários podem ser em qualquer posição do código, observe os exemplos abaixo.'''

#Posso colocar em cima do código também.
print(500) #Posso comentar aqui.
#Aqui o código ja terminou.

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# """Programa de teste"""

# # Este código irá mostrar um número
# # print(10)


# Exercício 2 - Médio

# """
# Programa que demonstra comentários.
# """

# # Primeiro número
# # print(100)

# # Segundo número
# # print(200)


# Exercício 3 - Difícil

# """
# Este programa demonstra a diferença
# entre DocString e comentários.
#
# A DocString documenta o código,
# enquanto os comentários explicam
# partes específicas.
# """

# # Primeiro número
# # print(1)

# # Segundo número
# # print(2)

# # Terceiro número
# # print(3)


# Exercício 4 - Difícil

# """
# Programa de exemplo com documentação
# e comentários.
# """

# # print(500)  # exibindo o número principal

# # Programa finalizado

