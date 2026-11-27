const form = document.querySelector("#search");
const input = document.querySelector("#query");
const scope = form.elements.namedItem("scope");
const language = document.querySelector("#search-language");
const filterPanel = document.querySelector("#search-filters");
const filterInputs = [...(filterPanel?.querySelectorAll("select") || [])];
const status = document.querySelector("#search-status");
const results = document.querySelector("#search-results");

const more = document.createElement("button");
more.type = "button";
more.textContent = "Show more results";
more.hidden = true;
results.after(more);

const batchSize = 25;
const engines = new Map();
const mediaLabels = new Map([["podcast", "Podcast"], ["video", "Video"]]);
const manifests = {
  articles: "/pagefind/shards.json",
  titles: "/pagefind/titles/shards.json",
  media: "/pagefind/media/shards.json",
};
const facetLabels = Object.fromEntries(
  filterInputs.map((select) => [
    select.name,
    new Map([...select.options].map((option) => [option.value, option.textContent])),
  ]),
);
let searchVersion = 0;
let matches = [];
let rendered = 0;

function excerpt(html) {
  const source = document.createElement("template");
  source.innerHTML = html;
  const summary = document.createElement("p");
  for (const node of source.content.childNodes) {
    if (node.nodeName === "MARK") {
      const highlighted = document.createElement("mark");
      highlighted.textContent = node.textContent;
      summary.append(highlighted);
    } else {
      summary.append(node.textContent || "");
    }
  }
  return summary;
}

function resultRow(documentResult, titlesOnly) {
  const { url, meta, filters, excerpt: snippet } = documentResult;
  const destination = new URL(url, location.origin);
  if (destination.origin !== location.origin) return null;
  const item = document.createElement("li");
  const link = document.createElement("a");
  link.href = destination.pathname.replace(/\/index\.html$/, "/");
  const mediaLabel = mediaLabels.get(meta.kind);
  link.textContent = meta.title || mediaLabel || "Archived document";
  item.append(link);
  if (mediaLabel) {
    const label = document.createElement("span");
    label.className = "count";
    label.textContent = mediaLabel;
    item.append(" · ", label);
  }
  if (titlesOnly) {
    const details = ["author", "column", "year"].flatMap((field) =>
      (filters?.[field] || []).map((value) => facetLabels[field]?.get(value)).filter(Boolean)
    );
    if (details.length) {
      const byline = document.createElement("p");
      byline.className = "record-meta";
      byline.textContent = details.join(" · ");
      item.append(byline);
    }
  } else if (snippet) {
    item.append(excerpt(snippet));
  }
  return item;
}

async function showMore(version) {
  more.disabled = true;
  const batchEnd = Math.min(matches.length, rendered + batchSize);
  try {
    const pages = await Promise.all(matches.slice(rendered, batchEnd).map((result) => result.data()));
    if (version !== searchVersion) return;
    const rows = pages.map((page) => resultRow(page, scope?.value === "titles")).filter(Boolean);
    results.append(...rows);
    rendered = batchEnd;
    status.textContent = `Showing ${rendered.toLocaleString()} of ${matches.length.toLocaleString()} results.`;
    more.hidden = rendered >= matches.length;
  } catch {
    if (version === searchVersion) status.textContent = "These search results could not load. Please retry.";
  } finally {
    if (version === searchVersion) more.disabled = false;
  }
}

async function loadEngine(source) {
  const response = await fetch(manifests[source]);
  if (!response.ok) throw new Error("Search index unavailable");
  const shards = await response.json();
  const locale = document.documentElement.lang.toLowerCase();
  const paths = shards[locale];
  if (!paths?.length) return null;
  const [primary, ...remaining] = paths;
  // Pagefind shares a WASM instance within a module. Isolate each source.
  const module = await import(`/pagefind/pagefind.js?index=${source}`);
  const instance = module.createInstance({ basePath: primary });
  await instance.init();
  await Promise.all(remaining.map((path) => instance.mergeIndex(path)));
  return instance;
}

function engineFor(source) {
  if (!engines.has(source)) {
    engines.set(source, loadEngine(source).catch((error) => {
      engines.delete(source);
      throw error;
    }));
  }
  return engines.get(source);
}

function activeFilters() {
  if (scope?.value !== "titles") return {};
  return Object.fromEntries(
    filterInputs.filter((select) => select.value).map((select) => [select.name, select.value]),
  );
}

function showFilters() {
  if (!filterPanel) return;
  const titlesOnly = scope?.value === "titles";
  filterPanel.hidden = !titlesOnly;
  filterPanel.disabled = !titlesOnly;
}

async function search() {
  const version = ++searchVersion;
  const term = input.value.trim();
  const selected = scope.value;
  const titlesOnly = selected === "titles";
  const filters = activeFilters();
  results.replaceChildren();
  more.hidden = true;
  matches = [];
  rendered = 0;
  if (!term && !Object.keys(filters).length) {
    status.textContent = "";
    return;
  }
  status.textContent = "Searching…";
  try {
    const searchArticles = titlesOnly || selected === "text" || selected === "article";
    const mediaType = mediaLabels.has(selected) ? selected : null;
    const searchMedia = form.hasAttribute("data-media-search") && (selected === "text" || mediaType !== null);
    const [articles, media] = await Promise.all([
      searchArticles && engineFor(titlesOnly ? "titles" : "articles"),
      searchMedia && engineFor("media"),
    ]);
    if (version !== searchVersion) return;
    const mediaFilters = mediaType ? { media: mediaType } : {};
    const responses = await Promise.all([
      articles && articles.search(term || null, { filters }),
      media && media.search(term, { filters: mediaFilters }),
    ]);
    if (version !== searchVersion) return;
    matches = responses.flatMap((response) => response?.results || []);
    if (articles && media) matches.sort((a, b) => b.score - a.score);
    if (matches.length) {
      await showMore(version);
    } else {
      status.textContent = titlesOnly ? "No matching articles." : "No matching documents.";
    }
  } catch {
    if (version === searchVersion) status.textContent = "Search could not load. Please retry.";
  }
}

function restoreQuery() {
  const query = new URLSearchParams(location.search);
  input.value = query.get("q") || "";
  const selected = query.get("scope");
  scope.value = [...scope.options].some((option) => option.value === selected) ? selected : "text";
  language.value = document.documentElement.lang.toLowerCase();
  for (const select of filterInputs) {
    const value = query.get(select.name);
    select.value = facetLabels[select.name].has(value) ? value : "";
  }
  showFilters();
  search();
}

function updateQuery() {
  showFilters();
  const local = language.value === document.documentElement.lang.toLowerCase();
  const query = new URLSearchParams(activeFilters());
  if (scope.value !== "text") query.set("scope", scope.value);
  const term = input.value.trim();
  if (term) query.set("q", term);
  const url = new URL(language.selectedOptions[0].dataset.path, location.origin);
  url.search = query;
  if (!local) {
    location.assign(url);
    return;
  }
  if (location.href !== url.href) history.pushState(null, "", url);
  search();
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  updateQuery();
});
const languageNames = new Intl.DisplayNames(["en"], { type: "language" });
for (const option of language.options) {
  const name = languageNames.of(option.value);
  if (name !== option.value) option.textContent = name;
}
scope.addEventListener("change", updateQuery);
language.addEventListener("change", updateQuery);
filterPanel?.addEventListener("change", updateQuery);
more.addEventListener("click", () => showMore(searchVersion));
window.addEventListener("popstate", restoreQuery);
window.addEventListener("pageshow", restoreQuery);
