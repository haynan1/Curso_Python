# Aula 16 - FUNÇÃO input() E CONVERSÃO DE TIPOS

## Fonte

- Python editável: `conteudos/secao_3/16 - aula15.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/16 - aula15.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[15 - aula14 - FORMATAÇÃO DE STRINGS COM .format()|Aula 15]]
- Próxima aula: [[17 - aula16 - CONDICIONAIS NO PYTHON (if - elif - else)|Aula 17]]

## Ideia central

"Input sempre devolve texto.
Se quiser número, converta certo."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

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
