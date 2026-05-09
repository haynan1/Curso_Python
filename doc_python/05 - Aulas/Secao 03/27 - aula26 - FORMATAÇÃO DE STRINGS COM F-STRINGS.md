# Aula 27 - FORMATAÇÃO DE STRINGS COM F-STRINGS

## Fonte

- Python editável: `conteudos/secao_3/27 - aula26.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/27 - aula26.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Strings, formatação e validação inicial]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[26 - aula25 - INTERPOLAÇÃO DE STRINGS COM %|Aula 26]]
- Próxima aula: [[28 - aula27 - FATIAMENTO DE STRINGS (SLICING)|Aula 28]]

## Ideia central

"Formato tem ordem: valor, dois pontos, regras e exibição."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

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

Ordem da...
