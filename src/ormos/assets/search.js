const form = document.querySelector("#search");
const input = document.querySelector("#query");
const scope = form.elements.namedItem("scope");
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
  const parsed = new DOMParser().parseFromString(html || "", "text/html");
  const summary = document.createElement("p");
  for (const node of parsed.body.childNodes) {
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
  link.textContent = meta.title || "Archived document";
  item.append(link);
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
  } else {
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

async function loadEngine(titlesOnly) {
  const manifest = titlesOnly ? "/pagefind/titles/shards.json" : "/pagefind/shards.json";
  const [module, response] = await Promise.all([
    import("/pagefind/pagefind.js"), fetch(manifest),
  ]);
  if (!response.ok) throw new Error("Search index unavailable");
  const shards = await response.json();
  const language = document.documentElement.lang.toLowerCase();
  const paths = shards[language];
  if (!paths?.length) return null;
  const [primary, ...remaining] = paths;
  const instance = module.createInstance({ basePath: primary });
  await instance.init();
  await Promise.all(remaining.map((path) => instance.mergeIndex(path)));
  return instance;
}

function engineFor(titlesOnly) {
  if (!engines.has(titlesOnly)) {
    engines.set(titlesOnly, loadEngine(titlesOnly).catch((error) => {
      engines.delete(titlesOnly);
      throw error;
    }));
  }
  return engines.get(titlesOnly);
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
  const titlesOnly = scope?.value === "titles";
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
    const index = await engineFor(titlesOnly);
    const response = index ? await index.search(term || null, { filters }) : { results: [] };
    if (version !== searchVersion) return;
    matches = response.results;
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
  // Bookmarked searches without a scope still use the full-text index.
  if (scope) {
    scope.value = query.get("scope") === "text" || (!query.has("scope") && query.has("q"))
      ? "text" : "titles";
  }
  for (const select of filterInputs) {
    const value = query.get(select.name);
    select.value = facetLabels[select.name].has(value) ? value : "";
  }
  showFilters();
  search();
}

function updateQuery() {
  showFilters();
  const query = new URLSearchParams(activeFilters());
  if (scope) query.set("scope", scope.value);
  const term = input.value.trim();
  if (term) query.set("q", term);
  const url = new URL(form.action);
  url.search = query;
  if (location.href !== url.href) history.pushState(null, "", url);
  search();
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  updateQuery();
});
scope?.addEventListener("change", updateQuery);
filterPanel?.addEventListener("change", updateQuery);
more.addEventListener("click", () => showMore(searchVersion));
window.addEventListener("popstate", restoreQuery);
restoreQuery();
