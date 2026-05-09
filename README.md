# Curso Python

Este é o repositório público do Curso Python. Ele organiza os conteúdos editáveis em `conteudos/`, mantém um cérebro de documentação no Obsidian em `doc_python/` e publica a trilha didática pelo GitHub Pages usando este `README.md`.

O objetivo é simples: estudar Python com uma estrutura que dá para crescer, revisar, editar e publicar sem bagunçar a origem dos conteúdos.

## Como este curso é organizado

- `conteudos/`: fonte editável do curso. Os arquivos Python, exercícios e materiais de cada seção ficam aqui.
- `doc_python/`: cofre Obsidian. É o cérebro do projeto, com mapas, decisões, vínculos e documentação interna.
- `README.md`: versão pública, organizada em módulos, renderizada no GitHub Pages.
- `index.html`, `script.js` e `style.css`: site que transforma este README em uma navegação por páginas.

## Regra principal

Nunca edite manualmente a pasta:

```text
doc_python/.obsidian/
```

Essa pasta pertence ao Obsidian. Ela guarda configurações internas do cofre e não deve ser usada como conteúdo do curso.

---

# Módulo 01 - Visão Geral da Trilha

O curso foi pensado para evoluir em camadas. Primeiro vem a lógica, depois os recursos da linguagem, depois organização de código, automação, projetos e evolução para assuntos mais profissionais.

## Objetivo da trilha

Ao longo do curso, o aluno deve sair de scripts simples para programas cada vez mais organizados, entendendo não só como escrever código, mas também como pensar, testar, documentar e evoluir soluções.

## Método de estudo

Cada seção deve seguir este ciclo:

1. Entender o conceito.
2. Ler exemplos pequenos.
3. Executar arquivos Python.
4. Alterar os exemplos.
5. Resolver exercícios.
6. Registrar aprendizados no Obsidian.
7. Consolidar a versão pública no README.

## Onde cada coisa fica

| Área | Papel |
| --- | --- |
| `conteudos/secao_X/` | Arquivos Python e materiais editáveis da seção |
| `conteudos/secao_X/README.md` | Índice interno da seção |
| `doc_python/` | Cérebro do curso no Obsidian |
| `README.md` | Página pública do GitHub Pages |
| `docs/` | Documentação técnica auxiliar |
| `templates/` | Modelos para novas aulas e seções |
| `tools/` | Scripts de manutenção |

## Estado atual

A pasta `conteudos/` já possui seções de `secao_3` até `secao_23`. A seção com conteúdo efetivo neste momento é:

- `conteudos/secao_3/`: lógica de programação em Python, com 69 arquivos `.py` e um `README.md` interno.

As seções `secao_4` até `secao_23` já existem como espaços preparados para receber novos conteúdos.

---

# Módulo 02 - Mapa dos Conteúdos

Este módulo lista todas as pastas dentro de `conteudos/` e define o papel de cada uma na evolução do curso.

## Índice geral

| Pasta | Estado | Função |
| --- | --- | --- |
| `conteudos/secao_3/` | Em produção | Lógica de programação, fundamentos de Python, coleções, strings, erros, laços e projeto CPF |
| `conteudos/secao_4/` | Preparada | Próxima etapa após lógica: funções, escopo, parâmetros e retorno |
| `conteudos/secao_5/` | Preparada | Organização de código, módulos, pacotes e importações |
| `conteudos/secao_6/` | Preparada | Estruturas de dados mais completas e prática guiada |
| `conteudos/secao_7/` | Preparada | Arquivos, leitura, escrita e persistência simples |
| `conteudos/secao_8/` | Preparada | Tratamento de exceções com mais profundidade e validações |
| `conteudos/secao_9/` | Preparada | Funções avançadas, lambdas, callbacks e escopo |
| `conteudos/secao_10/` | Preparada | Programação orientada a objetos |
| `conteudos/secao_11/` | Preparada | Ambientes, dependências e ferramentas de projeto |
| `conteudos/secao_12/` | Preparada | Testes automatizados e qualidade de código |
| `conteudos/secao_13/` | Preparada | Automação com Python |
| `conteudos/secao_14/` | Preparada | Manipulação de dados e arquivos estruturados |
| `conteudos/secao_15/` | Preparada | Projetos intermediários |
| `conteudos/secao_16/` | Preparada | Banco de dados e persistência |
| `conteudos/secao_17/` | Preparada | APIs, requisições e integração com serviços |
| `conteudos/secao_18/` | Preparada | Interfaces, scripts de terminal e produtividade |
| `conteudos/secao_19/` | Preparada | Web, deploy ou aplicações práticas |
| `conteudos/secao_20/` | Preparada | Projeto aplicado de maior porte |
| `conteudos/secao_21/` | Preparada | Revisão, refatoração e boas práticas |
| `conteudos/secao_22/` | Preparada | Portfólio e documentação de projetos |
| `conteudos/secao_23/` | Preparada | Fechamento, próximos passos e plano de evolução |

## Regra para cada pasta de seção

Cada pasta dentro de `conteudos/` deve ter:

- um `README.md` da seção;
- arquivos `.py` de aula, exercício ou projeto;
- nomes ordenáveis por número;
- critérios para considerar a seção concluída;
- relação clara com as notas do Obsidian.

## Convenção de arquivos

Use nomes previsíveis:

```text
01 - aula01.py
02 - aula02.py
03 - exercicio_guiado.py
04 - projeto_final.py
README.md
```

Evite nomes soltos sem contexto. O arquivo pode ser alterado quantas vezes for necessário durante o estudo, mas precisa continuar encontrável.

---

# Módulo 03 - Lógica de Programação em Python

Fonte editável:

```text
conteudos/secao_3/
```

Esta é a primeira seção real do curso. Ela constrói a base para entender Python: comentários, saída de dados, tipos, variáveis, operadores, entrada, decisões, repetições, coleções, strings, erros e projeto CPF.

## Objetivo da seção

Ao terminar esta seção, o aluno deve conseguir:

- ler um script Python simples;
- explicar a ordem de execução do código;
- usar `print()` para saída de dados;
- criar variáveis com nomes claros;
- trabalhar com `str`, `int`, `float` e `bool`;
- converter entradas recebidas por `input()`;
- escrever condições com `if`, `elif` e `else`;
- combinar regras com operadores lógicos;
- usar `while` e `for`;
- manipular listas, tuplas, strings e matrizes;
- tratar erros comuns;
- resolver um projeto de validação de CPF.

## Bloco 03.1 - Primeiros fundamentos

Arquivos:

```text
01 - arquivo_de_testes_0.py
02 - aula01.py
03 - aula02.py
04 - aula03.py
05 - aula04.py
06 - aula05.py
07 - aula06.py
08 - aula07.py
09 - aula08.py
10 - aula09.py
11 - aula10.py
12 - aula11.py
13 - aula12.py
14 - aula13.py
15 - aula14.py
16 - aula15.py
```

Conteúdos trabalhados:

- avaliação de expressões;
- docstrings e comentários;
- `print()`, `sep` e `end`;
- strings, aspas e escape;
- tipos `int`, `float`, `str` e `bool`;
- `type()`;
- conversão de tipos;
- variáveis e constantes;
- operadores aritméticos;
- entrada com `input()`;
- f-strings e formatação;
- exercícios de fixação.

Este bloco cria o vocabulário mínimo do aluno. Antes de avançar, ele precisa entender o que entra, o que o programa processa e o que sai.

## Bloco 03.2 - Decisões e lógica booleana

Arquivos:

```text
17 - aula16.py
18 - aula17.py
19 - aula18.py
20 - aula19.py
21 - aula20.py
22 - aula21.py
23 - aula22.py
24 - aula23.py
```

Conteúdos trabalhados:

- condicionais;
- `if`, `elif` e `else`;
- indentação;
- comparadores;
- operadores lógicos;
- `and`, `or`, `not`;
- `in` e `not in`;
- avaliação de curto-circuito;
- decisões encadeadas.

Este bloco ensina o programa a escolher caminhos. É aqui que o aluno deixa de escrever scripts lineares e começa a criar regras.

## Bloco 03.3 - Strings, formatação e validação inicial

Arquivos:

```text
25 - aula24.py
26 - aula25.py
27 - aula26.py
28 - aula27.py
29 - aula28.py
30 - aula29.py
31 - aula30.py
32 - aula31.py
33 - aula32.py
34 - aula33.py
```

Conteúdos trabalhados:

- interpolação;
- formatação de strings;
- fatiamento;
- tamanho de strings;
- validação de entrada;
- exercícios de par ou ímpar;
- documentação auxiliar;
- primeiros cuidados com erros.

Este bloco aproxima o aluno de problemas reais: dados digitados vêm sujos, incompletos ou em formato diferente do esperado.

## Bloco 03.4 - Repetições

Arquivos:

```text
35 - aula34.py
36 - aula35.py
37 - aula36.py
38 - aula37.py
39 - aula38.py
40 - aula39.py
41 - aula40.py
42 - aula41.py
43 - aula42.py
44 - aula43.py
45 - aula44.py
46 - aula45.py
47 - aula46.py
48 - aula47.py
```

Conteúdos trabalhados:

- `while`;
- controle de fluxo;
- acumuladores;
- contadores;
- `break`;
- `continue`;
- `while else`;
- calculadora com validação;
- contagem de letras;
- `for`;
- `range()`;
- exercícios de repetição.

Este bloco ensina o programa a insistir, percorrer e repetir. É uma virada importante: o aluno começa a resolver tarefas com volume.

## Bloco 03.5 - Coleções

Arquivos:

```text
49 - aula48.1.py
50 - aula48.2.py
51 - aula48.3.py
52 - aula48.4.py
53 - aula48.5.py
54 - aula49.py
55 - aula50.py
56 - aula51.py
57 - aula52.py
58 - aula53.py
59 - aula54.py
```

Conteúdos trabalhados:

- listas;
- índices;
- alteração de itens;
- inserção e remoção;
- `append()`, `pop()` e `clear()`;
- tuplas;
- empacotamento;
- desempacotamento;
- `enumerate()`;
- lista interativa;
- tratamento de índice inválido.

Este bloco ensina a trabalhar com vários dados ao mesmo tempo. Depois dele, o aluno já consegue construir pequenos sistemas em modo terminal.

## Bloco 03.6 - Dados, strings e estruturas

Arquivos:

```text
60 - aula55.py
61 - aula56.py
62 - aula57.py
63 - aula58.py
64 - aula59.py
```

Conteúdos trabalhados:

- imprecisão de ponto flutuante;
- `Decimal`;
- `split()`;
- `join()`;
- listas dentro de listas;
- matrizes;
- interpretador do Python;
- Zen of Python;
- diferença entre métodos e funções.

Este bloco melhora a maturidade do aluno. Ele passa a enxergar que Python não é só escrever comandos, mas entender comportamento, precisão e organização de dados.

## Bloco 03.7 - Projeto CPF

Arquivos:

```text
65 - aula60.py
66 - aula61.py
67 - aula62.1.py
68 - aula62.2.py
69 - aula63.py
```

Conteúdos trabalhados:

- cálculo de dígitos verificadores;
- contadores regressivos;
- acumuladores;
- limpeza de entrada;
- rejeição de sequências repetidas;
- `re.sub()`;
- `sys.exit()`;
- validação completa de CPF.

Este projeto fecha a seção porque combina quase tudo: strings, números, laços, condições, conversão de tipos, validação e organização em etapas.

## Critérios de conclusão da seção 3

O aluno pode avançar quando conseguir:

- explicar um código sem executar;
- escrever scripts pequenos sem copiar;
- montar condições com clareza;
- escolher entre `while` e `for`;
- manipular listas e strings;
- tratar erros simples de entrada;
- adaptar o validador de CPF;
- registrar dúvidas e decisões no Obsidian.

---

# Módulo 04 - Funções e Reutilização

Fonte editável:

```text
conteudos/secao_4/
```

Estado atual: pasta preparada para receber conteúdo.

## Objetivo planejado

Transformar scripts lineares em blocos reutilizáveis com funções.

## Conteúdos previstos

- criação de funções com `def`;
- parâmetros;
- argumentos;
- retorno com `return`;
- escopo local e global;
- funções pequenas e legíveis;
- refatoração de scripts da seção 3;
- aplicação em projetos simples.

## Conexão com a seção anterior

A seção 3 ensina o aluno a resolver problemas. Esta seção deve ensinar a organizar essas soluções em partes reutilizáveis.

---

# Módulo 05 - Organização de Código

Fonte editável:

```text
conteudos/secao_5/
```

Estado atual: pasta preparada para receber conteúdo.

## Objetivo planejado

Ensinar como separar responsabilidades e manter arquivos Python mais fáceis de evoluir.

## Conteúdos previstos

- módulos;
- importações;
- pacotes;
- arquivos auxiliares;
- separação entre execução e definição;
- `if __name__ == "__main__"`;
- organização de pequenos projetos.

---

# Módulo 06 - Estruturas de Dados

Fonte editável:

```text
conteudos/secao_6/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- dicionários;
- conjuntos;
- listas de dicionários;
- tuplas nomeadas ou estruturas simples;
- iteração em estruturas aninhadas;
- busca, filtro e transformação de dados.

---

# Módulo 07 - Arquivos e Persistência

Fonte editável:

```text
conteudos/secao_7/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- leitura de arquivos;
- escrita de arquivos;
- caminhos;
- `with open()`;
- arquivos `.txt`;
- arquivos `.csv`;
- introdução a JSON.

---

# Módulo 08 - Erros e Validações

Fonte editável:

```text
conteudos/secao_8/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- exceções específicas;
- múltiplos `except`;
- `else` e `finally`;
- validação de entrada;
- mensagens de erro úteis;
- criação de funções de validação.

---

# Módulo 09 - Funções Avançadas

Fonte editável:

```text
conteudos/secao_9/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- argumentos posicionais;
- argumentos nomeados;
- valores padrão;
- `*args`;
- `**kwargs`;
- funções lambda;
- funções como valores.

---

# Módulo 10 - Programação Orientada a Objetos

Fonte editável:

```text
conteudos/secao_10/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- classes;
- objetos;
- atributos;
- métodos;
- `__init__`;
- encapsulamento básico;
- herança;
- composição.

---

# Módulo 11 - Ambiente e Ferramentas

Fonte editável:

```text
conteudos/secao_11/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- ambiente virtual;
- instalação de pacotes;
- `pip`;
- organização de dependências;
- terminal;
- estrutura de projeto.

---

# Módulo 12 - Testes e Qualidade

Fonte editável:

```text
conteudos/secao_12/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- testes manuais;
- testes automatizados;
- `pytest`;
- casos de teste;
- refatoração segura;
- leitura de erros.

---

# Módulo 13 - Automação com Python

Fonte editável:

```text
conteudos/secao_13/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- automação de tarefas repetitivas;
- manipulação de arquivos em lote;
- scripts utilitários;
- entrada por terminal;
- relatórios simples.

---

# Módulo 14 - Dados Estruturados

Fonte editável:

```text
conteudos/secao_14/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- CSV;
- JSON;
- transformação de dados;
- filtros;
- agrupamentos;
- limpeza de dados.

---

# Módulo 15 - Projetos Intermediários

Fonte editável:

```text
conteudos/secao_15/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- projetos de terminal;
- cadastro;
- menu interativo;
- persistência simples;
- validação;
- organização por funções.

---

# Módulo 16 - Banco de Dados

Fonte editável:

```text
conteudos/secao_16/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- conceitos de banco;
- SQLite;
- conexão;
- criação de tabelas;
- inserção;
- consulta;
- atualização;
- remoção.

---

# Módulo 17 - APIs e Requisições

Fonte editável:

```text
conteudos/secao_17/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- HTTP;
- APIs;
- requisições;
- respostas JSON;
- tratamento de erros de rede;
- integração com serviços externos.

---

# Módulo 18 - Terminal e Produtividade

Fonte editável:

```text
conteudos/secao_18/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- argumentos de linha de comando;
- menus;
- scripts executáveis;
- produtividade no terminal;
- organização de utilitários.

---

# Módulo 19 - Aplicações Web ou Interfaces

Fonte editável:

```text
conteudos/secao_19/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- introdução a aplicações;
- rotas;
- entrada e saída;
- páginas simples;
- integração com projetos anteriores.

---

# Módulo 20 - Projeto Aplicado

Fonte editável:

```text
conteudos/secao_20/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- planejamento de projeto;
- requisitos;
- divisão em módulos;
- implementação incremental;
- testes;
- documentação.

---

# Módulo 21 - Revisão e Refatoração

Fonte editável:

```text
conteudos/secao_21/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- revisão de código;
- refatoração;
- nomes melhores;
- redução de duplicação;
- organização de funções;
- melhoria incremental.

---

# Módulo 22 - Portfólio e Documentação

Fonte editável:

```text
conteudos/secao_22/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- README de projeto;
- descrição de funcionalidades;
- prints e exemplos;
- instruções de execução;
- organização para GitHub.

---

# Módulo 23 - Fechamento e Próximos Passos

Fonte editável:

```text
conteudos/secao_23/
```

Estado atual: pasta preparada para receber conteúdo.

## Conteúdos previstos

- revisão geral;
- mapa do que foi aprendido;
- lacunas para revisar;
- próximos estudos;
- plano de continuidade.

---

# Cérebro Obsidian

O cérebro do curso fica em:

```text
doc_python/
```

Ele não substitui `conteudos/`. Ele documenta, conecta e explica a estrutura.

## Função do Obsidian

- criar mapas do curso;
- conectar seções;
- registrar decisões;
- apontar para arquivos editáveis;
- planejar módulos futuros;
- manter uma visão de longo prazo;
- servir como memória do projeto.

## Estrutura do cofre

```text
doc_python/
├── 00 - Início.md
├── 00 - Mapas/
├── 01 - Seções/
├── 02 - Blocos/
├── 03 - Manutenção/
└── 04 - Referências/
```

## Regra do cofre

Nunca altere manualmente:

```text
doc_python/.obsidian/
```

As notas ficam fora dessa pasta.

---

# Área Técnica

Esta seção existe para manutenção do repositório e para futuras atualizações automáticas ou assistidas.

## Publicação

O GitHub Pages publica a raiz do repositório. O site abre `index.html`, carrega `script.js` e renderiza este `README.md`.

## Como atualizar uma seção

1. Edite os arquivos em `conteudos/secao_X/`.
2. Atualize o `README.md` da própria seção.
3. Atualize ou crie notas em `doc_python/`.
4. Consolide a versão pública neste `README.md`.
5. Teste o site localmente.
6. Faça commit e push.

## Checklist antes de publicar

- O conteúdo público está no `README.md`.
- A fonte editável está em `conteudos/`.
- O cérebro está atualizado em `doc_python/`.
- `.obsidian` não foi alterado.
- Os links principais continuam funcionando.
- O site carrega sem erro no navegador.

## Comandos úteis

Executar servidor local:

```bash
python -m http.server 8017 --bind 127.0.0.1
```

Abrir site local:

```text
http://127.0.0.1:8017/
```

Listar arquivos da seção 3:

```bash
python tools/organizador.py --target conteudos/secao_3
```

Verificar alterações:

```bash
git status
```
