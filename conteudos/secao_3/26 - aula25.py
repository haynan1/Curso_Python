"""
Interpolação básica de Strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

É utilizado o sinal de %
"""

nome = "Haynan"
preco = 1000.95897643
variavel = "%s, o preço é R$%.2f" % (nome, preco) 
#.2 define duas casas decimais após a vírgula.
#variavel = 'Haynan, o preço total foi R$1000.95'
print(variavel)

print(" O hexadecimal de %d é %X" % (1500,1500))

#Dessa forma abaixo ele vai completar com 0, dentro de 8 digitos se não houver valor.
#print(" O hexadecimal de %d é %08X" % (1500,1500))


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# INTERPOLAÇÃO DE STRINGS COM %
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
% formata e organiza:
%s texto,
%d número inteiro,
%f número decimal,
%x hexadecimal.
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
🔎 O que é Interpolação?

Interpolação é o processo de inserir valores dentro de uma string
usando um padrão de formatação.

Em Python, uma das formas mais antigas de fazer isso é usando o operador %.

📌 Estrutura básica:

"texto %tipo" % (valor)

📌 Principais especificadores:

%s → string
%d → número inteiro
%i → número inteiro
%f → número float (decimal)
%x → hexadecimal (letras minúsculas)
%X → hexadecimal (letras maiúsculas)

----------------------------------------
📌 FORMATANDO CASAS DECIMAIS

%.2f

O número 2 indica quantas casas decimais serão exibidas.

Exemplo:
%.2f → 2 casas decimais
%.4f → 4 casas decimais

----------------------------------------
📌 FORMATANDO TAMANHO E PREENCHIMENTO

%08X

8 → largura total
0 → preenche com zero à esquerda
X → hexadecimal maiúsculo

Se o número convertido tiver menos que 8 caracteres,
o Python completa com zeros à esquerda.

----------------------------------------
📌 EXEMPLO CONCEITUAL

nome = "Haynan"
preco = 1000.95897643

"%s, o preço é R$%.2f" % (nome, preco)

Resultado:
Haynan, o preço é R$1000.96

⚠️ IMPORTANTE:
O valor 1000.95897643 foi arredondado para 1000.96
porque pedimos 2 casas decimais.

----------------------------------------
📌 HEXADECIMAL

Hexadecimal é base 16.

Ele usa:
0 1 2 3 4 5 6 7 8 9 A B C D E F

Exemplo:
1500 em hexadecimal = 5DC
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie uma variável com seu nome e outra com um valor decimal.
Mostre uma frase formatada exibindo o nome
e o valor com 3 casas decimais.
Depois mostre o valor convertido para hexadecimal (apenas a parte inteira).
"""

# nome = "Haynan"  # Armazena o nome
# preco = 1000.95897643  # Armazena o valor decimal

# frase = "%s, o valor é R$%.3f" % (nome, preco)  
# %s insere a string
# %.3f formata o número com 3 casas decimais

# print(frase)  # Exibe a frase formatada

# parte_inteira = int(preco)  # Converte o valor para inteiro
# print("Hexadecimal: %X" % parte_inteira)  
# %X converte o número inteiro para hexadecimal maiúsculo

"""
🔎 Explicação:

1) Criamos variáveis para armazenar dados.
2) Utilizamos % para inserir valores dentro da string.
3) %.3f controla as casas decimais.
4) int() remove a parte decimal.
5) %X converte para hexadecimal.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Crie uma variável chamada produto e outra chamada valor.
Mostre a frase:

"O produto X custa R$Y"

Formatando o valor com 2 casas decimais.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Crie uma variável numero = 255.
Mostre:

1) O número em decimal
2) O número em hexadecimal minúsculo
3) O número em hexadecimal maiúsculo
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Crie uma variável com um número inteiro.
Mostre ele formatado:

1) Com 6 dígitos preenchendo com zero à esquerda.
2) Em hexadecimal com 4 dígitos preenchendo com zero.
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Crie variáveis:

nome = "Maria"
idade = 27
salario = 3456.789

Mostre a seguinte frase formatada:

"Maria tem 27 anos e recebe R$3456.79"

Use interpolação com %.
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil

# produto = "Notebook"  # Nome do produto
# valor = 3500.5  # Valor do produto
# print("O produto %s custa R$%.2f" % (produto, valor))  
# %s insere o texto
# %.2f formata com 2 casas decimais

# Exercício 2 - Médio

# numero = 255  # Número inteiro
# print("Decimal: %d" % numero)  # Mostra em decimal
# print("Hexadecimal minúsculo: %x" % numero)  # Hexadecimal minúsculo
# print("Hexadecimal maiúsculo: %X" % numero)  # Hexadecimal maiúsculo

# Exercício 3 - Difícil

# numero = 42  # Número exemplo
# print("Com 6 dígitos: %06d" % numero)  
# %06d → largura 6 preenchido com zero

# print("Hex com 4 dígitos: %04X" % numero)  
# %04X → hexadecimal com largura 4 preenchido com zero

# Exercício 4 - Difícil

# nome = "Maria"  # Nome
# idade = 27  # Idade
# salario = 3456.789  # Salário

# print("%s tem %d anos e recebe R$%.2f" % (nome, idade, salario))  
# %s → string
# %d → inteiro
# %.2f → float com 2 casas decimais
