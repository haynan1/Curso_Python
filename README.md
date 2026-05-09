# Curso Python

Trilha de estudo em Python organizada para consulta pública pelo GitHub Pages e manutenção interna com apoio de um cofre Obsidian.

Este repositório tem dois papéis:

1. Publicar o conteúdo didático principal no site do curso.
2. Guardar os materiais de apoio usados para desenvolver, revisar e expandir as aulas.

O conteúdo atual foi reorganizado com base na pasta `conteudos/secao_3`, que reúne os arquivos Python da seção inicial do curso.

## Acesso rápido

- Site público: renderizado pelo `index.html` a partir deste `README.md`.
- Conteúdo-base da seção atual: `conteudos/secao_3/`.
- Cofre de anotações: `Curso_Python/`.
- Documentação interna: `docs/`.
- Modelos reutilizáveis: `templates/`.
- Ferramentas de organização: `tools/`.

## Regra principal do repositório

Nunca edite, apague, renomeie ou mova arquivos dentro de:

```text
Curso_Python/.obsidian/
```

Essa pasta pertence ao Obsidian e guarda configurações internas do cofre, como plugins, aparência, workspace e preferências locais. Alterar esses arquivos pode quebrar o ambiente de anotações.

Ao trabalhar no cofre, edite apenas arquivos `.md` de conteúdo, como:

```text
Curso_Python/00 - Início.md
Curso_Python/secao-03.md
Curso_Python/anotacoes/
Curso_Python/mapas/
```

Se uma alteração exigir mexer em `.obsidian`, ela deve ser feita manualmente pelo dono do cofre, dentro do próprio Obsidian.

---

# Guia Público do Curso

Este curso começa pela lógica de programação em Python e avança aos poucos até pequenos projetos práticos.

A proposta é estudar Python com três camadas:

- Conceito: entender o que o recurso faz.
- Código: ver exemplos pequenos e executáveis.
- Prática: resolver exercícios e mini-projetos.

## Objetivo da seção 3

Ao final da seção 3, o aluno deve conseguir:

- Ler código Python básico com segurança.
- Usar comentários e docstrings para documentar ideias.
- Exibir informações com `print()`.
- Trabalhar com strings, números e booleanos.
- Criar variáveis com nomes claros.
- Converter tipos de dados quando necessário.
- Receber entradas com `input()`.
- Fazer cálculos com operadores aritméticos.
- Comparar valores e montar condições.
- Usar `if`, `elif` e `else`.
- Combinar condições com `and`, `or`, `not`, `in` e `not in`.
- Repetir ações com `while`, `for` e `range()`.
- Manipular strings, listas, tuplas e matrizes.
- Tratar erros simples com `try` e `except`.
- Resolver pequenos projetos de lógica, incluindo validação de CPF.

## Trilha de aprendizagem

A seção 3 deve ser estudada nesta ordem:

1. Comentários, docstrings e organização mental do código.
2. Saída de dados com `print()`, `sep` e `end`.
3. Strings, aspas, caracteres de escape e raw strings.
4. Tipos numéricos: `int` e `float`.
5. Tipo booleano e operadores de comparação.
6. Conversão de tipos, coerção e cuidados com `input()`.
7. Variáveis, constantes e boas práticas de nomeação.
8. Operadores aritméticos, precedência e expressões.
9. Concatenação, f-strings e formatação de valores.
10. Entrada de dados e exercícios de processamento.
11. Condicionais com `if`, `elif` e `else`.
12. Operadores lógicos e avaliação de curto-circuito.
13. Interpolação, formatação de strings e fatiamento.
14. Tratamento de erros com `try` e `except`.
15. Repetição com `while`.
16. Controle de laços com `break`, `continue` e `while else`.
17. Repetição com `for` e `range()`.
18. Listas, índices, alteração, inserção e remoção.
19. Tuplas, empacotamento e desempacotamento.
20. Iteração com listas, `range(len())` e `enumerate()`.
21. Lista interativa com validação e tratamento de erros.
22. Precisão numérica com `float`, `round()` e `Decimal`.
23. Manipulação de strings com `split()`, `join()` e métodos.
24. Listas dentro de listas e matrizes.
25. Leitura do interpretador, métodos e funções.
26. Projeto final: cálculo, geração e validação de CPF.

## Organização dos arquivos da seção 3

Os arquivos de aula ficam em:

```text
conteudos/secao_3/
```

Eles seguem a ordem numérica do curso:

```text
01 - arquivo_de_testes_0.py
02 - aula01.py
03 - aula02.py
...
69 - aula63.py
```

Cada arquivo Python pode conter:

- anotações iniciais do estudo;
- exemplos executáveis;
- material de suporte;
- explicação didática;
- exercícios;
- gabarito ou resolução comentada.

## Mapa da seção 3

| Bloco | Arquivos | Tema |
| --- | --- | --- |
| Preparação | `01` | Testes curtos e avaliação de expressões |
| Fundamentos | `02` a `16` | Comentários, `print()`, strings, tipos, variáveis, operadores, entrada e formatação |
| Decisões | `17` a `24` | Condicionais, comparação, operadores lógicos e fluxo de decisão |
| Strings e validação | `25` a `34` | Interpolação, fatiamento, entrada, exercícios e tratamento inicial de erros |
| Repetições | `35` a `47` | `while`, `for`, `range()`, controle de laços e exercícios práticos |
| Coleções | `48.1` a `54` | Listas, tuplas, índices, `enumerate()` e lista interativa |
| Dados e estruturas | `55` a `59` | `Decimal`, manipulação de strings, matrizes, interpretador e métodos |
| Projeto CPF | `60` a `63` | Cálculo de dígitos, geração e validação de CPF |

## Critérios para avançar

O aluno está pronto para continuar quando conseguir:

- explicar a ordem de execução de um script simples;
- separar entrada, processamento e saída;
- escrever variáveis com nomes claros;
- converter dados recebidos por `input()`;
- montar condições com comparadores e operadores lógicos;
- usar `while` quando a repetição depende de uma condição;
- usar `for` quando existe uma sequência definida;
- manipular listas e strings sem depender de tentativa e erro;
- tratar erros básicos de entrada;
- construir uma solução pequena em etapas.

---

# Estrutura do Repositório

Esta é a organização recomendada para manter o curso público, evolutivo e compatível com GitHub Pages.

```text
.
├── README.md
├── index.html
├── script.js
├── style.css
├── assets/
├── conteudos/
│   └── secao_3/
│       ├── README.md
│       ├── 01 - arquivo_de_testes_0.py
│       ├── 02 - aula01.py
│       └── ...
├── Curso_Python/
│   ├── .obsidian/
│   └── 00 - Início.md
├── docs/
├── templates/
└── tools/
```

## Função de cada área

| Caminho | Função |
| --- | --- |
| `README.md` | Conteúdo principal publicado no GitHub Pages |
| `index.html` | Página que abre o curso no navegador |
| `script.js` | Lê e renderiza o Markdown do curso |
| `style.css` | Aparência do site |
| `assets/` | Imagens, ícones e arquivos visuais |
| `conteudos/` | Materiais de base separados por seção |
| `Curso_Python/` | Cofre Obsidian para anotações estruturadas |
| `Curso_Python/.obsidian/` | Configurações internas do Obsidian. Não mexer |
| `docs/` | Documentação técnica e guias de manutenção |
| `templates/` | Modelos para novas aulas e seções |
| `tools/` | Scripts auxiliares de organização |

## Como o GitHub Pages usa este projeto

O site público deve continuar simples:

1. O GitHub Pages publica a raiz do repositório.
2. O navegador abre `index.html`.
3. O JavaScript carrega este `README.md`.
4. Os títulos do Markdown viram páginas e seções navegáveis.

Por isso, o `README.md` precisa ser claro, bem estruturado e estável. Ele é a versão pública do curso.

Os arquivos em `conteudos/` funcionam como fonte de estudo e desenvolvimento. Eles não precisam ser lidos diretamente pelo aluno no primeiro acesso.

---

# Padrão para Novas Seções

Toda nova seção deve nascer dentro de `conteudos/`.

Use nomes previsíveis:

```text
conteudos/secao_04/
conteudos/secao_05/
conteudos/secao_06/
```

A pasta atual permanece como `secao_3` para preservar o histórico já existente.

## Estrutura mínima de uma seção

```text
conteudos/secao_04/
├── README.md
├── 01 - aula01.py
├── 02 - aula02.py
└── 03 - aula03.py
```

O `README.md` da seção deve conter:

- objetivo da seção;
- pré-requisitos;
- ordem sugerida das aulas;
- lista de arquivos;
- critérios para avançar;
- observações de manutenção.

## Padrão de aula

Ao criar um novo arquivo de aula, siga esta estrutura:

```python
"""
Título da aula

Resumo curto do que será estudado.
"""

# ========================================
# OBJETIVO
# ========================================

"""
- Objetivo 1
- Objetivo 2
- Objetivo 3
"""

# ========================================
# EXPLICAÇÃO
# ========================================

"""
Explicação didática em linguagem simples.
"""

# ========================================
# EXEMPLOS
# ========================================

print("Exemplo executável")

# ========================================
# EXERCÍCIOS
# ========================================

"""
1. Exercício fácil.
2. Exercício médio.
3. Exercício de revisão.
"""
```

## Fluxo de atualização

1. Criar ou atualizar os arquivos em `conteudos/secao_XX/`.
2. Registrar a visão geral no `README.md` da própria seção.
3. Criar ou atualizar notas no cofre `Curso_Python/`, sem mexer em `.obsidian`.
4. Consolidar a versão pública no `README.md` da raiz.
5. Abrir o site localmente e conferir a navegação.
6. Publicar no GitHub Pages.

---

# Cofre Obsidian

O cofre fica em:

```text
Curso_Python/
```

Ele deve ser usado para organizar pensamento, mapas de conteúdo, rascunhos e anotações conectadas.

## O que pode ficar no cofre

- mapas de estudo;
- resumos por seção;
- links entre conceitos;
- planejamento de novas aulas;
- observações de revisão;
- ideias de exercícios;
- anotações pessoais de evolução do curso.

## O que não deve ser feito no cofre

- Não transformar `.obsidian` em área de conteúdo.
- Não mover configurações internas para outra pasta.
- Não depender de plugin específico para o site funcionar.
- Não publicar notas incompletas como se fossem conteúdo final.

## Separação entre cofre e site

O Obsidian é a oficina.

O GitHub Pages é a vitrine.

As notas podem ser livres, conectadas e exploratórias. O `README.md` da raiz deve ser limpo, sequencial e pronto para o aluno.

---

# Manual do README Público

Este arquivo é o conteúdo principal renderizado pelo site.

## Regras de escrita

- Use `#` para criar uma página principal no site.
- Use `##` e `###` para criar divisões dentro da página.
- Use blocos de código com três crases.
- Prefira exemplos pequenos antes de exemplos completos.
- Explique o conceito antes de mostrar a solução.
- Termine conteúdos didáticos com exercícios ou critérios de domínio.
- Mantenha a ordem de aprendizagem progressiva.

## Modelo de módulo público

````md
# Módulo X - Nome do conteúdo

Introdução curta do tema.

## Objetivo

- Objetivo 1
- Objetivo 2
- Objetivo 3

## Explicação

Texto didático em linguagem simples.

## Exemplo

```python
print("Olá, Python")
```

## Exercícios

1. Exercício inicial.
2. Exercício intermediário.
3. Exercício de revisão.
````

## Quando atualizar este README

Atualize o `README.md` da raiz quando:

- uma seção estiver pronta para publicação;
- a ordem da trilha mudar;
- um projeto novo entrar no curso;
- a estrutura do repositório mudar;
- uma regra de manutenção precisar ficar visível.

Não use o README público para guardar rascunhos longos. Rascunhos devem ficar em `conteudos/` ou no cofre Obsidian.

---

# Manutenção

## Antes de publicar

Confira:

- O `README.md` abre corretamente no site.
- Os títulos principais usam apenas um `#`.
- Os subtítulos usam `##` ou `###`.
- Os blocos de código estão fechados.
- Links internos apontam para arquivos existentes.
- Nenhum arquivo dentro de `Curso_Python/.obsidian/` foi alterado.
- Arquivos temporários, ambientes virtuais e logs não entraram no Git.

## Comandos úteis

Listar arquivos da seção 3:

```bash
python tools/organizador.py --target conteudos/secao_3
```

Executar uma aula específica:

```bash
python "conteudos/secao_3/02 - aula01.py"
```

Verificar o status do repositório:

```bash
git status
```

## Próxima evolução recomendada

A próxima melhoria natural é criar páginas públicas específicas para cada seção, mantendo este README como índice principal.

Uma estrutura futura possível:

```text
conteudos/
├── secao_03/
│   └── publico.md
├── secao_04/
│   └── publico.md
└── secao_05/
    └── publico.md
```

Depois disso, o site pode carregar cada arquivo sob demanda, sem deixar o `README.md` grande demais.
