# Aula 48 - JOGO DA PALAVRA SECRETA (FORCA SIMPLES)

## Fonte

- Python editável: `conteudos/secao_3/48 - aula47.py`
- Markdown estruturado: `conteudos/secao_3/aulas_estruturadas/48 - aula47.md`

## Relações

- Seção: [[01 - Seções/Seção 03 - Lógica Python|Seção 03 - Lógica Python]]
- Bloco: [[02 - Blocos/03 - Repetições|Repetições]]
- Índice: [[Índice da Seção 03]]
- Aula anterior: [[47 - aula46 - BREAK, CONTINUE E ELSE NO FOR|Aula 47]]
- Próxima aula: [[49 - aula48.1 - LISTAS EM PYTHON (TIPO LIST)|Aula 49]]

## Ideia central

"Testa letra, guarda acerto, monta palavra e repete até ganhar."

## Pontos para revisar

- Conferir se o arquivo Python executa sem erro.
- Conferir se a explicação está clara para aluno iniciante.
- Conferir se há exercício e gabarito quando fizer sentido.
- Atualizar o README público se esta aula mudar a trilha.

## Conteúdo extraído

Este exercício implementa um jogo simples parecido com o da forca.

Fluxo do programa:

1. Definimos uma palavra secreta.
2. O usuário digita uma letra por vez.
3. Verificamos:
   - Se a letra existe na palavra secreta → guardamos como acerto.
   - Se não existe → apenas ignoramos (mas contamos tentativa).
4. Montamos uma nova string:
   - Letras corretas aparecem
   - Letras não descobertas aparecem como "*"
5. O jogo continua até o usuário acertar toda a palavra.

Conceitos importantes usados:

- while True → loop infinito até condição de parada
- input() → entrada de dados do usuário
- if / else → tomada de decisão
- for → percorrer cada letra da palavra
- string → manipulação de texto
- acumulador → guardar letras corretas

Além disso:
- Contamos o número de tentativas
- Validamos se o usuário digitou apenas 1 letra
