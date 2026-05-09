# Aula 06 - Tipo de Dado Booleano (bool) e Operador de Igualdade (==)

## Fonte

- Python editável: `conteudos/secao_3/06 - aula05.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/06 - aula05.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[05 - aula04 - TIPOS NUMÉRICOS- INT E FLOAT NO PYTHON|Aula 05]]
- Próxima aula: [[07 - aula06 - CONVERSÃO DE TIPOS EM PYTHON|Aula 07]]

## Ideia central

Boolean só tem duas portas:
ou é Verdade (True) ou é Falso (False).

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O tipo de dado bool (booleano) é utilizado quando fazemos
uma pergunta ao programa.

Toda pergunta lógica só pode ter duas respostas possíveis:
True  -> Verdadeiro
False -> Falso

Em programação, usamos operadores para fazer perguntas.
Esses operadores são chamados de operadores lógicos ou relacionais.

Um dos mais importantes é:

==  (operador de igualdade)

Ele pergunta:
"Um valor é igual ao outro?"

Exemplo lógico:
10 == 10  → True  (porque são iguais)
10 == 11  → False (porque são diferentes)

Quando fazemos uma comparação usando ==,
o resultado da expressão sempre será do tipo bool.

Podemos verificar o tipo usando a função type().

Exemplo:
type(True)
type(False)
type(10 == 10)

Todos esses retornam:
<class 'bool'>

Isso significa que o resultado de uma comparação
sempre será um valor booleano.
