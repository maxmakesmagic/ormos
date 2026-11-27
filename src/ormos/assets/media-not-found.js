const address = new URLSearchParams(location.search).get("url");
if (address) {
  try {
    const source = address.replace(
      /^https?:\/\/web\.archive\.org\/web\/[0-9]{1,14}(?:[a-z]{1,8}_)?\/(?=https?:\/\/)/i,
      "",
    );
    const url = new URL(source);
    if (
      ["http:", "https:"].includes(url.protocol)
      && (url.hostname === "wizards.com" || url.hostname.endsWith(".wizards.com"))
      && !url.username
      && !url.password
    ) {
      const original = document.querySelector(".missing-media-source");
      original.querySelector("code").textContent = address;
      original.hidden = false;
    }
  } catch {
    // Keep the generic message for malformed URLs.
  }
}
