# Aula 32 - FLAG (BANDEIRA), NONE, IS, IS NOT E ID

## Fonte

- Python editável: `conteudos/secao_3/32 - aula31.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/32 - aula31.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Strings, formatação e validação inicial]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[31 - aula30 - CONSTANTES, LEGIBILIDADE E COMPLEXIDADE|Aula 31]]
- Próxima aula: [[33 - aula32 - ESTRUTURAS CONDICIONAIS E TRATAMENTO DE ERROS|Aula 33]]

## Ideia central

Flag marca estado.
None marca ausência.
is compara identidade.
== compara valor.
id mostra identidade.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

📌 O que é uma FLAG (Bandeira)?

Uma "flag" é uma variável usada para marcar um estado.
Normalmente usamos valores booleanos (True ou False).

Exemplo mental:
condicao = False

Se algo acontecer:
condicao = True

Ela serve para indicar se algo ocorreu ou não.

📌 O que é None?

None significa "ausência de valor".
Não é 0.
Não é False.
Não é string vazia.
É um tipo especial que indica que a variável não aponta para nenhum valor ainda.

Exemplo:
passou_no_if = None

Isso significa:
"Ainda não sabemos se passou no if."

📌 Diferença entre == e is

==  → Compara VALOR
is  → Compara IDENTIDADE (mesmo objeto na memória)

Exemplo:
a = 10
b = 10

a == b → True (mesmo valor)
a is b → Pode ser True ou False dependendo da otimização

Já com None:
Sempre use:

variavel is None
variavel is not None

Nunca use:
variavel == None  ❌

📌 Função id()

id(variavel) mostra o endereço (identidade) do objeto na memória.
É como perguntar:
"Quem você é na memória do Python?"

📌 Entendendo o seu código

Você criou:

condicao = False
passou_no_if = None

Depois:

if condicao:
    passou_no_if = True

Como condicao é False,
o bloco do if não executa.

Logo:
passou_no_if continua sendo None.

Depois você...
