# Aula 30 - INTRODUÇÃO AO TRY / EXCEPT

## Fonte

- Python editável: `conteudos/secao_3/30 - aula29.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/30 - aula29.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Strings, formatação e validação inicial]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[29 - aula28 - VALIDAÇÃO DE DADOS + STRINGS + CONDIÇÕES|Aula 29]]
- Próxima aula: [[31 - aula30 - CONSTANTES, LEGIBILIDADE E COMPLEXIDADE|Aula 31]]

## Ideia central

TRY tenta.
EXCEPT trata.
Se der erro, o programa não mata.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O que é try/except?

Em Python, usamos try/except para tratar erros.

Quando o programa executa um código que pode dar problema,
usamos:

try -> tentar executar algo
except -> executar algo caso dê erro

Isso evita que o programa "quebre".

Exemplo clássico de erro:

int('a')

Isso gera um ValueError porque não é possível converter
uma letra em número.

Sem tratamento de erro:
O programa para de funcionar.

Com try/except:
O programa continua funcionando normalmente.

Estrutura básica:

try:
    código que pode dar erro
except:
    código executado se der erro

No seu exemplo:

O usuário digita algo.
Tentamos converter para float.
Se conseguir -> mostramos o dobro.
Se não conseguir -> avisamos que não é número.

IMPORTANTE:
Nunca deixe o except vazio em projetos reais.
O ideal é especificar o tipo de erro:

except ValueError:

Mas para iniciantes, entender o conceito já é o primeiro passo.
