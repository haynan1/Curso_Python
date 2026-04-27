# Estrutura do repositório

Este repositório tem duas camadas principais: o site público do curso e os materiais de apoio usados para evoluir novas sessões.

## Raiz

- `index.html`: página principal do curso.
- `style.css`: estilos do site.
- `script.js`: carrega e renderiza o `README.md` no navegador.
- `README.md`: conteúdo publicado no site.
- `assets/`: imagens e ícones usados pela página.
- `LICENSE`: licença do projeto.

## Conteúdos

- `conteudos/README.md`: visão rápida da área de conteúdos.
- `conteudos/secao_3/`: arquivos Python da seção atual do curso.
- `conteudos/secao_3/README.md`: índice e convenções da seção 3.

## Manutenção

- `docs/`: documentação interna de organização e atualização.
- `templates/`: modelos para criar novas sessões, aulas e páginas.
- `tools/`: scripts utilitários que ajudam a organizar arquivos.

## Regra de ouro

O site lê o conteúdo diretamente de `README.md`. Ao criar novas sessões, atualize primeiro os arquivos de apoio em `conteudos/` e depois consolide a versão didática final no `README.md`.
