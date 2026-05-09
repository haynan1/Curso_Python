# Aula 33 - ESTRUTURAS CONDICIONAIS E TRATAMENTO DE ERROS

## Fonte

- Python editável: `conteudos/secao_3/33 - aula32.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/33 - aula32.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Strings, formatação e validação inicial]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[32 - aula31 - FLAG (BANDEIRA), NONE, IS, IS NOT E ID|Aula 32]]
- Próxima aula: [[34 - aula33 - https---docs.python.org-pt-br-3-library-stdtypes.html|Aula 34]]

## Ideia central

SE decide.
ELIF ajusta.
ELSE resolve.
TRY testa.
EXCEPT protege.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

As estruturas condicionais permitem que o programa tome decisões.

Em Python utilizamos:

- if → executa um bloco se a condição for verdadeira
- elif → testa uma nova condição caso a anterior seja falsa
- else → executa caso nenhuma condição anterior seja verdadeira

Exemplo lógico:
Se a condição for verdadeira → faça algo.
Senão → faça outra coisa.

Operadores importantes:
==  igual
!=  diferente
>   maior
<   menor
>=  maior ou igual
<=  menor ou igual
%   resto da divisão (muito usado para verificar par ou ímpar)

Número par:
Um número é par quando o resto da divisão por 2 é igual a 0.
Exemplo:
10 % 2 == 0 → par

Tratamento de erros:

try:
    tenta executar um código
except:
    executa caso ocorra erro

Isso evita que o programa quebre caso o usuário digite algo inválido.

Funções importantes:

input() → recebe dados do usuário (sempre como texto)
int() → converte texto para número inteiro
len() → retorna o tamanho de um texto
isdigit() → verifica se a string contém apenas números positivos
