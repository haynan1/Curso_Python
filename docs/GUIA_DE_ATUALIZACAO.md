# Guia de atualização de novas sessões

Use este fluxo sempre que adicionar uma nova sessão ao curso.

## 1. Criar a pasta da sessão

Crie uma pasta com numeração estável:

```text
conteudos/secao_04/
conteudos/secao_05/
```

Prefira dois dígitos quando a seção for nova. A pasta atual permanece como `secao_3` para preservar o histórico já versionado.

## 2. Criar o índice da sessão

Copie `templates/nova_sessao.md` para dentro da nova pasta como `README.md`.

Preencha:

- objetivo da sessão
- pré-requisitos
- ordem das aulas
- critérios para avançar

## 3. Adicionar aulas

Use nomes previsíveis:

```text
01 - aula01.py
02 - aula02.py
03 - aula03.py
```

Para uma aula nova, copie `templates/nova_aula.py` e ajuste título, objetivo, exemplos e exercícios.

## 4. Consolidar no site

Quando a sessão estiver pronta, transfira a explicação final para o `README.md` da raiz usando este padrão:

````md
# Módulo 13 - Funções em Python

Introdução curta.

## Objetivo

- Objetivo 1
- Objetivo 2

## Explicação

Conteúdo didático.

## Exemplo

```python
def saudacao():
    print("Olá, Python")
```

## Exercícios

1. Exercício simples.
2. Exercício intermediário.
3. Exercício de revisão.
````

## 5. Conferir antes de publicar

- O `README.md` da raiz abre no site sem erro.
- Os títulos principais usam apenas um `#`.
- Os subtítulos usam `##` ou `###`.
- Blocos de código usam três crases.
- Arquivos temporários, logs e ambientes virtuais não entram no Git.
