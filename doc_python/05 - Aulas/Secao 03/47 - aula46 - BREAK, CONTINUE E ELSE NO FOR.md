# Aula 47 - BREAK, CONTINUE E ELSE NO FOR

## Fonte

- Python editável: `conteudos/secao_3/47 - aula46.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/47 - aula46.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[46 - aula45 - ITERÁVEIS E ITERADORES EM PYTHON|Aula 46]]
- Próxima aula: [[48 - aula47 - JOGO DA PALAVRA SECRETA (FORCA SIMPLES)|Aula 48]]

## Ideia central

Continue pula.
Break interrompe.
Else só roda se NÃO quebrar.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Vamos entender o comportamento do seu código:

🔹 CONTINUE
Quando o Python encontra "continue", ele:
- PULA o restante do bloco atual
- Vai para a próxima iteração do loop

No seu código:
if i == 2:
    continue

👉 Ou seja:
Quando i for 2, ele NÃO executa o for interno.

---

🔹 BREAK
Quando o Python encontra "break", ele:
- INTERROMPE completamente o loop

No seu código:
if i == 8:
    break

👉 Ou seja:
Quando i for 8, o loop para imediatamente.

---

🔹 ELSE NO FOR
O else no for é pouco conhecido.

Ele SÓ executa se o loop terminar naturalmente (sem break).

✔ Terminou normal → executa o else
❌ Teve break → NÃO executa o else

---

🔹 FLUXO DO SEU CÓDIGO

Loop de i: 0 até 9

i = 0 → roda normal
i = 1 → roda normal
i = 2 → cai no continue (pula o resto)
i = 3 → roda normal
i = 4 → roda normal
i = 5 → roda normal
i = 6 → roda normal
i = 7 → roda normal
i = 8 → cai no break → PARA TUDO

Como teve break:
👉 O else NÃO executa

---

🔹 FOR INTERNO

for j in range(1,3):

👉 j vai ser:
1 e 2

Então cada i válido imprime:
(i, 1) e (i, 2)

---

Resumo final:

continue → ignora o resto da rodada
break → mata o loop
else → só roda se NÃO houver break
