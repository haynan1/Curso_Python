# Aula 26 - INTERPOLAÇÃO DE STRINGS COM %

## Fonte

- Python editável: `conteudos/secao_3/26 - aula25.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/26 - aula25.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Strings, formatação e validação inicial]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[25 - aula24 - OPERADORES in E not in (STRINGS)|Aula 25]]
- Próxima aula: [[27 - aula26 - FORMATAÇÃO DE STRINGS COM F-STRINGS|Aula 27]]

## Ideia central

% formata e organiza:
%s texto,
%d número inteiro,
%f número decimal,
%x hexadecimal.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

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
porque pedimos 2 casas...
