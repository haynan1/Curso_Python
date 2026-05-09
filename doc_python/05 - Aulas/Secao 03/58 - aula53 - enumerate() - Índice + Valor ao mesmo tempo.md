# Aula 58 - enumerate() - Índice + Valor ao mesmo tempo

## Fonte

- Python editável: `conteudos/secao_3/58 - aula53.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/58 - aula53.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/04 - Coleções|Coleções]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[57 - aula52 - Tuplas em Python (Listas Imutáveis)|Aula 57]]
- Próxima aula: [[59 - aula54 - Lista Interativa com Tratamento de Erros|Aula 59]]

## Ideia central

"enumerate junta índice e valor num só passo."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O enumerate() é uma função do Python usada para percorrer iteráveis
(como listas, tuplas, strings), retornando:

👉 índice + valor ao mesmo tempo

Estrutura:

for indice, valor in enumerate(lista):
    ...

Cada item gerado pelo enumerate é uma tupla:

(indice, valor)

----------------------------------------

SEU CÓDIGO

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

Resultado interno do enumerate(lista):

[(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]

----------------------------------------

FORMA MAIS COMUM (DESEMPACOTANDO)

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

Aqui:
- indice → posição
- nome → valor da lista
- lista[indice] → mesma coisa que nome

Ou seja:
nome == lista[indice]

----------------------------------------

FORMA 2 (SEM DESEMPACOTAR)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

Aqui você recebe a tupla inteira e depois separa.

----------------------------------------

FORMA 3 (LOOP DENTRO DA TUPLA)

for tupla_enumerada in enumerate(lista):
    for valor in tupla_enumerada:
        print(valor)

Aqui você percorre cada tupla (índice e valor...
