# Aula 31 - CONSTANTES, LEGIBILIDADE E COMPLEXIDADE

## Fonte

- Python editável: `conteudos/secao_3/31 - aula30.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/31 - aula30.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/05 - Strings e Dados|Strings, formatação e validação inicial]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[30 - aula29 - INTRODUÇÃO AO TRY - EXCEPT|Aula 30]]
- Próxima aula: [[32 - aula31 - FLAG (BANDEIRA), NONE, IS, IS NOT E ID|Aula 32]]

## Ideia central

Constante é regra fixa.
Código limpo simplifica.
Menos condição, menos confusão.
Legibilidade é evolução.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

🔎 O QUE É UMA CONSTANTE?

Em Python não existe uma palavra reservada chamada "constante",
mas por convenção usamos LETRAS MAIÚSCULAS para representar valores
que NÃO DEVEM MUDAR durante a execução do programa.

Exemplo:
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

Esses valores representam regras fixas do sistema.

----------------------------------------

🔎 POR QUE USAR CONSTANTES?

1) Evita números mágicos espalhados pelo código
2) Facilita manutenção
3) Aumenta legibilidade
4) Deixa claro o propósito do valor

----------------------------------------

🔎 COMPLEXIDADE EM CONDIÇÕES

Quando colocamos muitas condições dentro de um único if,
o código fica difícil de entender.

Exemplo ruim:
if velocidade > 60 and local >= 99 and local <= 101:

Melhor prática:
Criar variáveis booleanas com nomes claros:

vel_carro_pass_radar_1
carro_passou_radar_1
carro_multado_radar_1

Isso deixa o código:
- Mais legível
- Mais organizado
- Mais fácil de testar
- Mais fácil de manter

----------------------------------------

🔎 IDEIA PRINCIPAL

Divida sua lógica em partes pequenas.
Dê nomes claros.
Evite if gigantes.
Deixe o código "explicativo".

Código bom parece texto.
