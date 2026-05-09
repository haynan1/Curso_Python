# Aula 08 - VARIÁVEIS EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/08 - aula07.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/08 - aula07.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[07 - aula06 - CONVERSÃO DE TIPOS EM PYTHON|Aula 07]]
- Próxima aula: [[09 - aula08 - VARIÁVEIS + CÁLCULOS + EXIBIÇÃO FORMATADA|Aula 09]]

## Ideia central

"Variável guarda.
= atribui.
E o nome explica o que possui."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O QUE É UMA VARIÁVEL?

Uma variável é um espaço na memória do computador
que recebe um nome para armazenar um valor.

Exemplo:
nome = "Haynan"

Aqui:
nome → é o identificador (nome da variável)
= → operador de atribuição
"Haynan" → valor armazenado

IMPORTANTE:
O sinal de = NÃO significa igualdade matemática.
Ele significa: RECEBE.

REGRAS DE NOMES (PEP8):
- Letras minúsculas
- Pode usar números
- Pode usar underline _
- Não pode começar com número

Exemplo válido:
nome_completo
idade_usuario
valor1

Exemplo inválido:
1nome
nome-completo

POR QUE USAMOS VARIÁVEIS?

Para evitar repetição de código.

No arquivo aula7.py vemos:

int("1")
Depois foi criada a variável:
int_um = int("1")

Assim não precisamos repetir int("1") várias vezes.

TIPOS OBSERVADOS NO ARQUIVO:

str  → "Haynan"
int  → 20
bool → idade >= 18

O operador >= significa:
"maior ou igual"

idade >= 18
Retorna True ou False.

Fluxo mental:

Variável = valor
Expressões podem ser armazenadas
Comparações retornam booleanos
