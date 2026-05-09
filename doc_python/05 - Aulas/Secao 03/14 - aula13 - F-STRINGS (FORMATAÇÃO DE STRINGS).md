# Aula 14 - F-STRINGS (FORMATAÇÃO DE STRINGS)

## Fonte

- Python editável: `conteudos/secao_3/14 - aula13.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/14 - aula13.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/01 - Fundamentos|Fundamentos]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[13 - aula12 - CÁLCULO DE IMC + USO DE EXPRESSÕES|Aula 13]]
- Próxima aula: [[15 - aula14 - FORMATAÇÃO DE STRINGS COM .format()|Aula 15]]

## Ideia central

"Colocou f na frente?
Chaves pegam a variável automaticamente."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O que é f-string?

F-string é uma forma moderna e mais organizada
de formatar textos no Python.

Ela permite inserir variáveis diretamente
dentro da string usando { }.

Sintaxe:

f"texto {variavel}"

IMPORTANTE:
A variável precisa já existir antes da f-string.
Senão, dará erro.

Comparação:

FORMA ANTIGA (aula 12):
print(nome, "tem", altura, "de altura...")

FORMA COM F-STRING (aula 13):
f"{nome} tem {altura} de altura..."

Muito mais limpo e organizado.

No arquivo temos:

linha_1 = f"{nome}, tem {altura} de altura pesa {peso} kilos e seu IMC é {imc}"

O que acontece?

1) O Python identifica o f antes da string.
2) Ele procura tudo que está entre { }.
3) Substitui pelo valor da variável.

Vantagens da f-string:

• Código mais legível
• Mais organizado
• Permite formatar números
• Permite colocar expressões dentro das chaves

Exemplo com expressão:

f"{peso / (altura ** 2)}"

Regra mental:

f + "texto {variavel}" = texto formatado automaticamente
