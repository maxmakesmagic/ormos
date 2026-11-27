function filterVideos(filter) {
  const count = document.querySelector("[data-video-count]");
  const normalize = (value) => value.normalize("NFKD").replace(/\p{Mark}/gu, "").toLowerCase();
  const entries = [...document.querySelectorAll("[data-video-entry]")].map((row) => {
    const title = row.querySelector("[data-video-page]");
    const text = normalize([title.textContent, row.dataset.videoSearch].join(" "));
    return { row, text };
  });

  filter.closest(".video-filter").hidden = false;
  filter.addEventListener("input", () => {
    const terms = normalize(filter.value).trim().split(/\s+/);
    let visible = 0;
    for (const { row, text } of entries) {
      row.hidden = !terms.every((term) => text.includes(term));
      if (!row.hidden) visible += 1;
    }
    const noun = visible === 1 ? "video" : "videos";
    count.textContent = visible ? `${visible.toLocaleString()} ${noun}` : "No videos match.";
  });
}

function seekFromTranscript(player, transcript) {
  const seek = () => {
    const offset = /^#t=(\d+(?:\.\d{1,3})?)$/.exec(location.hash);
    const seconds = Number(offset?.[1]);
    if (player.readyState >= 1 && Number.isFinite(seconds) && seconds <= player.duration) {
      player.currentTime = seconds;
    }
  };

  transcript.addEventListener("click", (event) => {
    const cue = event.target.closest("[data-video-seek], [data-podcast-seek]");
    if (!cue || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    history.replaceState(null, "", cue.hash);
    seek();
  });
  player.addEventListener("loadedmetadata", seek);
  window.addEventListener("hashchange", seek);
  seek();
}

const filter = document.querySelector("[data-video-filter]");
if (filter) filterVideos(filter);

const player = document.querySelector(".video-player, .podcast-player");
const transcript = document.querySelector("[data-video-transcript], [data-podcast-transcript]");
if (player && transcript) seekFromTranscript(player, transcript);
