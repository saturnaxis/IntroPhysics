function readPage() {
    const text = document.body.innerText;
    const speech = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(speech);
}
// Add button to page
document.addEventListener("DOMContentLoaded", function() {
    const btn = document.createElement("button");
    btn.innerHTML = "🔊 Read Article";
    btn.style.position = "fixed";
    btn.style.top = "10px";
    btn.style.right = "10px";
    btn.onclick = readPage;
    document.body.appendChild(btn);
});
