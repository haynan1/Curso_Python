'''

Função 'print'

'''

print(12, 34, sep=" ")
print(56, 78)

#A função print coloca algumas coisas por padrão, imprimi os argumentos não nomeados, e ja coloca espaços print(56, 78, sep=' ') = print(56, 78).

# O VS code se vc selecionar por exemplo o "print" e fazer Ctrl + C e Ctrl + V, ele vai duplicar a linha.

#sep = separador, posso colocar qualquer coisa dentro das aspas.
#Por padrão o print ja coloca um espaço.
print("Banana", "Maçã")
print("Banana", "Maçã","Pera", sep="---")


#\r\n -> CRLF
#\n -> LF
#\n ele faz uma quebra de linha.

print(12,34,1011, sep="  ", end="#")

print(56,78, sep='-', end='\n')
#print(9,10, sep="-", end='\n')

#end = coloque como vai terminar seu código, isso pode ser delimitado.


#Exemplo

import time

for i in range(5):
    print("Carregando...", i, end="\r")
    time.sleep(1)



"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# TÍTULO DO CONTEÚDO
# ========================================

# FUNÇÃO PRINT, SEPARADOR (sep) E FINALIZAÇÃO (end)

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
print mostra, sep separa, end decide como termina.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
A função print() é usada para exibir informações na tela.

Ela é uma das funções mais usadas em Python e possui alguns
comportamentos padrão importantes.

----------------------------------------
ESTRUTURA BÁSICA
----------------------------------------

print(valor1, valor2, valor3)

Exemplo conceitual:

print(12, 34)

Saída esperada:

12 34

O Python automaticamente coloca um espaço entre os valores.

----------------------------------------
ARGUMENTOS NÃO NOMEADOS
----------------------------------------

Os valores dentro do print são chamados de argumentos.

Exemplo:

print(12, 34, 56)

Nesse caso temos três argumentos que serão exibidos.

----------------------------------------
PARÂMETRO sep (SEPARATOR)
----------------------------------------

O parâmetro sep define qual será o separador entre
os valores exibidos.

Por padrão o separador é um espaço.

Exemplo conceitual padrão:

print(56, 78)

Isso é equivalente a:

print(56, 78, sep=" ")

Exemplo alterando o separador:

print("Banana", "Maçã", "Pera", sep="---")

Saída conceitual:

Banana---Maçã---Pera

Ou seja, qualquer texto pode ser usado como separador.

----------------------------------------
PARÂMETRO end
----------------------------------------

O parâmetro end define como a linha termina.

Por padrão o print termina com uma quebra de linha:

end = "\\n"

Exemplo conceitual:

print(10)
print(20)

Saída:

10
20

Se alterarmos o end:

print(10, end=" ")
print(20)

Saída:

10 20

----------------------------------------
QUEBRA DE LINHA
----------------------------------------

Alguns caracteres especiais são usados para formatar texto.

\\n

Significa:

Line Feed (LF)

Ele faz uma quebra de linha.

Exemplo conceitual:

print("Olá\\nMundo")

Saída:

Olá
Mundo

----------------------------------------
CRLF
----------------------------------------

\\r\\n significa:

Carriage Return + Line Feed

Muito usado em sistemas Windows para quebra de linha.

----------------------------------------
CARREGAMENTO EM LOOP
----------------------------------------

Um uso interessante do parâmetro end é criar
efeitos de atualização na mesma linha.

Exemplo conceitual:

for i in range(5):
    print("Carregando...", i, end="\\r")

O caractere \\r faz o cursor voltar para o início da linha,
permitindo atualizar o texto.

Isso é usado em barras de progresso e carregamentos.

----------------------------------------
RESUMO
----------------------------------------

print() → mostra valores na tela

sep → define o separador entre valores

end → define como a linha termina

\\n → quebra de linha

\\r → retorna ao início da linha
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie um exemplo demonstrando:

1) Um print com dois números
2) Um print usando separador "-"
3) Um print usando end para evitar quebra de linha
"""

# # Primeiro exemplo mostrando dois números
# # print(12, 34)

# # Segundo exemplo usando separador personalizado
# # print(56, 78, sep="-")

# # Terceiro exemplo alterando o final da linha
# # print("Olá", end=" ")
# # print("Mundo")

"""
Explicação do código resolvido.

No primeiro exemplo o Python usa o separador padrão,
que é um espaço.

No segundo exemplo usamos sep="-" para substituir
o espaço por um hífen.

No terceiro exemplo usamos end=" " para impedir
a quebra de linha padrão e continuar imprimindo
na mesma linha.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie um print que mostre:

10 20

Utilizando apenas um print.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie um print que mostre:

Python-Java-C++

Usando o parâmetro sep.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Crie dois prints que exibam:

Olá Mundo

Mas sem quebrar linha no primeiro print.
Use o parâmetro end.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Simule um pequeno carregamento.

Use um loop de 3 repetições e um print
com end="\\r" para atualizar a mesma linha.

Exemplo esperado conceitualmente:

Carregando... 0
Carregando... 1
Carregando... 2
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# # print(10, 20)


# Exercício 2 - Médio

# # print("Python", "Java", "C++", sep="-")


# Exercício 3 - Difícil

# # print("Olá", end=" ")
# # print("Mundo")


# Exercício 4 - Difícil

# # import time

# # for i in range(3):
# #     print("Carregando...", i, end="\r")
# #     time.sleep(1)

