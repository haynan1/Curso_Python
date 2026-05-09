# Aula 69 - VALIDAÇÃO DE CPF COM TRATAMENTO DE ENTRADA

## Fonte

- Python editável: `conteudos/secao_3/69 - aula63.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/69 - aula63.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/06 - Projeto CPF|Projeto CPF]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[68 - aula62.2 - VALIDAÇÃO DE CPF (CÁLCULO DOS DÍGITOS)|Aula 68]]

## Ideia central

Limpa → Valida sequência → Calcula → Compara

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Agora você evoluiu o código adicionando tratamento de entrada — isso é MUITO importante.

Vamos entender os novos pontos:

----------------------------------------
🔹 LIMPEZA DO CPF (REGEX)
----------------------------------------

Você usou:

re.sub(r'[^0-9]', '', entrada)

Isso significa:
- Remove tudo que NÃO for número
- Deixa apenas os dígitos

Exemplo:
'746.824.890-70' → '74682489070'

----------------------------------------
🔹 VALIDAÇÃO DE SEQUÊNCIA
----------------------------------------

entrada == entrada[0] * len(entrada)

Isso verifica se todos os caracteres são iguais:

Ex:
'11111111111' → inválido
'00000000000' → inválido

⚠️ OBS:
O ideal seria validar usando o CPF LIMPO, não a entrada original.

----------------------------------------
🔹 CÁLCULO DOS DÍGITOS
----------------------------------------

Você aplicou corretamente:

✔ Primeiro dígito (peso 10 → 2)
✔ Segundo dígito (peso 11 → 2)
✔ Regra do resto da divisão por 11

----------------------------------------
🔹 VALIDAÇÃO FINAL
----------------------------------------

Compara:

cpf_digitado == cpf_calculado

Se forem iguais → CPF válido

----------------------------------------
🔹 POSSÍVEL...
