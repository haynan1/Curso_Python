# Aula 59 - Lista Interativa com Tratamento de Erros

## Fonte

- Python editável: `conteudos/secao_3/59 - aula54.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/59 - aula54.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/04 - Coleções|Coleções]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[58 - aula53 - enumerate() - Índice + Valor ao mesmo tempo|Aula 58]]
- Próxima aula: [[60 - aula55 - Imprecisão de Ponto Flutuante e Decimal|Aula 60]]

## Ideia central

"Antes de apagar, verifique; antes de usar, valide."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Este programa implementa uma lista de compras interativa no terminal.

O usuário pode:
- Inserir valores na lista
- Apagar valores pelo índice
- Listar todos os itens

O ponto mais importante deste código é o TRATAMENTO DE ERROS.

Por que isso é necessário?
Quando trabalhamos com listas, podemos tentar acessar posições que não existem,
o que gera um erro chamado IndexError.

Também podemos ter erro ao converter texto para número (ValueError).

Para evitar que o programa "quebre", usamos o bloco try/except.

Estrutura:

try:
    código que pode dar erro
except TipoDeErro:
    o que fazer se der erro

Além disso, usamos:
- append(): para adicionar itens
- del: para remover itens pelo índice
- enumerate(): para mostrar índice + valor

Também usamos len(lista) para verificar se a lista está vazia.

Esse tipo de programa é muito importante para treinar:
- lógica
- controle de fluxo
- validação de dados
