# Aula 07 - CONVERSÃO DE TIPOS EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/07 - aula06.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/07 - aula06.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[06 - aula05 - Tipo de Dado Booleano (bool) e Operador de Igualdade (==)|Aula 06]]
- Próxima aula: [[08 - aula07 - VARIÁVEIS EM PYTHON|Aula 08]]

## Ideia central

"Se o tipo não combina, o Python reclama.
Converta primeiro, depois calcula."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

CONVERSÃO DE TIPOS (Type Casting / Type Conversion)

Converter tipos é o ato de transformar um dado de um tipo para outro.

Em Python, os tipos primitivos imutáveis mais comuns são:

- str  → texto
- int  → número inteiro
- float → número decimal
- bool → verdadeiro ou falso

Por que isso é importante?

Porque o Python não permite misturar tipos incompatíveis em certas operações.

Exemplo:
int + int → soma
str + str → concatenação
int + str → ERRO

O Python pode fazer dois tipos de conversão:

1) Conversão explícita (manual)
   Quando usamos funções como:
   int()
   float()
   str()
   bool()

2) Coerção (automática)
   Quando o Python ajusta o tipo sozinho.
   Exemplo:
   float + int → resultado será float

Exemplos importantes do seu código original:

1 + 1 → soma = 2
"a" + "b" → concatenação = "ab"

int("1") → transforma texto em número
float("1.5") → transforma texto decimal em número decimal

bool(" ") → retorna True
Qualquer string NÃO vazia é considerada True.
Somente:
"" (string vazia)
0
0.0
None
False
São considerados False.

str(11) + "b" → converte 11 para texto e concatena.

Resumo mental:

NÚMERO + NÚMERO → soma
TEXTO + TEXTO → junta
MISTUROU? → converta antes
