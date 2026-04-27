# Lógica de programação básica

Curso inicial de Python para construir a base de raciocínio usada em qualquer programa: entrada, processamento, saída, variáveis, tipos de dados, decisões e repetições.

## Manutenção do repositório

- A estrutura do projeto está documentada em `docs/ESTRUTURA.md`.
- O fluxo para criar novas sessões está em `docs/GUIA_DE_ATUALIZACAO.md`.
- Modelos reutilizáveis ficam em `templates/`.
- Scripts utilitários ficam em `tools/`, fora das pastas de aula.

## Manual estrutural do curso

Este curso é renderizado no navegador a partir deste arquivo `README.md`.

A regra principal é simples:

- Cada título com `#` vira uma página no site.
- Cada subtítulo com `##` ou `###` vira item do índice da página atual.
- Blocos de código devem ficar entre três crases.
- A ordem das páginas no navegador segue a ordem em que aparecem neste arquivo.

Exemplo de nova página:

````md
# Aula 16 - Funções

Texto introdutório da aula.

## Objetivo da aula

- Entender para que servem funções.
- Criar funções simples.
- Reutilizar código.

## Exemplo

```python
def saudacao():
    print("Olá, Python")

saudacao()
```

## Exercícios

1. Crie uma função que mostre seu nome.
2. Crie uma função que some dois números.
````

Ao adicionar uma nova página, use sempre este padrão:

````md
# Aula ou Módulo - Nome do conteúdo

Introdução curta.

## Objetivo

- Objetivo 1
- Objetivo 2

## Explicação

Conteúdo didático.

## Exemplo

```python
# código aqui
```

## Exercícios

1. Exercício simples.
2. Exercício intermediário.
3. Exercício de revisão.
````

### Como organizar a trilha

Use `Aula` para conteúdos sequenciais menores.

```md
# Aula 17 - Parâmetros de funções
```

Use `Módulo` para blocos maiores de aprendizagem.

```md
# Módulo 13 - Funções em Python
```

Use `Projeto` quando o conteúdo juntar vários assuntos.

```md
# Projeto 2 - Sistema de cadastro simples
```

### Boas práticas para adicionar conteúdo

- Coloque uma introdução curta antes dos subtítulos.
- Explique primeiro o conceito, depois mostre o código.
- Use exemplos pequenos antes de exemplos completos.
- Termine cada página com exercícios.
- Evite colocar assuntos avançados antes da base necessária.
- Não use `#` dentro de blocos de código como título; dentro do código, `#` continua sendo comentário.

### Quando separar em vários arquivos

Enquanto o curso estiver pequeno ou médio, manter tudo no `README.md` é prático.

Quando o curso crescer muito, a melhor evolução será separar o conteúdo assim:

```text
README.md
conteudo/
  00-visao-geral.md
  01-logica-basica.md
  02-listas-tuplas.md
  03-funcoes.md
  04-projetos.md
```

Nesse formato, o site pode carregar cada arquivo sob demanda. Isso deixa o curso mais leve e mais fácil de manter.

Por enquanto, a estrutura atual é adequada: um único `README.md`, organizado por páginas usando títulos `#`.

## Objetivo da sessão

Ao final desta sessão, o aluno deve conseguir:

- Entender a diferença entre escrever código e documentar código.
- Exibir informações na tela com `print()`.
- Trabalhar com textos, números e valores booleanos.
- Criar variáveis com nomes claros.
- Fazer cálculos usando operadores aritméticos.
- Receber dados do usuário com `input()`.
- Converter tipos quando necessário.
- Comparar valores e tomar decisões com `if`, `elif` e `else`.
- Usar operadores lógicos como `and`, `or` e `not`.
- Repetir ações com `while`, `for` e `range()`.
- Resolver pequenos problemas juntando entrada, processamento e saída.

## Ordem cronológica de aprendizado

1. Primeiros passos e execução mental do código
2. Comentários e docstrings
3. Saída de dados com `print()`
4. Tipos primitivos: `str`, `int`, `float` e `bool`
5. Variáveis e atribuição
6. Operadores aritméticos e precedência
7. Strings, concatenação e f-strings
8. Entrada de dados com `input()`
9. Conversão de tipos
10. Comparações e valores booleanos
11. Condicionais com `if`, `elif` e `else`
12. Operadores lógicos
13. Laço de repetição `while`
14. Laço de repetição `for` e `range()`
15. Mini-projeto de fechamento

## Próximos módulos da trilha

Esta primeira sessão trabalha a lógica básica. Depois dela, a trilha continua com:

- Coleções: listas, tuplas, índices e matrizes
- Iteração com listas, `range()`, `len()` e `enumerate()`
- Empacotamento, desempacotamento e operador `*`
- Manipulação de strings com `split()`, `join()`, fatiamento e busca
- Tratamento de erros com `try` e `except`
- Precisão numérica com `round()` e `Decimal`
- Operador ternário
- Projetos práticos, incluindo validação e geração de CPF

Esses conteúdos fazem parte do curso, mas entram depois dos fundamentos para manter a aprendizagem em ordem.

---

# Aula 1 - Primeiros passos

Programar é escrever uma sequência de instruções para o computador executar.

Um programa básico costuma seguir esta lógica:

1. Entrada: dados que entram no programa.
2. Processamento: cálculos, comparações ou decisões.
3. Saída: resultado mostrado ao usuário.

Exemplo:

```python
nome = "Ana"
idade = 20

print("Nome:", nome)
print("Idade:", idade)
```

Neste exemplo:

- `"Ana"` e `20` são dados.
- `nome` e `idade` guardam os dados.
- `print()` mostra os resultados na tela.

## Ideia principal

Antes de pensar em código difícil, pense na pergunta:

> O que entra, o que o programa faz e o que deve sair?

---

# Aula 2 - Comentários e docstrings

Comentários são anotações ignoradas pelo Python. Eles ajudam a explicar partes do código.

```python
# Isto é um comentário
print("Olá, mundo")
```

Tudo que vem depois de `#` na mesma linha é ignorado pelo interpretador.

Docstrings são textos entre aspas triplas. Elas são usadas principalmente para documentar módulos, funções e classes.

```python
"""
Este programa mostra uma mensagem na tela.
"""

print("Bem-vindo ao Python")
```

## Diferença importante

- Comentário: começa com `#` e é ignorado pelo Python.
- Docstring: é uma string válida em Python, usada como documentação.

## Boa prática

Comente o motivo de uma decisão, não o óbvio.

Ruim:

```python
idade = 18  # cria idade com 18
```

Melhor:

```python
idade_minima = 18  # regra para permitir cadastro no sistema
```

## Exercícios

1. Crie um programa que mostre seu nome na tela e tenha um comentário explicando a finalidade do programa.
2. Escreva uma docstring no início de um arquivo explicando que o programa calcula a idade de uma pessoa.
3. Escreva três linhas de código com comentários laterais explicando o que cada linha representa.

---

# Aula 3 - Saída de dados com print()

A função `print()` mostra informações na tela.

```python
print("Python")
print(123)
print("Idade:", 25)
```

Quando passamos vários valores separados por vírgula, o Python coloca um espaço entre eles.

```python
print("Ana", "Silva", 30)
```

Saída:

```text
Ana Silva 30
```

## Parâmetro sep

O `sep` define o separador entre os valores.

```python
print("2026", "04", "27", sep="-")
```

Saída:

```text
2026-04-27
```

## Parâmetro end

O `end` define o que acontece no final do `print()`.

```python
print("Olá", end=" ")
print("mundo")
```

Saída:

```text
Olá mundo
```

## Exercícios

1. Mostre seu nome e sua idade usando dois `print()`.
2. Mostre dia, mês e ano separados por `/`.
3. Use `end` para mostrar duas palavras na mesma linha.
4. Mostre três informações diferentes no mesmo `print()`.

---

# Aula 4 - Tipos primitivos

Python trabalha com tipos de dados. Nesta sessão, os principais são:

- `str`: texto
- `int`: número inteiro
- `float`: número decimal
- `bool`: verdadeiro ou falso

```python
print(type("Python"))  # str
print(type(10))        # int
print(type(10.5))      # float
print(type(True))      # bool
```

## Strings

Strings são textos.

```python
nome = "Carlos"
frase = 'Python é uma linguagem de programação'
```

Você pode usar aspas simples ou duplas.

```python
print('Ele disse: "Olá"')
print("Python é 'simples' de ler")
```

## Inteiros e floats

```python
idade = 25
altura = 1.75
```

`idade` é `int`. `altura` é `float`.

## Booleanos

Booleanos representam respostas lógicas.

```python
maior_de_idade = True
usuario_bloqueado = False
```

## Exercícios

1. Crie uma variável de cada tipo: `str`, `int`, `float` e `bool`.
2. Use `type()` para conferir o tipo de cada variável.
3. Mostre na tela uma frase contendo seu nome e sua idade.
4. Crie uma variável chamada `aprovado` com valor booleano.

---

# Aula 5 - Variáveis e atribuição

Variáveis guardam valores na memória.

```python
nome = "Mariana"
idade = 28
altura = 1.68
```

O sinal `=` é o operador de atribuição. Ele atribui um valor a um nome.

```python
preco = 100
desconto = 20
preco_final = preco - desconto

print(preco_final)
```

## Regras e boas práticas

- Use letras minúsculas.
- Use `_` para separar palavras.
- Escolha nomes claros.
- Não comece nomes de variáveis com números.
- Evite nomes genéricos como `x`, `y` e `valor` quando o contexto pedir clareza.

Bom:

```python
idade_usuario = 30
preco_produto = 99.90
```

Ruim:

```python
x = 30
p = 99.90
```

## Exercícios

1. Crie variáveis para nome, sobrenome e idade. Mostre tudo na tela.
2. Crie `preco`, `desconto` e `preco_final`.
3. Crie `ano_atual`, `idade` e calcule o ano aproximado de nascimento.
4. Crie `nota1`, `nota2`, `nota3` e calcule a média.

---

# Aula 6 - Operadores aritméticos

Operadores aritméticos fazem cálculos.

```python
a = 10
b = 3

print(a + b)   # soma
print(a - b)   # subtração
print(a * b)   # multiplicação
print(a / b)   # divisão comum
print(a // b)  # divisão inteira
print(a % b)   # resto da divisão
print(a ** b)  # potência
```

## Módulo

O operador `%` retorna o resto da divisão.

Ele é muito usado para descobrir se um número é par.

```python
numero = 10
eh_par = numero % 2 == 0

print(eh_par)
```

## Precedência

Python segue uma ordem nos cálculos:

1. Parênteses
2. Potência
3. Multiplicação, divisão, divisão inteira e módulo
4. Soma e subtração

```python
resultado = 2 + 3 * 4
print(resultado)  # 14

resultado = (2 + 3) * 4
print(resultado)  # 20
```

## Exercícios

1. Calcule a soma, subtração, multiplicação e divisão entre dois números.
2. Verifique se um número é divisível por 3.
3. Calcule o IMC usando `peso / (altura ** 2)`.
4. Explique a diferença entre `10 / 3` e `10 // 3`.

---

# Aula 7 - Strings, concatenação e f-strings

Strings podem ser unidas com `+`.

```python
nome = "Ana"
sobrenome = "Lima"

nome_completo = nome + " " + sobrenome
print(nome_completo)
```

Strings também podem ser repetidas com `*`.

```python
linha = "-" * 20
print(linha)
```

## F-strings

F-strings são a forma mais prática de montar textos com variáveis.

```python
nome = "Carlos"
idade = 25

print(f"{nome} tem {idade} anos.")
```

Também podemos formatar números.

```python
preco = 19.9
print(f"Preço: R$ {preco:.2f}")
```

Saída:

```text
Preço: R$ 19.90
```

## Exercícios

1. Crie `nome` e `sobrenome`, depois mostre o nome completo.
2. Crie uma linha decorativa usando repetição de string.
3. Mostre uma frase usando f-string.
4. Mostre um preço com duas casas decimais.

---

# Aula 8 - Entrada de dados com input()

A função `input()` recebe dados digitados pelo usuário.

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

Ponto essencial:

```python
input() sempre retorna str
```

Mesmo quando o usuário digita um número, o Python recebe texto.

```python
numero = input("Digite um número: ")
print(type(numero))  # str
```

## Exercícios

1. Peça o nome do usuário e mostre uma saudação.
2. Peça cidade e estado, depois mostre uma frase formatada.
3. Peça o nome de um produto e mostre uma mensagem de cadastro.
4. Peça duas informações e mostre as duas no mesmo `print()`.

---

# Aula 9 - Conversão de tipos

Como `input()` retorna texto, precisamos converter quando queremos calcular.

```python
numero_texto = input("Digite um número: ")
numero = int(numero_texto)

print(numero + 10)
```

Conversões comuns:

```python
int("10")       # texto para inteiro
float("10.5")   # texto para decimal
str(10)         # número para texto
bool("")        # False
bool("texto")   # True
```

Exemplo com dois números:

```python
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2

print(f"Soma: {soma}")
```

## Exercícios

1. Peça um número inteiro e mostre o dobro.
2. Peça dois números e mostre a soma.
3. Peça peso e altura, depois calcule o IMC.
4. Converta uma idade digitada para `int` e mostre o tipo com `type()`.

---

# Aula 10 - Comparações e booleanos

Comparações produzem valores booleanos: `True` ou `False`.

```python
print(10 == 10)  # True
print(10 == 11)  # False
print(10 > 5)    # True
print(10 < 5)    # False
```

Operadores de comparação:

- `==`: igual
- `!=`: diferente
- `>`: maior que
- `<`: menor que
- `>=`: maior ou igual
- `<=`: menor ou igual

Exemplo:

```python
idade = 20
maior_de_idade = idade >= 18

print(maior_de_idade)
```

## Exercícios

1. Compare dois números usando `==`.
2. Verifique se uma idade é maior ou igual a 18.
3. Verifique se uma nota é maior ou igual a 7.
4. Verifique se dois textos digitados são iguais.

---

# Aula 11 - Condicionais

Condicionais permitem que o programa escolha caminhos.

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

## if, elif e else

```python
nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

O Python testa de cima para baixo. Quando uma condição verdadeira é encontrada, aquele bloco é executado.

## Indentação

Indentação é o recuo do código. Em Python, ela define quais comandos pertencem ao bloco.

```python
if True:
    print("Este print está dentro do if")

print("Este print está fora do if")
```

## Exercícios

1. Peça a idade e diga se a pessoa pode votar.
2. Peça um número e diga se ele é positivo, negativo ou zero.
3. Peça duas notas, calcule a média e diga se o aluno foi aprovado.
4. Peça dois números e informe qual é o maior ou se são iguais.

---

# Aula 12 - Operadores lógicos

Operadores lógicos combinam condições.

## and

`and` exige que todas as condições sejam verdadeiras.

```python
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
```

## or

`or` exige que pelo menos uma condição seja verdadeira.

```python
tem_ingresso = False
esta_na_lista = True

if tem_ingresso or esta_na_lista:
    print("Entrada liberada")
else:
    print("Entrada negada")
```

## not

`not` inverte uma condição.

```python
usuario_bloqueado = False

if not usuario_bloqueado:
    print("Usuário pode acessar")
```

## in e not in

`in` verifica se algo está dentro de outro valor.

```python
email = "aluno@exemplo.com"

if "@" in email:
    print("E-mail contém @")
```

## Exercícios

1. Verifique se uma pessoa tem idade suficiente e autorização para entrar em um evento.
2. Verifique se um usuário digitou `"S"` ou `"s"` para continuar.
3. Verifique se uma senha não está vazia.
4. Verifique se um e-mail contém `@` e `.`.

---

# Aula 13 - Repetição com while

O `while` repete um bloco enquanto uma condição for verdadeira.

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Saída:

```text
1
2
3
4
5
```

## Cuidado com loop infinito

Se a condição nunca ficar falsa, o programa não para.

```python
contador = 1

while contador <= 5:
    print(contador)
    # faltou alterar o contador
```

## break

`break` interrompe o laço.

```python
while True:
    senha = input("Digite a senha: ")

    if senha == "1234":
        print("Acesso liberado")
        break

    print("Senha incorreta")
```

## continue

`continue` pula para a próxima repetição.

```python
contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print(contador)
```

## Exercícios

1. Mostre os números de 1 a 10 usando `while`.
2. Mostre apenas os números pares de 1 a 20.
3. Peça uma senha até o usuário digitar a senha correta.
4. Peça números ao usuário até ele digitar `0`. Ao final, mostre a soma.

---

# Aula 14 - Repetição com for e range()

O `for` percorre uma sequência de valores.

```python
for numero in range(1, 6):
    print(numero)
```

Saída:

```text
1
2
3
4
5
```

## range()

`range()` gera uma sequência numérica.

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

## Percorrendo texto

Strings também podem ser percorridas.

```python
palavra = "Python"

for letra in palavra:
    print(letra)
```

## Quando usar while e quando usar for

Use `while` quando a repetição depende de uma condição que pode mudar durante o programa.

Use `for` quando você já sabe a sequência que deseja percorrer.

Exemplo com `while`:

```python
senha = ""

while senha != "1234":
    senha = input("Senha: ")
```

Exemplo com `for`:

```python
for numero in range(1, 11):
    print(numero)
```

## Exercícios

1. Mostre os números de 1 a 10 usando `for`.
2. Mostre os números pares de 0 a 20 usando `range()`.
3. Peça uma palavra e mostre cada letra em uma linha.
4. Peça um número e mostre a tabuada dele de 1 a 10.

---

# Aula 15 - Mini-projeto de fechamento

## Projeto: calculadora de média com situação do aluno

Crie um programa que:

1. Peça o nome do aluno.
2. Peça três notas.
3. Calcule a média.
4. Mostre a média com duas casas decimais.
5. Informe a situação:
   - Média maior ou igual a 7: aprovado
   - Média maior ou igual a 5 e menor que 7: recuperação
   - Média menor que 5: reprovado

## Resolução comentada

```python
nome = input("Nome do aluno: ")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Aluno: {nome}")
print(f"Média: {media:.2f}")

if media >= 7:
    print("Situação: aprovado")
elif media >= 5:
    print("Situação: recuperação")
else:
    print("Situação: reprovado")
```

## Desafio extra

Adapte o programa para permitir cadastrar vários alunos.

Regras:

- Use `while True`.
- Ao final de cada cadastro, pergunte se o usuário deseja continuar.
- Se o usuário digitar `n`, encerre o programa.
- Mostre a situação de cada aluno logo após calcular a média.

Modelo:

```python
while True:
    nome = input("Nome do aluno: ")

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = (nota1 + nota2 + nota3) / 3

    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Situação: aprovado")
    elif media >= 5:
        print("Situação: recuperação")
    else:
        print("Situação: reprovado")

    continuar = input("Cadastrar outro aluno? [s/n]: ")

    if continuar.lower() == "n":
        break
```

---

# Lista geral de revisão

## Parte 1 - Fundamentos

1. O que é uma variável?
2. Qual a diferença entre `int` e `float`?
3. O que `input()` sempre retorna?
4. Para que serve `type()`?
5. Qual a diferença entre `=` e `==`?

## Parte 2 - Cálculos

1. Calcule a média de três notas.
2. Calcule o preço final de um produto com desconto.
3. Verifique se um número é par.
4. Verifique se um número é divisível por 5.
5. Calcule o IMC.

## Parte 3 - Condições

1. Peça uma idade e diga se é maior de idade.
2. Peça uma nota e diga se o aluno foi aprovado.
3. Peça dois números e mostre o maior.
4. Peça uma senha e valide se ela está correta.
5. Peça um horário de 0 a 23 e mostre bom dia, boa tarde ou boa noite.

## Parte 4 - Repetições

1. Mostre os números de 1 a 100.
2. Mostre os números pares de 1 a 50.
3. Peça uma senha até acertar.
4. Faça uma tabuada.
5. Some números digitados até o usuário digitar `0`.

---

# Gabarito sugerido

## Fundamentos

1. Variável é um nome que guarda um valor na memória.
2. `int` representa inteiro; `float` representa número decimal.
3. `input()` sempre retorna `str`.
4. `type()` mostra o tipo de um valor.
5. `=` atribui valor; `==` compara valores.

## Número par

```python
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
```

## Maior de dois números

```python
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))

if a > b:
    print("O primeiro é maior")
elif b > a:
    print("O segundo é maior")
else:
    print("Os dois são iguais")
```

## Tabuada

```python
numero = int(input("Digite um número: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
```

## Soma até zero

```python
soma = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:
        break

    soma += numero

print(f"Soma final: {soma}")
```

---

# Critérios para considerar esta sessão concluída

O aluno está pronto para avançar quando conseguir:

- Ler um código simples e explicar a ordem de execução.
- Criar variáveis com nomes claros.
- Converter entradas do usuário para número.
- Usar `if`, `elif` e `else` sem confundir indentação.
- Criar condições com comparadores e operadores lógicos.
- Usar `while` para repetir até uma condição mudar.
- Usar `for` com `range()` para repetições previsíveis.
- Resolver sozinho exercícios pequenos de cálculo, decisão e repetição.

Depois desta sessão, a sequência natural é estudar coleções: listas, tuplas, índices, iteração com listas e métodos básicos de manipulação de dados.

---

# Módulo 2 - Coleções: listas, índices e tuplas

Depois de aprender variáveis simples, o próximo passo é guardar vários valores em uma única estrutura.

Uma lista permite armazenar vários itens.

```python
nomes = ["Ana", "Carlos", "João"]
print(nomes)
```

## Índices

Cada item da lista possui uma posição. Em Python, a contagem começa em `0`.

```python
nomes = ["Ana", "Carlos", "João"]

print(nomes[0])  # Ana
print(nomes[1])  # Carlos
print(nomes[2])  # João
```

## Alterando itens

Listas são mutáveis, ou seja, podem ser alteradas.

```python
nomes = ["Ana", "Carlos", "João"]
nomes[1] = "Mariana"

print(nomes)
```

## Adicionando itens

```python
nomes = []

nomes.append("Ana")
nomes.append("Carlos")

print(nomes)
```

## Removendo itens

```python
nomes = ["Ana", "Carlos", "João"]

nomes.pop()
print(nomes)
```

`pop()` sem índice remove o último item.

```python
nomes.pop(0)
```

Com índice, remove a posição informada.

## Tamanho da lista

```python
nomes = ["Ana", "Carlos", "João"]
print(len(nomes))
```

`len()` retorna a quantidade de itens.

## Tuplas

Tuplas são parecidas com listas, mas são imutáveis.

```python
cores = ("vermelho", "verde", "azul")
print(cores[0])
```

Use tuplas quando os dados não devem mudar.

## Listas ou tuplas?

- Lista: quando os dados podem mudar.
- Tupla: quando os dados devem permanecer fixos.

## Exercícios

1. Crie uma lista com três nomes e mostre o segundo nome.
2. Adicione um novo item usando `append()`.
3. Remova o último item usando `pop()`.
4. Altere o primeiro item da lista.
5. Crie uma tupla com três cores e mostre a última cor.

---

# Módulo 3 - Iteração com listas

Iterar significa percorrer item por item.

```python
nomes = ["Ana", "Carlos", "João"]

for nome in nomes:
    print(nome)
```

## Percorrendo com índice

Podemos combinar `range()` e `len()`.

```python
nomes = ["Ana", "Carlos", "João"]

for indice in range(len(nomes)):
    print(indice, nomes[indice])
```

## enumerate()

`enumerate()` entrega o índice e o valor ao mesmo tempo.

```python
nomes = ["Ana", "Carlos", "João"]

for indice, nome in enumerate(nomes):
    print(indice, nome)
```

Essa forma costuma ser mais limpa do que usar `range(len(lista))`.

## Lista interativa

```python
lista = []

while True:
    opcao = input("[i]nserir [l]istar [s]air: ")

    if opcao == "i":
        item = input("Item: ")
        lista.append(item)
    elif opcao == "l":
        if len(lista) == 0:
            print("Lista vazia")
        else:
            for indice, item in enumerate(lista):
                print(indice, item)
    elif opcao == "s":
        break
    else:
        print("Opção inválida")
```

## Exercícios

1. Percorra uma lista de nomes com `for`.
2. Mostre índice e valor usando `range()` e `len()`.
3. Mostre índice e valor usando `enumerate()`.
4. Crie uma lista interativa com opções para inserir, listar e sair.
5. Adicione uma opção para apagar um item pelo índice.

---

# Módulo 4 - Tratamento de erros

Programas podem quebrar quando recebem dados inesperados.

Exemplo problemático:

```python
numero = int(input("Digite um número: "))
print(numero * 2)
```

Se o usuário digitar texto, ocorrerá `ValueError`.

## try e except

```python
try:
    numero = int(input("Digite um número: "))
    print(numero * 2)
except ValueError:
    print("Você precisa digitar um número inteiro.")
```

O `try` tenta executar o código. O `except` trata o erro se ele acontecer.

## Tratando índice inválido

```python
nomes = ["Ana", "Carlos", "João"]

try:
    indice = int(input("Índice: "))
    print(nomes[indice])
except ValueError:
    print("Digite um número inteiro.")
except IndexError:
    print("Índice fora da lista.")
```

## Boa prática

Trate erros específicos. Evite usar `except` genérico sem necessidade.

## Exercícios

1. Peça um número e trate erro caso o usuário digite texto.
2. Peça dois números e trate erro de conversão.
3. Crie uma lista e permita buscar um item pelo índice.
4. Trate `ValueError` e `IndexError` no mesmo programa.
5. Refaça a lista interativa do módulo anterior com tratamento de erros.

---

# Módulo 5 - Manipulação de strings

Strings são sequências de caracteres. Por isso, podem ser acessadas por índice e percorridas.

```python
texto = "Python"

print(texto[0])  # P
print(texto[-1]) # n
```

## Fatiamento

```python
texto = "Python"

print(texto[0:2])  # Py
print(texto[2:])   # thon
print(texto[::-1]) # nohtyP
```

## in e not in

```python
email = "aluno@exemplo.com"

if "@" in email:
    print("Possui @")
```

## strip()

`strip()` remove espaços do começo e do fim.

```python
nome = "  Ana  "
print(nome.strip())
```

## split()

`split()` divide uma string e retorna uma lista.

```python
frase = "Ana,Carlos,João"
nomes = frase.split(",")

print(nomes)
```

## join()

`join()` junta itens de uma lista em uma string.

```python
nomes = ["Ana", "Carlos", "João"]
texto = ", ".join(nomes)

print(texto)
```

## Limpando dados

```python
entrada = "  Python, Java, C++  "
partes = entrada.split(",")
linguagens = []

for parte in partes:
    linguagens.append(parte.strip())

print(linguagens)
```

## Exercícios

1. Peça uma palavra e mostre a primeira e a última letra.
2. Inverta uma string usando fatiamento.
3. Peça nomes separados por vírgula e transforme em lista.
4. Remova espaços extras com `strip()`.
5. Junte uma lista de palavras usando `" - ".join(lista)`.

---

# Módulo 6 - Matrizes e listas dentro de listas

Uma matriz é uma lista que contém outras listas.

```python
salas = [
    ["Ana", "Carlos"],
    ["João", "Mariana"],
    ["Pedro", "Luiza"],
]
```

## Acessando valores

```python
print(salas[0])     # primeira sala
print(salas[0][1])  # Carlos
```

O primeiro índice escolhe a lista interna. O segundo índice escolhe o item dentro dela.

## Percorrendo matriz

```python
salas = [
    ["Ana", "Carlos"],
    ["João", "Mariana"],
    ["Pedro", "Luiza"],
]

for sala in salas:
    for aluno in sala:
        print(aluno)
```

## Com índice da sala

```python
for indice_sala, sala in enumerate(salas):
    print(f"Sala {indice_sala}:")

    for aluno in sala:
        print(aluno)
```

## Exercícios

1. Crie uma matriz com duas salas e dois alunos em cada sala.
2. Mostre apenas um aluno usando dois índices.
3. Percorra todos os alunos com dois `for`.
4. Mostre o número da sala usando `enumerate()`.
5. Conte quantos alunos existem no total.

---

# Módulo 7 - Empacotamento, desempacotamento e operador *

Desempacotar é distribuir valores de uma sequência em variáveis.

```python
dados = ["Ana", 25, "Brasil"]

nome, idade, pais = dados

print(nome)
print(idade)
print(pais)
```

## Usando * para capturar o restante

```python
valores = [1, 2, 3, 4, 5]

primeiro, segundo, *resto = valores

print(primeiro)
print(segundo)
print(resto)
```

## Ignorando valores

```python
dados = ["Ana", 25, "Brasil", "Python"]

nome, *_, linguagem = dados

print(nome)
print(linguagem)
```

`_` é usado por convenção para valores que não serão utilizados.

## Espalhando valores no print()

```python
nomes = ["Ana", "Carlos", "João"]

print(*nomes)
print(*nomes, sep=" | ")
```

## Exercícios

1. Desempacote uma lista com nome, idade e cidade.
2. Use `*resto` para capturar valores restantes.
3. Ignore valores intermediários usando `*_`.
4. Imprima uma lista usando `print(*lista)`.
5. Use `sep` junto com desempacotamento.

---

# Módulo 8 - Precisão numérica e Decimal

Números decimais com `float` podem ter pequenas imprecisões.

```python
print(0.1 + 0.2)
```

O resultado pode não ser exatamente `0.3`.

Isso acontece porque computadores representam números decimais em binário.

## round()

`round()` arredonda valores.

```python
valor = 10 / 3
print(round(valor, 2))
```

## Formatação com f-string

```python
valor = 10 / 3
print(f"{valor:.2f}")
```

## Decimal

Para cálculos que exigem mais precisão decimal, use `Decimal`.

```python
from decimal import Decimal

numero1 = Decimal("0.1")
numero2 = Decimal("0.2")

print(numero1 + numero2)
```

Importante: passe strings para `Decimal`.

```python
Decimal("0.1")  # recomendado
Decimal(0.1)    # carrega a imprecisão do float
```

## Exercícios

1. Some `0.1 + 0.2` usando `float`.
2. Some `Decimal("0.1") + Decimal("0.2")`.
3. Arredonde `10 / 3` para duas casas.
4. Mostre um preço com duas casas usando f-string.
5. Some uma lista de valores monetários usando `Decimal`.

---

# Módulo 9 - Operador ternário

O operador ternário é uma forma curta de escrever `if/else`.

Forma geral:

```python
valor_se_verdadeiro if condicao else valor_se_falso
```

Exemplo:

```python
idade = 20
resultado = "Maior de idade" if idade >= 18 else "Menor de idade"

print(resultado)
```

## Comparação com if comum

```python
idade = 20

if idade >= 18:
    resultado = "Maior de idade"
else:
    resultado = "Menor de idade"
```

O ternário é útil para decisões simples. Para regras maiores, prefira `if`, `elif` e `else`.

## Ternário encadeado

```python
nota = 8
conceito = "A" if nota >= 9 else "B" if nota >= 7 else "C"

print(conceito)
```

Use com cuidado. Se ficar difícil de ler, escreva com `if/elif/else`.

## Exercícios

1. Crie um ternário para verificar se uma idade é maior de idade.
2. Crie um ternário para retornar `"Par"` ou `"Ímpar"`.
3. Crie um ternário para verificar se uma nota aprova ou reprova.
4. Reescreva um ternário usando `if/else`.
5. Reescreva um `if/else` simples usando ternário.

---

# Módulo 10 - Projetos de lógica

Este módulo junta fundamentos, coleções, strings, erros e repetição.

## Projeto 1 - Lista de compras

Requisitos:

- Inserir item
- Listar itens
- Apagar item pelo índice
- Sair do programa
- Tratar índice inválido

```python
lista = []

while True:
    opcao = input("[i]nserir [l]istar [a]pagar [s]air: ")

    if opcao == "i":
        item = input("Item: ")
        lista.append(item)

    elif opcao == "l":
        if len(lista) == 0:
            print("Lista vazia")
        else:
            for indice, item in enumerate(lista):
                print(indice, item)

    elif opcao == "a":
        try:
            indice = int(input("Índice para apagar: "))
            lista.pop(indice)
        except ValueError:
            print("Digite um índice numérico.")
        except IndexError:
            print("Índice não existe.")

    elif opcao == "s":
        break

    else:
        print("Opção inválida.")
```

## Projeto 2 - Contador de letras

Requisitos:

- Pedir uma frase
- Ignorar espaços
- Contar quantas vezes cada letra aparece

```python
frase = input("Digite uma frase: ").lower()
letras_contadas = []

for letra in frase:
    if letra == " ":
        continue

    if letra not in letras_contadas:
        quantidade = frase.count(letra)
        letras_contadas.append(letra)
        print(f"{letra}: {quantidade}")
```

## Projeto 3 - Validação simples de dados

Requisitos:

- Pedir nome
- Pedir idade
- Nome não pode ficar vazio
- Idade precisa ser numérica

```python
nome = input("Nome: ").strip()
idade = input("Idade: ").strip()

if not nome:
    print("Nome não pode ficar vazio.")
elif not idade.isdigit():
    print("Idade precisa ser numérica.")
elif int(idade) <= 0:
    print("Idade precisa ser maior que zero.")
else:
    print(f"Cadastro realizado: {nome}, {idade} anos.")
```

---

# Módulo 11 - Projeto CPF

Este projeto deve aparecer depois de o aluno já dominar:

- strings
- índices e fatiamento
- `for`
- acumuladores
- conversão com `int()` e `str()`
- condicionais
- funções de limpeza de texto

## Regra geral do CPF

Um CPF possui 11 dígitos. Os dois últimos são dígitos verificadores.

A validação consiste em:

1. Limpar a entrada, deixando apenas números.
2. Rejeitar sequências repetidas, como `11111111111`.
3. Calcular o primeiro dígito verificador.
4. Calcular o segundo dígito verificador.
5. Comparar o CPF calculado com o CPF informado.

## Limpando entrada

```python
cpf = "746.824.890-70"
cpf = cpf.replace(".", "").replace("-", "").replace(" ", "")

print(cpf)
```

## Primeiro dígito

```python
cpf = "74682489070"
nove_digitos = cpf[:9]

soma = 0
contador = 10

for digito in nove_digitos:
    soma += int(digito) * contador
    contador -= 1

digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(digito_1)
```

## Segundo dígito

```python
dez_digitos = nove_digitos + str(digito_1)

soma = 0
contador = 11

for digito in dez_digitos:
    soma += int(digito) * contador
    contador -= 1

digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(digito_2)
```

## Validador completo

```python
cpf_enviado = input("CPF: ")
cpf = cpf_enviado.replace(".", "").replace("-", "").replace(" ", "")

if len(cpf) != 11:
    print("CPF inválido")
elif cpf == cpf[0] * len(cpf):
    print("CPF inválido")
else:
    nove_digitos = cpf[:9]

    soma = 0
    contador = 10

    for digito in nove_digitos:
        soma += int(digito) * contador
        contador -= 1

    digito_1 = (soma * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)

    soma = 0
    contador = 11

    for digito in dez_digitos:
        soma += int(digito) * contador
        contador -= 1

    digito_2 = (soma * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f"{nove_digitos}{digito_1}{digito_2}"

    if cpf == cpf_gerado:
        print("CPF válido")
    else:
        print("CPF inválido")
```

## Gerador simples de CPF

```python
import random

nove_digitos = ""

for _ in range(9):
    nove_digitos += str(random.randint(0, 9))

soma = 0
contador = 10

for digito in nove_digitos:
    soma += int(digito) * contador
    contador -= 1

digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)

soma = 0
contador = 11

for digito in dez_digitos:
    soma += int(digito) * contador
    contador -= 1

digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf = f"{nove_digitos}{digito_1}{digito_2}"
cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

print(cpf_formatado)
```

## Exercícios

1. Explique por que CPFs com todos os dígitos iguais devem ser rejeitados.
2. Calcule manualmente o primeiro dígito de um CPF com 9 dígitos.
3. Faça o programa exibir o CPF formatado.
4. Permita validar vários CPFs até o usuário digitar `sair`.
5. Separe a lógica em etapas escritas em pseudocódigo antes de programar.

---

# Módulo 12 - Organização final da trilha

A trilha completa fica assim:

1. Lógica de programação básica
2. Coleções: listas, índices e tuplas
3. Iteração com listas
4. Tratamento de erros
5. Manipulação de strings
6. Matrizes e listas dentro de listas
7. Empacotamento, desempacotamento e operador `*`
8. Precisão numérica e `Decimal`
9. Operador ternário
10. Projetos de lógica
11. Projeto CPF

## Critérios para avançar para funções

O aluno estará pronto para estudar funções quando conseguir:

- Resolver problemas usando entrada, processamento e saída.
- Escolher entre `if`, `while` e `for` de forma consciente.
- Trabalhar com listas e índices sem se perder.
- Tratar erros básicos de entrada.
- Manipular strings com fatiamento, `split()`, `strip()` e `join()`.
- Organizar um projeto pequeno em etapas.

O próximo módulo natural depois desta trilha é: funções, escopo, retorno, parâmetros e reutilização de código.
