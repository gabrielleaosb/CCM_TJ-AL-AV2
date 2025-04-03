document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const scanBtn = document.getElementById("scan-btn");
    const ctx = canvas.getContext("2d");

    let scanning = false;

    scanBtn.addEventListener("click", () => {
        navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
            .then(stream => {
                video.srcObject = stream;
                video.setAttribute("playsinline", true);
                video.play();
                scanning = true;
                scanQRCode();
            })
            .catch(err => {
                console.error("Erro ao acessar a câmera:", err);
                alert("Erro ao acessar a câmera. Verifique as permissões.");
            });
    });

    function scanQRCode() {
        if (!scanning) return;

        if (video.readyState === video.HAVE_ENOUGH_DATA) {
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const code = jsQR(imageData.data, canvas.width, canvas.height);

            if (code) {
                showConfirmationPopup(code.data);
                scanning = false;
                video.srcObject.getTracks().forEach(track => track.stop());
            } else {
                requestAnimationFrame(scanQRCode);
            }
        } else {
            requestAnimationFrame(scanQRCode);
        }
    }

    function showConfirmationPopup(qrData) {
        const modalBg = document.createElement("div");
        modalBg.className = "fixed inset-0 flex items-center justify-center z-50";
    
        const modal = document.createElement("div");
        modal.className = "bg-white p-6 rounded-lg shadow-lg text-center max-w-xs";
    
        const message = document.createElement("p");
        message.className = "mb-4 text-lg";
        message.textContent = "Abrir este link?";
        
        const link = document.createElement("a");
        link.className = "text-blue-500 break-all";
        link.href = qrData;
        link.textContent = qrData;
        link.target = "_blank";
    
        const buttonContainer = document.createElement("div");
        buttonContainer.className = "flex justify-center space-x-4 mt-4"; 
    
        const acceptBtn = document.createElement("button");
        acceptBtn.className = "bg-green-500 text-white px-4 py-2 rounded";
        acceptBtn.textContent = "Sim";
        acceptBtn.onclick = () => {
            window.location.href = qrData;
            document.body.removeChild(modalBg);
        };
    
        const declineBtn = document.createElement("button");
        declineBtn.className = "bg-red-500 text-white px-4 py-2 rounded";
        declineBtn.textContent = "Não";
        declineBtn.onclick = () => {
            document.body.removeChild(modalBg);
        };
    
        buttonContainer.appendChild(acceptBtn);
        buttonContainer.appendChild(declineBtn);

        modal.appendChild(message);
        modal.appendChild(link);
        modal.appendChild(buttonContainer);
        modalBg.appendChild(modal);
        document.body.appendChild(modalBg);
    }
    
});
