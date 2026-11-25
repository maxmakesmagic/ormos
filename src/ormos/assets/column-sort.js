for (const section of document.querySelectorAll("[data-column-table]")) {
  const table = section.querySelector("table");
  const body = table.tBodies[0];
  const buttons = [...table.querySelectorAll("[data-sort-key]")];
  const originalRows = [...body.rows];
  const status = section.querySelector("[data-sort-status]");
  const scope = section.querySelector("[data-sort-scope]");
  const collator = new Intl.Collator(document.documentElement.lang || undefined, {
    numeric: true,
    sensitivity: "base",
  });

  if (scope) scope.hidden = false;
  buttons.forEach((button, column) => {
    const header = button.closest("th");
    header.querySelector("[data-sort-label]").hidden = true;
    button.hidden = false;
    button.addEventListener("click", () => {
      const ascending = header.getAttribute("aria-sort") !== "ascending";
      const values = originalRows.map((row, index) => ({
        row,
        index,
        value: row.cells[column].dataset.sortValue ?? row.cells[column].textContent.trim(),
      }));

      values.sort((first, second) => {
        const missing = Number(!first.value) - Number(!second.value);
        if (missing) return missing;
        const comparison = collator.compare(first.value, second.value);
        return (ascending ? comparison : -comparison) || first.index - second.index;
      });

      for (const control of buttons) control.closest("th").removeAttribute("aria-sort");
      header.setAttribute("aria-sort", ascending ? "ascending" : "descending");
      body.append(...values.map(({ row }) => row));
      status.textContent = button.dataset.sortKey === "date"
        ? `Sorted by publication date, ${ascending ? "earliest" : "latest"} first.`
        : `Sorted by ${button.textContent.trim().toLowerCase()}, ${ascending ? "ascending" : "descending"}.`;
    });
  });
}
