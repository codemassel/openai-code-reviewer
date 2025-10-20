const reviewBtn = document.getElementById('reviewBtn');
const codeInput = document.getElementById('codeInput');
const output = document.getElementById('output');

reviewBtn.addEventListener('click', async () => {
  const code = codeInput.value;
  output.textContent = "Loading...";

  try {
    const res = await fetch('http://localhost:8000/api/summarize/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: code })
    });

    const data = await res.json();
    output.textContent = data.review || "Keine Antwort vom Backend.";
  } catch (err) {
    output.textContent = "Fehler: " + err;
  }
});
