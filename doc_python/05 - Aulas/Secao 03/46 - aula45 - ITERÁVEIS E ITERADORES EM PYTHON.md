# Aula 46 - ITERÁVEIS E ITERADORES EM PYTHON

## Fonte

- Python editável: `conteudos/secao_3/46 - aula45.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/46 - aula45.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[45 - aula44 - FOR + RANGE EM PYTHON|Aula 45]]
- Próxima aula: [[47 - aula46 - BREAK, CONTINUE E ELSE NO FOR|Aula 47]]

## Ideia central

Iterável é a coleção.
Iterador é quem faz a entrega.
next pega o próximo.
iter cria o entregador.

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Vamos entender de forma simples:

🔹 ITERÁVEL
É qualquer objeto que pode ser percorrido.
Exemplos: string, lista, tupla, range...

Exemplo:
texto = "Haynan"

Aqui, "texto" é ITERÁVEL porque podemos percorrer letra por letra.

---

🔹 ITERADOR
É o objeto que sabe como percorrer o iterável.
Ele entrega UM valor por vez.

Criamos um iterador com:
iter(iterável)

Exemplo:
iterador = iter(texto)

---

🔹 next()
Serve para pegar o próximo valor do iterador.

Exemplo:
next(iterador)

Ele vai retornando letra por letra.

---

🔹 StopIteration
Quando os valores acabam, o Python lança esse erro.

Por isso usamos try/except.

---

🔹 FOR por trás dos panos

O for faz EXATAMENTE isso:

1. Cria um iterador
2. Chama next()
3. Para quando dá StopIteration

Ou seja:
for letra in texto:

é equivalente ao while com next()

---

Resumo mental:

for = automático
while + next = manual
