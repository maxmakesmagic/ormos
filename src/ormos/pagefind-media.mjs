import { readFileSync } from "node:fs";
import { close, createIndex } from "pagefind";

function checkErrors({ errors }, action) {
  if (errors.length) {
    throw new Error(`${action}: ${errors.join("\n")}`);
  }
}

const [, outputPath] = process.argv;
if (!outputPath) {
  throw new Error("Pass the media search output directory.");
}

// Decode bytes in one step so split UTF-8 characters survive piped input.
const records = JSON.parse(readFileSync(0).toString("utf8"));

try {
  const created = await createIndex();
  checkErrors(created, "Create Pagefind media index");
  const { index } = created;

  for (const record of records) {
    const added = await index.addCustomRecord(record);
    checkErrors(added, `Index ${record.url}`);
  }

  const written = await index.writeFiles({ outputPath });
  checkErrors(written, `Write Pagefind media index to ${outputPath}`);
} finally {
  await close();
}
