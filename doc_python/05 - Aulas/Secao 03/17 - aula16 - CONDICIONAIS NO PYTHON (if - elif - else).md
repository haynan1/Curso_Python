# Aula 17 - CONDICIONAIS NO PYTHON (if / elif / else)

## Fonte

- Python editável: `conteudos/secao_3/17 - aula16.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/17 - aula16.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/02 - Decisões|Decisões]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[16 - aula15 - FUNÇÃO input() E CONVERSÃO DE TIPOS|Aula 16]]
- Próxima aula: [[18 - aula17 - CONDICIONAIS NO PYTHON (if - elif - else)|Aula 18]]

## Ideia central

SE for verdadeiro, EXECUTA.
SE NÃO, testa outra condição.
SE NADA for verdadeiro, executa o FINAL.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Estruturas Condicionais no Python

As estruturas condicionais permitem que o programa tome decisões.

Elas funcionam com base em expressões booleanas.
Uma expressão booleana só pode resultar em:

True  (Verdadeiro)
False (Falso)

Estrutura básica:

if condição:
    bloco de código

elif outra_condição:
    outro bloco

else:
    bloco final

Regras importantes:

1) O IF sempre inicia a estrutura.
2) O ELIF é opcional e pode existir várias vezes.
3) O ELSE é opcional e executa quando nenhuma condição anterior for verdadeira.
4) A indentação (espaço antes do código) é obrigatória.
5) Fora do bloco, o código volta ao fluxo normal.

No arquivo analisado, o programa:
- Recebe uma entrada do usuário.
- Compara essa entrada com textos específicos.
- Executa uma ação dependendo da resposta.
- Depois imprime uma mensagem fora da estrutura condicional.

Isso mostra claramente a diferença entre:
Código dentro do bloco condicional
Código fora do bloco condicional
