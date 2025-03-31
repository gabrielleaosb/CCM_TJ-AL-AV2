document.addEventListener("DOMContentLoaded", function () {
    const scanBtn = document.getElementById("scan-btn");

    function startScanner() {
        const scanner = new Html5Qrcode("reader");

        document.getElementById("reader").classList.remove("hidden");

        scanner.start(
            { facingMode: "environment" }, 
            {
                fps: 10, 
                qrbox: { width: 250, height: 250 }, 
            },
            (decodedText) => {
                alert("QR Code detectado: " + decodedText);

                scanner.stop();
                document.getElementById("reader").classList.add("hidden");
            },
            (errorMessage) => {
                console.log("Erro: " + errorMessage);
            }
        ).catch(err => {
            console.log("Erro ao iniciar o scanner: ", err);
        });
    }
    scanBtn.addEventListener("click", function () {
        startScanner();
    });
});
