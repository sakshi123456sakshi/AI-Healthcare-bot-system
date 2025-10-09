function startListening() {
    let recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";

    recognition.onresult = function(event) {
        let userInput = event.results[0][0].transcript;
        document.getElementById("user-input").value = userInput;
        sendMessage();
    };

    recognition.start();
}