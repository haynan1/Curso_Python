# Prompt Fixo Codex

Use este prompt quando quiser que o Codex se situe antes de alterar o curso.

## Comando curto

Quando eu disser:

```text
Atualize a estrutura conforme as regras
```

interprete como:

- leia este prompt fixo;
- leia o cofre Obsidian;
- confira `conteudos/`;
- atualize a estrutura de forma coerente;
- preserve `doc_python/.obsidian/`;
- atualize README público, READMEs das seções e notas do Obsidian quando necessário;
- valide links e estrutura antes de finalizar.

## Prompt

```text
Antes de alterar qualquer arquivo, leia e entenda a estrutura do projeto.

1. Comece pelo cofre Obsidian em `doc_python/`.
   - Abra `doc_python/00 - Início.md`.
   - Depois leia `doc_python/00 - Mapas/Mapa do Curso.md`.
   - Depois leia `doc_python/00 - Mapas/Mapa dos Conteúdos.md`.
   - Se a tarefa envolver uma seção específica, leia a nota correspondente em `doc_python/01 - Seções/`.

2. Nunca edite manualmente nada dentro de:
   `doc_python/.obsidian/`

3. Depois confira a fonte editável em `conteudos/`.
   - Cada seção do curso fica em `conteudos/secao_X/`.
   - Os arquivos Python são a fonte prática e podem ser alterados.
   - O `README.md` de cada seção deve explicar objetivo, ordem, arquivos e critérios.

4. Se atualizar conteúdo de aula:
   - atualize os arquivos em `conteudos/secao_X/`;
   - atualize o `README.md` da seção;
   - atualize as notas relacionadas em `doc_python/`;
   - atualize o `README.md` da raiz se isso precisar aparecer no GitHub Pages.

5. O `README.md` da raiz é a versão pública do curso.
   - Ele deve continuar organizado por módulos.
   - A parte técnica deve ficar separada na seção `Área Técnica`.
   - Não coloque rascunhos soltos no README público.

6. Antes de finalizar:
   - valide se os links do Obsidian continuam coerentes;
   - confira se todas as seções em `conteudos/` continuam documentadas;
   - teste ou pelo menos valide o site local;
   - informe exatamente quais arquivos foram alterados.

Agora execute a tarefa solicitada respeitando essa estrutura.
```

## Como usar

Copie o prompt acima e cole no início de uma conversa com o Codex quando quiser fazer manutenção estruturada no curso.

Depois do prompt, escreva a tarefa específica.

Exemplo:

```text
[cole o prompt fixo aqui]

Agora atualize a seção 4 com aulas sobre funções, parâmetros e retorno.
```

## Links úteis

- [[00 - Início|Início do Cofre]]
- [[00 - Mapas/Mapa do Curso|Mapa do Curso]]
- [[00 - Mapas/Mapa dos Conteúdos|Mapa dos Conteúdos]]
- [[Fluxo de Atualização]]
- [[Publicação no GitHub Pages]]
