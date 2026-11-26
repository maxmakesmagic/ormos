async function loadFlash(viewer) {
  const stage = viewer.querySelector("[data-flash-stage]");
  const status = viewer.querySelector("[data-flash-status]");
  const embedded = viewer.hasAttribute("data-flash-embedded");
  status.textContent = "Loading Flash…";

  try {
    const player = window.RufflePlayer.newest().createPlayer();
    const playback = player.ruffle();
    const base = viewer.dataset.flashBase
      ? new URL(viewer.dataset.flashBase, window.location.href).href : null;
    const parameters = JSON.parse(viewer.dataset.flashParameters);
    const puzzleImage = viewer.dataset.flashImage;
    const urlRewriteRules = puzzleImage
      ? [[new URL(parameters.stgImage, base).href, puzzleImage]] : [];
    player.tabIndex = 0;
    player.setAttribute("aria-label", viewer.getAttribute("aria-label") ?? "Flash player");
    player.addEventListener("loadedmetadata", () => {
      const { width, height } = playback.metadata ?? {};
      if (Number.isFinite(width) && Number.isFinite(height) && width > 0 && height > 0) {
        player.style.setProperty("--flash-player-ratio", `${width} / ${height}`);
        if (embedded) player.style.setProperty("--flash-player-width", `${width}px`);
      }
    }, { once: true });

    stage.replaceChildren(player);
    await playback.load({
      url: viewer.dataset.flashPlayer,
      base,
      parameters,
      urlRewriteRules,
      autoplay: "on",
      unmuteOverlay: "visible",
      allowScriptAccess: false,
      allowNetworking: "internal",
      openUrlMode: "deny",
    });
    status.textContent = "";
  } catch {
    stage.replaceChildren();
    status.textContent = embedded
      ? "The Flash player could not load here. Try opening it on its own page."
      : "The Flash player could not load. You can open the archived SWF below.";
  }
}

for (const viewer of document.querySelectorAll("[data-flash-player]")) {
  const preview = viewer.closest("[data-flash-preview]");
  if (preview && !preview.open) {
    const startOnOpen = () => {
      if (!preview.open) return;
      preview.removeEventListener("toggle", startOnOpen);
      loadFlash(viewer);
    };
    preview.addEventListener("toggle", startOnOpen);
  } else {
    loadFlash(viewer);
  }
}
