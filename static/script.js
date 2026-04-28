function sendGuess() {
    let guess = document.getElementById("guessInput").value;

    fetch("/guess", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ guess: guess })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
        document.getElementById("attempts").innerText = "Attempts: " + data.attempts;
        document.getElementById("guessInput").value = "";
    });
}