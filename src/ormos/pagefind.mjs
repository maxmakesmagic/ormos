import { readFileSync } from "node:fs";
import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { close, createIndex } from "pagefind";

function checkErrors({ errors }, action) {
  if (errors.length) {
    throw new Error(`${action}: ${errors.join("\n")}`);
  }
}

const [siteRoot, outputPath] = process.argv.slice(-2);
if (process.argv.length < 3 || !siteRoot || !outputPath) {
  throw new Error("Pass the site root and the search output directory.");
}

// Read piped input as bytes to avoid Node's UTF-8 pipe bug (nodejs/node#66341).
const sources = JSON.parse(readFileSync(0).toString("utf8"));
if (!Array.isArray(sources)) {
  throw new Error("Pass an array of HTML paths or title records on standard input.");
}

try {
  const created = await createIndex();
  checkErrors(created, "Create Pagefind index");
  const { index } = created;

  for (const source of sources) {
    if (typeof source === "string") {
      const content = await readFile(join(siteRoot, source), "utf8");
      const added = await index.addHTMLFile({ sourcePath: source, content });
      checkErrors(added, `Index ${source}`);
    } else {
      const added = await index.addCustomRecord(source);
      checkErrors(added, `Index title at ${source.url}`);
    }
  }

  const written = await index.writeFiles({ outputPath });
  checkErrors(written, `Write Pagefind index to ${outputPath}`);
} finally {
  await close();
}
