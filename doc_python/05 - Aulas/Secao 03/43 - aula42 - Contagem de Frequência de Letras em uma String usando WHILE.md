# Aula 43 - Contagem de Frequência de Letras em uma String usando WHILE

## Fonte

- Python editável: `conteudos/secao_3/43 - aula42.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/43 - aula42.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[42 - aula41 - WHILE + ELSE EM PYTHON|Aula 42]]
- Próxima aula: [[44 - aula43 - WHILE E FOR EM PYTHON (LAÇOS DE REPETIÇÃO)|Aula 44]]

## Ideia central

Percorra, conte, compare e guarde.
Quem aparece mais, vence no final.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Este algoritmo tem como objetivo descobrir qual letra aparece mais vezes
dentro de uma frase.

Para isso usamos:

1) Uma STRING (frase ou texto)
2) Um LOOP WHILE para percorrer cada caractere
3) O método count() para contar quantas vezes a letra aparece
4) Variáveis de controle para guardar o maior valor encontrado

Estrutura lógica do algoritmo:

PASSO 1
Criamos uma variável de índice que começa em 0.
Esse índice será usado para percorrer cada caractere da string.

PASSO 2
Enquanto o índice for menor que o tamanho da frase (len(frase)),
continuamos o loop.

PASSO 3
Pegamos o caractere atual da frase usando:

frase[indice]

PASSO 4
Ignoramos espaços usando:

if letra == " ":
    continue

Isso evita contar espaços como caracteres relevantes.

PASSO 5
Usamos:

frase.count(letra)

para descobrir quantas vezes aquela letra aparece na frase.

PASSO 6
Comparamos essa quantidade com o maior valor já encontrado.

Se for maior, atualizamos:

- maior quantidade
- letra mais frequente

PASSO 7
Incrementamos o índice para continuar percorrendo a frase.

PASSO 8
Ao final do loop teremos armazenado:

- a letra que mais apareceu
- quantas vezes ela apareceu

IMPORTANTE SOBRE EFICIÊNCIA

Este...
