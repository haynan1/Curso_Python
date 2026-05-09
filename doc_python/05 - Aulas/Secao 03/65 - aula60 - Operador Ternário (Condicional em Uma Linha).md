# Aula 65 - Operador Ternário (Condicional em Uma Linha)

## Fonte

- Python editável: `conteudos/secao_3/65 - aula60.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/65 - aula60.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/06 - Projeto CPF|Projeto CPF]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[64 - aula59 - Desempacotamento com - (Unpacking)|Aula 64]]
- Próxima aula: [[66 - aula61 - Cálculo do Primeiro Dígito Verificador do CPF|Aula 66]]

## Ideia central

"Se for verdade, vai pra esquerda; senão, vai pra direita."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

📌 O QUE É O OPERADOR TERNÁRIO?

O operador ternário é uma forma curta de escrever um if/else em uma única linha.

Sintaxe:

<valor_se_verdadeiro> if <condicao> else <valor_se_falso>

--------------------------------------------------

📌 EXEMPLO SIMPLES

condicao = True

resultado = 'Sim' if condicao else 'Não'

Equivalente a:

if condicao:
    resultado = 'Sim'
else:
    resultado = 'Não'

--------------------------------------------------

📌 EXEMPLO DO SEU CÓDIGO

print('Valor' if False else 'Outro valor' if False else 'Fim')

Agora vamos entender passo a passo.

--------------------------------------------------

📌 COMO O PYTHON LÊ ISSO?

Quando há mais de um ternário, o Python resolve da direita para a esquerda.

Ou seja, ele interpreta assim:

print(
    'Valor' if False else (
        'Outro valor' if False else 'Fim'
    )
)

--------------------------------------------------

📌 RESOLUÇÃO PASSO A PASSO

1. Primeiro resolve:
   'Outro valor' if False else 'Fim'

→ Como é False:
→ Resultado: 'Fim'

2. Agora fica:

'Valor' if False else 'Fim'

→ Como é False:
→ Resultado final: 'Fim'

--------------------------------------------------

📌 RESULTADO...
