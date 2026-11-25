const form = document.querySelector("#search");
const input = document.querySelector("#query");
const status = document.querySelector("#search-status");
const results = document.querySelector("#search-results");

const more = document.createElement("button");
more.type = "button";
more.textContent = "Show more results";
more.hidden = true;
results.after(more);

const batchSize = 25;
let searchVersion = 0;
let matches = [];
let rendered = 0;
let engine;

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

function resultRow(documentResult) {
  const { url, meta, excerpt: snippet } = documentResult;
  const destination = new URL(url, location.origin);
  if (destination.origin !== location.origin) return null;
  const item = document.createElement("li");
  const link = document.createElement("a");
  link.href = destination.pathname.replace(/\/index\.html$/, "/");
  link.textContent = meta.title || "Archived document";
  item.append(link, excerpt(snippet));
  return item;
}

async function showMore(version) {
  more.disabled = true;
  const batchEnd = Math.min(matches.length, rendered + batchSize);
  try {
    const pages = await Promise.all(matches.slice(rendered, batchEnd).map((result) => result.data()));
    if (version !== searchVersion) return;
    const rows = pages.map(resultRow).filter(Boolean);
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

async function loadEngine() {
  const [module, response] = await Promise.all([
    import("/pagefind/pagefind.js"), fetch("/pagefind/shards.json"),
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

async function search(term) {
  const version = ++searchVersion;
  results.replaceChildren();
  more.hidden = true;
  matches = [];
  rendered = 0;
  if (!term) {
    status.textContent = "";
    return;
  }
  status.textContent = "Searching…";
  try {
    engine ??= loadEngine().catch((error) => {
      engine = undefined;
      throw error;
    });
    const index = await engine;
    const response = index ? await index.search(term) : { results: [] };
    if (version !== searchVersion) return;
    matches = response.results;
    if (matches.length) {
      await showMore(version);
    } else {
      status.textContent = "No matching documents.";
    }
  } catch {
    if (version === searchVersion) status.textContent = "Search could not load. Please retry.";
  }
}

function restoreQuery() {
  input.value = new URLSearchParams(location.search).get("q") || "";
  search(input.value.trim());
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const query = new URLSearchParams({ q: input.value.trim() });
  history.pushState(null, "", `${new URL(form.action).pathname}?${query}`);
  search(input.value.trim());
});
more.addEventListener("click", () => showMore(searchVersion));
window.addEventListener("popstate", restoreQuery);
restoreQuery();
