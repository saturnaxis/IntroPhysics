function getMainText() {
  const main =
    document.querySelector("main") ||
    document.querySelector(".bd-main") ||
    document.querySelector("article");

  if (!main) return "";

  // Clone so we can remove junk before reading
  const clone = main.cloneNode(true);

  // Remove navigation/UI/code prompts you probably don't want spoken
  clone.querySelectorAll("script, style, nav, .sidebar, .toc, .headerlink").forEach(el => el.remove());

  return clone.innerText.replace(/\s+/g, " ").trim();
}

function stopSpeech() {
  if ("speechSynthesis" in window) {
    window.speechSynthesis.cancel();
  }
}

function readPage() {
  if (!("speechSynthesis" in window)) {
    alert("Text-to-speech is not supported in this browser.");
    return;
  }

  stopSpeech();

  const text = getMainText();
  if (!text) return;

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = document.documentElement.lang || "en";

  // Optional tuning
  utterance.rate = 1.0;
  utterance.pitch = 1.0;
  utterance.volume = 1.0;

  // Try to pick a matching voice if available
  const voices = window.speechSynthesis.getVoices();
  const match = voices.find(v => v.lang && utterance.lang && v.lang.startsWith(utterance.lang));
  if (match) utterance.voice = match;

  window.speechSynthesis.speak(utterance);
}

function addTTSButtons() {
  if (document.getElementById("tts-controls")) return;

  const container = document.createElement("div");
  container.id = "tts-controls";
  container.style.margin = "1rem 0";

  const readBtn = document.createElement("button");
  readBtn.textContent = "🔊 Read page aloud";
  readBtn.type = "button";
  readBtn.onclick = readPage;

  const stopBtn = document.createElement("button");
  stopBtn.textContent = "⏹ Stop";
  stopBtn.type = "button";
  stopBtn.style.marginLeft = "0.5rem";
  stopBtn.onclick = stopSpeech;

  container.appendChild(readBtn);
  container.appendChild(stopBtn);

  const target =
    document.querySelector("main") ||
    document.querySelector(".bd-main") ||
    document.body;

  target.prepend(container);
}

document.addEventListener("DOMContentLoaded", () => {
  addTTSButtons();

  // Some browsers populate voices asynchronously
  if ("speechSynthesis" in window) {
    window.speechSynthesis.onvoiceschanged = () => {};
  }
});