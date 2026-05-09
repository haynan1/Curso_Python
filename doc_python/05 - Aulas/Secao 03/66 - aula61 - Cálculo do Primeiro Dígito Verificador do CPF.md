# Aula 66 - Cálculo do Primeiro Dígito Verificador do CPF

## Fonte

- Python editável: `conteudos/secao_3/66 - aula61.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/66 - aula61.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/06 - Projeto CPF|Projeto CPF]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[65 - aula60 - Operador Ternário (Condicional em Uma Linha)|Aula 65]]
- Próxima aula: [[67 - aula62.1 - Cálculo do Segundo Dígito Verificador do CPF|Aula 67]]

## Ideia central

"Multiplica, soma, vezes 10, divide por 11 — passou de 9, vira zero então."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

📌 O QUE É O DÍGITO VERIFICADOR DO CPF?

O CPF possui 11 dígitos:
- Os 9 primeiros são o número base
- Os 2 últimos são dígitos verificadores

Esses dígitos servem para validar se o CPF é verdadeiro.

--------------------------------------------------

📌 PASSO A PASSO DO PRIMEIRO DÍGITO

Dado:
CPF: 746.824.890-70
Base: 746824890

1. Pegamos os 9 primeiros dígitos

2. Criamos uma contagem regressiva de 10 até 2

3. Multiplicamos cada dígito pelo peso correspondente:

   7 × 10 = 70
   4 × 9  = 36
   6 × 8  = 48
   8 × 7  = 56
   2 × 6  = 12
   4 × 5  = 20
   8 × 4  = 32
   9 × 3  = 27
   0 × 2  = 0

4. Somamos tudo:
   70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

5. Multiplicamos por 10:
   301 × 10 = 3010

6. Pegamos o resto da divisão por 11:
   3010 % 11 = 7

7. Regra final:
   - Se resultado > 9 → vira 0
   - Senão → mantém o valor

✔ Resultado final: 7

--------------------------------------------------

📌 RESUMO

- Multiplica pelos pesos (10 até 2)
- Soma tudo
- Multiplica por 10
- Faz % 11
- Ajusta (se > 9 → 0)

Esse resultado é o primeiro dígito verificador.
