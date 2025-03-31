document.addEventListener("DOMContentLoaded", function () {
    const scanBtn = document.getElementById("scan-btn");
    const reader = document.getElementById("reader");

    scanBtn.addEventListener("click", () => {
        reader.classList.remove("hidden"); 

        const html5QrCode = new Html5Qrcode("reader");

        html5QrCode.start(
            { facingMode: "environment" }, 
            {
                fps: 10, // Frames por segundo
                qrbox: { width: 250, height: 250 }, 
            },
            (decodedText, decodedResult) => {
                alert("QR Code detectado: " + decodedText);
                html5QrCode.stop(); 
                reader.classList.add("hidden"); 
            },
            (errorMessage) => {
                console.log("Erro ao escanear: ", errorMessage);
            }
        ).catch(err => console.log("Erro ao iniciar câmera:", err));
    });
});
