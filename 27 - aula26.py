"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')


"""
========================================
MATERIAL DE SUPORTE - JAMES IA 🤖↓↓↓
========================================
"""

# ========================================
# FORMATAÇÃO DE STRINGS COM F-STRINGS
# ========================================

# ========================================
# FRASE MNEMÔNICA
# ========================================

"""
"Formato tem ordem: valor, dois pontos, regras e exibição."
"""

# ========================================
# EXPLICAÇÃO DIDÁTICA
# ========================================

"""
F-strings são uma forma moderna e poderosa de formatar textos no Python.
Elas utilizam a letra f antes das aspas e permitem inserir variáveis
diretamente dentro da string usando chaves {}.

Estrutura básica:

f'{valor:formatação}'

Após os dois pontos (:), podemos definir regras de formatação.

Principais tipos:

s  -> string
d  -> inteiro
f  -> float
x  -> hexadecimal minúsculo
X  -> hexadecimal maiúsculo

Controle de casas decimais:

:.2f   -> 2 casas decimais
:.1f   -> 1 casa decimal

Alinhamento e largura:

(>)(<)(^) definem alinhamento
>  -> Alinha à direita
<  -> Alinha à esquerda
^  -> Centraliza

Exemplo:
:>10  -> ocupa 10 espaços alinhando à direita

Preenchimento com zeros:

0>10  -> completa com zeros à esquerda
0=10  -> força o sinal a aparecer antes dos zeros

Sinal numérico:

+  -> sempre mostra o sinal (+ ou -)
-  -> mostra apenas se for negativo

Separador de milhares:

,  -> adiciona vírgula como separador

Hexadecimal:

:08X  -> 8 caracteres, preenchido com zero, hexadecimal maiúsculo

Flags de conversão:

!r  -> representação oficial (repr)
!s  -> conversão padrão (str)
!a  -> representação ASCII

Exemplo completo:
f'{1000.4873648123746:0=+10,.1f}'

Ordem da formatação:
[preenchimento][alinhamento][sinal][largura][separador][.casas][tipo]
"""

# ========================================
# EXERCÍCIO RESOLVIDO
# ========================================

"""
Crie uma variável chamada nome com o valor "Python".
Mostre:
1) O nome centralizado em 20 espaços.
2) O nome alinhado à direita com 15 espaços.
3) O nome usando !r.
"""

# nome = "Python"                    # Criando variável nome
# print(f'{nome:^20}')               # Centralizando em 20 espaços
# print(f'{nome:>15}')               # Alinhando à direita com 15 espaços
# print(f'{nome!r}')                 # Mostrando representação oficial

"""
Explicação:

:^20  -> Centraliza o texto em 20 posições.
:>15  -> Alinha o texto à direita em 15 posições.
!r    -> Mostra a representação oficial da string, incluindo aspas.
"""

# ========================================
# EXERCÍCIO 1 - FÁCIL
# ========================================

"""
Exercício 1 - Fácil

Crie uma variável valor = 50.
Mostre o valor com 5 espaços alinhado à esquerda.
"""

# ========================================
# EXERCÍCIO 2 - MÉDIO
# ========================================

"""
Exercício 2 - Médio

Crie uma variável preco = 1234.5678.
Mostre:
1) Com 2 casas decimais.
2) Com separador de milhar.
3) Sempre mostrando o sinal.
"""

# ========================================
# EXERCÍCIO 3 - DIFÍCIL
# ========================================

"""
Exercício 3 - Difícil

Mostre o número 255 em hexadecimal:
1) Em minúsculo
2) Em maiúsculo
3) Com 6 dígitos preenchidos com zero
"""

# ========================================
# EXERCÍCIO 4 - DIFÍCIL
# ========================================

"""
Exercício 4 - Difícil

Mostre o número -42 formatado com:
1) 6 espaços
2) Preenchido com zeros
3) Forçando o sinal antes dos zeros
"""

# ========================================
# GABARITO
# ========================================

# Exercício 1 - Fácil
# valor = 50
# print(f'{valor:<5}')        # Alinhado à esquerda em 5 espaços

# Exercício 2 - Médio
# preco = 1234.5678
# print(f'{preco:.2f}')       # Duas casas decimais
# print(f'{preco:,.2f}')      # Separador de milhar
# print(f'{preco:+,.2f}')     # Sempre mostra o sinal

# Exercício 3 - Difícil
# print(f'{255:x}')           # Hexadecimal minúsculo
# print(f'{255:X}')           # Hexadecimal maiúsculo
# print(f'{255:06X}')         # 6 dígitos com zeros

# Exercício 4 - Difícil
# print(f'{-42:6}')           # 6 espaços
# print(f'{-42:06}')          # Preenchido com zeros
# print(f'{-42:0=6}')         # Sinal antes dos zeros
