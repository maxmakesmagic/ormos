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

const paths = JSON.parse(readFileSync(0, "utf8"));
if (!Array.isArray(paths) || paths.some((path) => typeof path !== "string")) {
  throw new Error("Pass an array of relative HTML paths on standard input.");
}

try {
  const created = await createIndex();
  checkErrors(created, "Create Pagefind index");
  const { index } = created;

  for (const sourcePath of paths) {
    const content = await readFile(join(siteRoot, sourcePath), "utf8");
    const added = await index.addHTMLFile({ sourcePath, content });
    checkErrors(added, `Index ${sourcePath}`);
  }

  const written = await index.writeFiles({ outputPath });
  checkErrors(written, `Write Pagefind index to ${outputPath}`);
} finally {
  await close();
}
