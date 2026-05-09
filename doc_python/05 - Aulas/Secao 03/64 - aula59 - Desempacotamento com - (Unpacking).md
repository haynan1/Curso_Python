# Aula 64 - Desempacotamento com * (Unpacking)

## Fonte

- Python editável: `conteudos/secao_3/64 - aula59.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/64 - aula59.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Dados, strings e estruturas]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[63 - aula58 - Interpretador do Python + Zen of Python|Aula 63]]
- Próxima aula: [[65 - aula60 - Operador Ternário (Condicional em Uma Linha)|Aula 65]]

## Ideia central

"O asterisco abre caixas: ele espalha valores onde você quiser."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

📌 O QUE É DESEMPACOTAMENTO?

Desempacotamento (unpacking) é quando você "abre" uma estrutura
(iterável como lista, tupla ou string) e usa seus valores separadamente.

O operador responsável por isso é o * (asterisco).

--------------------------------------------------

📌 EXEMPLO SIMPLES

lista = [1, 2, 3]

print(*lista)

Saída:
1 2 3

Ou seja:
O * tira os elementos de dentro da lista e passa um por um.

--------------------------------------------------

📌 FUNCIONA COM:

✔ Listas
✔ Tuplas
✔ Strings
✔ Qualquer iterável

Exemplo com string:

string = "ABC"
print(*string)

Saída:
A B C

--------------------------------------------------

📌 USO EM FUNÇÕES

A função print aceita vários argumentos separados por vírgula.

Então:

print(*lista)

é equivalente a:

print(1, 2, 3)

--------------------------------------------------

📌 PARÂMETRO sep

sep = separador entre os valores

Exemplo:

print(*lista, sep='-')

Saída:
1-2-3

--------------------------------------------------

📌 CASO DO SEU CÓDIGO

Você tem:

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda']
]

E faz:

print(*salas, sep='\n')

O que acontece:

1. O * desempacota a lista principal
2. Cada...
