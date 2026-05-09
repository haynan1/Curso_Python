# Aula 19 - FLUXO DE EXECUÇÃO EM CONDICIONAIS

## Fonte

- Python editável: `conteudos/secao_3/19 - aula18.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/19 - aula18.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/02 - Decisões|Decisões]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[18 - aula17 - CONDICIONAIS NO PYTHON (if - elif - else)|Aula 18]]
- Próxima aula: [[20 - aula19 - OPERADORES DE COMPARAÇÃO (RELACIONAIS)|Aula 20]]

## Ideia central

O Python desce lendo.
Achou True? Para de escolher.
Novo if? Novo teste.
Fora do bloco? Executa sempre.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

O arquivo enviado mostra dois pontos extremamente importantes
sobre estruturas condicionais no Python:

1) Cadeia de if / elif / else
2) Blocos independentes de if

PARTE 1 — Cadeia de decisão

Quando usamos:

if condicao1:
elif condicao2:
elif condicao3:
else:

O Python executa de cima para baixo.

Ele testa condicao1.
Se for True → executa e IGNORA todo o resto.
Se for False → testa a próxima.

Importante:
Mesmo que existam várias condições True,
apenas a primeira verdadeira será executada.

No código enviado:

condicao1 = True
condicao2 = False
condicao3 = True

Mesmo condicao3 sendo True,
ela nunca executa,
porque condicao1 já era verdadeira.

Isso se chama:
Fluxo de decisão sequencial com parada na primeira verdade.

PARTE 2 — Novo bloco if

Depois da estrutura principal,
existe:

if 10 == 10:
    print("Outro bloco de if")

Isso é um NOVO bloco independente.
Não tem relação com o primeiro.

Ou seja:
Um programa pode ter vários if separados.

PARTE 3 — Código fora do if

print("Fora do if")

Essa linha sempre executa.
Ela não depende de condição.

Regra de ouro:
Indentação define pertencimento ao bloco.
