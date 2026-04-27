const contentEl = document.getElementById("content");
const statusEl = document.getElementById("status");
const projectTitleEl = document.getElementById("project-title");
const projectSubtitleEl = document.getElementById("project-subtitle");
const heroTitleEl = document.getElementById("hero-title");
const heroDescriptionEl = document.getElementById("hero-description");
const themeToggleEl = document.getElementById("theme-toggle");
const tocToggleEl = document.getElementById("toc-toggle");
const tocListEl = document.getElementById("toc-list");
const pageListEl = document.getElementById("page-list");
const pageToolbarEl = document.getElementById("page-toolbar");
const pageSelectEl = document.getElementById("page-select");
const prevPageEl = document.getElementById("prev-page");
const nextPageEl = document.getElementById("next-page");
const pageProgressEl = document.getElementById("page-progress");
const searchInputEl = document.getElementById("manual-search");
const clearSearchEl = document.getElementById("clear-search");
const sectionCountEl = document.getElementById("section-count");
const commandCountEl = document.getElementById("command-count");

const README_PATH = "./README.md";
const THEME_KEY = "python-course-theme";
const themeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");

let fullMarkdown = "";
let pages = [];
let currentPageIndex = 0;
let headingRecords = [];
let activeObserver = null;
let renderSlugCounts = new Map();

function slugify(value) {
  return value
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^\w\s-]/g, "")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

function normalizeSearch(value) {
  return value
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

function plainTextFromTokens(tokens) {
  return tokens
    .map((token) => {
      if (token.text) return token.text;
      if (token.tokens) return plainTextFromTokens(token.tokens);
      return "";
    })
    .join(" ")
    .replace(/\s+/g, " ")
    .trim();
}

function extractIntro(markdown) {
  const lines = markdown.split(/\r?\n/);
  const firstParagraph = [];
  let passedTitle = false;

  for (const line of lines) {
    if (!passedTitle && line.startsWith("# ")) {
      passedTitle = true;
      continue;
    }

    if (!passedTitle) continue;
    if (!line.trim() && firstParagraph.length) break;
    if (line.trim()) firstParagraph.push(line.trim());
  }

  return firstParagraph.join(" ");
}

function getSystemTheme() {
  return themeMediaQuery.matches ? "dark" : "light";
}

function getStoredTheme() {
  try {
    return localStorage.getItem(THEME_KEY);
  } catch {
    return null;
  }
}

function setStoredTheme(theme) {
  try {
    localStorage.setItem(THEME_KEY, theme);
  } catch {
    // Local storage can be unavailable in restricted browser contexts.
  }
}

function applyTheme(theme) {
  document.documentElement.classList.remove("theme-light", "theme-dark");
  document.documentElement.classList.add(`theme-${theme}`);
  themeToggleEl.textContent = theme === "dark" ? "Claro" : "Escuro";
  themeToggleEl.setAttribute("aria-pressed", String(theme === "dark"));
}

function initializeTheme() {
  applyTheme(getStoredTheme() || getSystemTheme());
}

function configureMarkdown() {
  const renderer = new marked.Renderer();

  renderer.heading = ({ tokens, depth }) => {
    const text = marked.Parser.parseInline(tokens);
    const plainText = plainTextFromTokens(tokens) || text.replace(/<[^>]+>/g, "");
    const baseSlug = slugify(plainText || "secao");
    const count = renderSlugCounts.get(baseSlug) || 0;
    renderSlugCounts.set(baseSlug, count + 1);
    const slug = count === 0 ? baseSlug : `${baseSlug}-${count}`;

    return `
      <h${depth} id="${slug}">
        ${text}
        <a class="heading-anchor" href="#${slug}" aria-label="Link para ${plainText}">#</a>
      </h${depth}>
    `;
  };

  marked.setOptions({
    gfm: true,
    breaks: false,
    headerIds: false,
    mangle: false,
    renderer,
  });
}

function updatePageMetadata(markdown) {
  const headingMatch = markdown.match(/^#\s+(.+)$/m);
  const title = headingMatch ? headingMatch[1].trim() : "Curso Python";
  const intro = extractIntro(markdown);

  document.title = `${title} | Curso Python`;
  projectTitleEl.textContent = title;
  projectSubtitleEl.textContent = "Lógica, dados e projetos";
  heroTitleEl.textContent = title;
  heroDescriptionEl.textContent =
    intro || "Curso de Python organizado em ordem cronológica de aprendizado.";
}

function createUniqueSlug(title, usedSlugs) {
  const base = slugify(title || "pagina") || "pagina";
  const count = usedSlugs.get(base) || 0;
  usedSlugs.set(base, count + 1);
  return count === 0 ? base : `${base}-${count}`;
}

function getMarkdownHeadings(markdown) {
  const lines = markdown.split(/\r?\n/);
  let openFence = null;
  const usedSlugs = new Map();
  const headings = [];

  lines.forEach((line) => {
    const fenceMatch = line.match(/^\s*(`{3,}|~{3,})/);
    if (fenceMatch) {
      const marker = fenceMatch[1];
      if (!openFence) {
        openFence = marker;
        return;
      }

      if (marker[0] === openFence[0] && marker.length >= openFence.length) {
        openFence = null;
      }

      return;
    }

    if (openFence) return;

    const headingMatch = line.match(/^(#{1,3})\s+(.+)$/);
    if (!headingMatch) return;

    const title = headingMatch[2].trim();
    headings.push({
      depth: headingMatch[1].length,
      title,
      slug: createUniqueSlug(title, usedSlugs),
    });
  });

  return headings;
}

function classifyPage(page) {
  if (page.title === "Visão geral") {
    return { group: "Visão geral", label: "Início", title: "Apresentação" };
  }

  const aulaMatch = page.title.match(/^Aula\s+(\d+)\s*-\s*(.+)$/i);
  if (aulaMatch) {
    return {
      group: "Aulas da sessão",
      label: `Aula ${aulaMatch[1].padStart(2, "0")}`,
      title: aulaMatch[2],
    };
  }

  const moduloMatch = page.title.match(/^Módulo\s+(\d+)\s*-\s*(.+)$/i);
  if (moduloMatch) {
    return {
      group: "Módulos da trilha",
      label: `Módulo ${moduloMatch[1].padStart(2, "0")}`,
      title: moduloMatch[2],
    };
  }

  if (/revisão|gabarito|critérios/i.test(page.title)) {
    return { group: "Revisão e apoio", label: "Apoio", title: page.title };
  }

  if (/projeto/i.test(page.title)) {
    return { group: "Projetos", label: "Projeto", title: page.title };
  }

  return { group: "Outras páginas", label: "Página", title: page.title };
}

function parsePages(markdown) {
  const lines = markdown.split(/\r?\n/);
  let openFence = null;
  const headingIndexes = [];

  lines.forEach((line, index) => {
    const fenceMatch = line.match(/^\s*(`{3,}|~{3,})/);
    if (fenceMatch) {
      const marker = fenceMatch[1];
      if (!openFence) {
        openFence = marker;
        return;
      }

      if (marker[0] === openFence[0] && marker.length >= openFence.length) {
        openFence = null;
      }

      return;
    }

    if (!openFence && /^#\s+/.test(line)) {
      headingIndexes.push(index);
    }
  });

  const titleLineIndex = headingIndexes[0] ?? -1;
  const titleIndex = titleLineIndex === -1 ? -1 : titleLineIndex;
  const starts = headingIndexes.filter((index) => index !== titleIndex);

  const usedSlugs = new Map();
  const parsedPages = [];
  const preambleStart = titleIndex === -1 ? 0 : titleIndex + 1;
  const firstPageStart = starts[0] ?? lines.length;
  const preamble = lines.slice(preambleStart, firstPageStart).join("\n").trim();

  if (preamble) {
    const title = "Visão geral";
    const pageMarkdown = `# ${title}\n\n${preamble}`;
    parsedPages.push({
      title,
      slug: createUniqueSlug(title, usedSlugs),
      markdown: pageMarkdown,
      headingSlugs: getMarkdownHeadings(pageMarkdown).map((heading) => heading.slug),
      searchableText: normalizeSearch(`${title} ${preamble}`),
    });
  }

  starts.forEach((start, index) => {
    const end = starts[index + 1] ?? lines.length;
    const markdownChunk = lines.slice(start, end).join("\n").trim();
    const title = lines[start].replace(/^#\s+/, "").trim() || `Página ${index + 1}`;

    parsedPages.push({
      title,
      slug: createUniqueSlug(title, usedSlugs),
      markdown: markdownChunk,
      headingSlugs: getMarkdownHeadings(markdownChunk).map((heading) => heading.slug),
      searchableText: normalizeSearch(`${title} ${markdownChunk}`),
    });
  });

  if (!parsedPages.length && markdown.trim()) {
    const title = "Conteúdo";
    const pageMarkdown = `# ${title}\n\n${markdown}`;
    parsedPages.push({
      title,
      slug: createUniqueSlug(title, usedSlugs),
      markdown: pageMarkdown,
      headingSlugs: getMarkdownHeadings(pageMarkdown).map((heading) => heading.slug),
      searchableText: normalizeSearch(`${title} ${markdown}`),
    });
  }

  return parsedPages;
}

function enhanceLinksAndImages() {
  contentEl.querySelectorAll("a[href]").forEach((link) => {
    const href = link.getAttribute("href");
    if (!href) return;

    if (/^https?:\/\//i.test(href)) {
      link.target = "_blank";
      link.rel = "noreferrer noopener";
    }
  });

  contentEl.querySelectorAll("img").forEach((image) => {
    image.loading = "lazy";
    image.decoding = "async";
  });
}

function addCopyButtons() {
  contentEl.querySelectorAll("pre").forEach((pre) => {
    const code = pre.querySelector("code");
    if (!code) return;

    const button = document.createElement("button");
    button.className = "copy-button";
    button.type = "button";
    button.textContent = "Copiar";
    button.setAttribute("aria-label", "Copiar código");

    button.addEventListener("click", async () => {
      const text = code.innerText.trim();
      try {
        await navigator.clipboard.writeText(text);
        button.textContent = "Copiado";
        window.setTimeout(() => {
          button.textContent = "Copiar";
        }, 1400);
      } catch {
        button.textContent = "Erro";
        window.setTimeout(() => {
          button.textContent = "Copiar";
        }, 1400);
      }
    });

    pre.appendChild(button);
  });
}

function collectHeadings() {
  headingRecords = [...contentEl.querySelectorAll("h2, h3")].map((heading) => ({
    id: heading.id,
    title: heading.textContent.replace("#", "").trim(),
    depth: Number(heading.tagName.slice(1)),
    element: heading,
  }));
}

function buildToc() {
  tocListEl.innerHTML = "";

  if (!headingRecords.length) {
    const empty = document.createElement("span");
    empty.className = "toc-empty";
    empty.textContent = "Sem subtítulos nesta página.";
    tocListEl.appendChild(empty);
    return;
  }

  headingRecords.forEach((record) => {
    const link = document.createElement("a");
    link.href = `#${record.id}`;
    link.textContent = record.title;
    link.dataset.target = record.id;
    link.className = `toc-depth-${record.depth}`;
    tocListEl.appendChild(link);
  });
}

function setActiveTocLink(id) {
  tocListEl.querySelectorAll("a").forEach((link) => {
    link.classList.toggle("is-active", link.dataset.target === id);
  });
}

function observeActiveSections() {
  if (activeObserver) activeObserver.disconnect();
  if (!headingRecords.length) return;

  activeObserver = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);

      if (visible[0]) {
        setActiveTocLink(visible[0].target.id);
      }
    },
    {
      rootMargin: "-20% 0px -65% 0px",
      threshold: 0,
    }
  );

  headingRecords.forEach((record) => activeObserver.observe(record.element));
}

function updateMetrics(markdown) {
  const codeCount = (markdown.match(/^```/gm) || []).length / 2;

  sectionCountEl.textContent = String(pages.length);
  commandCountEl.textContent = String(Math.floor(codeCount));
}

function buildPageNavigation() {
  pageListEl.innerHTML = "";
  pageSelectEl.innerHTML = "";
  let currentGroup = "";

  pages.forEach((page, index) => {
    const meta = classifyPage(page);

    if (meta.group !== currentGroup) {
      currentGroup = meta.group;
      const groupTitle = document.createElement("span");
      groupTitle.className = "page-group";
      groupTitle.textContent = currentGroup;
      pageListEl.appendChild(groupTitle);
    }

    const link = document.createElement("a");
    link.href = `#${page.slug}`;
    link.dataset.pageIndex = String(index);
    link.innerHTML = `
      <span class="page-kicker">${meta.label}</span>
      <span class="page-title">${meta.title}</span>
    `;
    pageListEl.appendChild(link);

    const option = document.createElement("option");
    option.value = String(index);
    option.textContent = page.title;
    pageSelectEl.appendChild(option);
  });
}

function updatePageNavigation() {
  pageListEl.querySelectorAll("a").forEach((link) => {
    link.classList.toggle("is-active", Number(link.dataset.pageIndex) === currentPageIndex);
  });

  const page = pages[currentPageIndex];
  const meta = page ? classifyPage(page) : null;

  pageSelectEl.value = String(currentPageIndex);
  prevPageEl.disabled = currentPageIndex === 0;
  nextPageEl.disabled = currentPageIndex === pages.length - 1;
  pageProgressEl.textContent = meta ? `${meta.label} · ${meta.title}` : "";
}

function getSectionBlocks() {
  const headings = [...contentEl.querySelectorAll("h2")];
  return headings.map((heading, index) => {
    const nodes = [];
    let node = heading;
    const nextHeading = headings[index + 1];

    while (node && node !== nextHeading) {
      nodes.push(node);
      node = node.nextElementSibling;
    }

    return {
      heading,
      headingIds: nodes
        .filter((item) => /^H[23]$/.test(item.tagName))
        .map((item) => item.id),
      nodes,
      text: normalizeSearch(nodes.map((item) => item.textContent).join(" ")),
    };
  });
}

function applySearchFilter() {
  const term = normalizeSearch(searchInputEl.value.trim());
  const blocks = getSectionBlocks();

  clearSearchEl.hidden = !term;

  pages.forEach((page, index) => {
    const link = pageListEl.querySelector(`[data-page-index="${index}"]`);
    if (!link) return;
    link.classList.toggle("is-hidden-by-search", Boolean(term && !page.searchableText.includes(term)));
  });

  if (!blocks.length) return;

  blocks.forEach((block) => {
    const matches = !term || block.text.includes(term);
    block.nodes.forEach((node) => {
      node.classList.toggle("is-hidden-by-search", !matches);
    });
  });

  tocListEl.querySelectorAll("a").forEach((link) => {
    const block = blocks.find((item) => item.headingIds.includes(link.dataset.target));
    link.classList.toggle("is-hidden-by-search", Boolean(term && block && !block.text.includes(term)));
  });
}

function enhanceRenderedContent(markdown) {
  const firstHeading = contentEl.querySelector("h1");
  if (firstHeading) firstHeading.remove();

  contentEl.querySelectorAll("pre code").forEach((block) => {
    hljs.highlightElement(block);
  });

  enhanceLinksAndImages();
  addCopyButtons();
  collectHeadings();
  buildToc();
  observeActiveSections();
  updateMetrics(fullMarkdown || markdown);
}

function renderPage(index, options = {}) {
  if (!pages.length) return;

  currentPageIndex = Math.min(Math.max(index, 0), pages.length - 1);
  const page = pages[currentPageIndex];
  renderSlugCounts = new Map();
  contentEl.innerHTML = marked.parse(page.markdown);
  enhanceRenderedContent(page.markdown);
  updatePageNavigation();
  applySearchFilter();

  statusEl.hidden = true;
  contentEl.hidden = false;
  pageToolbarEl.hidden = pages.length <= 1;

  if (options.scroll !== false) {
    const target = options.targetId ? document.getElementById(options.targetId) : null;
    const scrollTarget = target || document.getElementById("manual");
    window.requestAnimationFrame(() => scrollTarget.scrollIntoView({ block: "start" }));
  }
}

function showError(message) {
  statusEl.innerHTML = `
    <div class="empty-state">
      <h2>Não foi possível carregar o README</h2>
      <p>${message}</p>
    </div>
  `;
}

function findPageByHash(hash) {
  if (!hash) return { index: 0, targetId: "" };

  const pageIndex = pages.findIndex((page) => page.slug === hash);
  if (pageIndex !== -1) return { index: pageIndex, targetId: "" };

  const headingPageIndex = pages.findIndex((page) => page.headingSlugs.includes(hash));
  if (headingPageIndex !== -1) return { index: headingPageIndex, targetId: hash };

  return { index: 0, targetId: "" };
}

function getInitialPageTarget() {
  const hash = decodeURIComponent(window.location.hash.replace(/^#/, ""));
  return findPageByHash(hash);
}

async function renderReadme() {
  try {
    const response = await fetch(README_PATH, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Falha ao buscar ${README_PATH}: ${response.status}`);
    }

    fullMarkdown = await response.text();
    if (!fullMarkdown.trim()) {
      throw new Error("O arquivo README.md está vazio.");
    }

    updatePageMetadata(fullMarkdown);
    pages = parsePages(fullMarkdown);
    buildPageNavigation();
    const initialTarget = getInitialPageTarget();
    renderPage(initialTarget.index, { scroll: false, targetId: initialTarget.targetId });
    if (initialTarget.targetId) {
      window.requestAnimationFrame(() => {
        document.getElementById(initialTarget.targetId)?.scrollIntoView({ block: "start" });
      });
    }
  } catch (error) {
    console.error(error);
    const isFileProtocol = window.location.protocol === "file:";
    const hint = isFileProtocol
      ? "Seu navegador pode bloquear o carregamento de arquivos locais via fetch. Abra por um servidor local, como python -m http.server."
      : "Verifique se README.md está na mesma pasta de index.html.";

    showError(`${error.message} ${hint}`);
  }
}

function isCompactToc() {
  return window.matchMedia("(max-width: 980px)").matches;
}

function setTocOpen(isOpen) {
  document.body.classList.toggle("toc-open", isOpen);
  tocToggleEl.setAttribute("aria-expanded", String(isOpen));
}

function focusTocPanel() {
  searchInputEl.focus({ preventScroll: true });
}

function handleTocToggle() {
  if (isCompactToc()) {
    const willOpen = !document.body.classList.contains("toc-open");
    setTocOpen(willOpen);

    if (willOpen) {
      document.getElementById("manual").scrollIntoView({ block: "start" });
      window.setTimeout(focusTocPanel, 180);
    }

    return;
  }

  setTocOpen(false);
  document.querySelector(".sidebar-panel").scrollIntoView({ block: "nearest" });
  focusTocPanel();
}

function goToPage(index) {
  renderPage(index);
  const page = pages[currentPageIndex];
  if (page) {
    history.replaceState(null, "", `#${encodeURIComponent(page.slug)}`);
  }
}

themeToggleEl.addEventListener("click", () => {
  const nextTheme = document.documentElement.classList.contains("theme-dark") ? "light" : "dark";
  setStoredTheme(nextTheme);
  applyTheme(nextTheme);
});

tocToggleEl.addEventListener("click", handleTocToggle);

tocListEl.addEventListener("click", (event) => {
  if (event.target.closest("a") && isCompactToc()) {
    setTocOpen(false);
  }
});

pageListEl.addEventListener("click", (event) => {
  const link = event.target.closest("a[data-page-index]");
  if (!link) return;

  event.preventDefault();
  goToPage(Number(link.dataset.pageIndex));

  if (isCompactToc()) {
    setTocOpen(false);
  }
});

pageSelectEl.addEventListener("change", () => {
  goToPage(Number(pageSelectEl.value));
});

prevPageEl.addEventListener("click", () => {
  goToPage(currentPageIndex - 1);
});

nextPageEl.addEventListener("click", () => {
  goToPage(currentPageIndex + 1);
});

window.addEventListener("hashchange", () => {
  const target = findPageByHash(decodeURIComponent(window.location.hash.replace(/^#/, "")));
  renderPage(target.index, { targetId: target.targetId });
});

window.addEventListener("resize", () => {
  if (!isCompactToc()) {
    setTocOpen(false);
  }
});

searchInputEl.addEventListener("input", applySearchFilter);

clearSearchEl.addEventListener("click", () => {
  searchInputEl.value = "";
  applySearchFilter();
  searchInputEl.focus();
});

function handleSystemThemeChange(event) {
  if (!getStoredTheme()) {
    applyTheme(event.matches ? "dark" : "light");
  }
}

if (typeof themeMediaQuery.addEventListener === "function") {
  themeMediaQuery.addEventListener("change", handleSystemThemeChange);
} else if (typeof themeMediaQuery.addListener === "function") {
  themeMediaQuery.addListener(handleSystemThemeChange);
}

initializeTheme();
configureMarkdown();
renderReadme();
