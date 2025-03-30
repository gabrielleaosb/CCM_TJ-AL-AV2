document.addEventListener("DOMContentLoaded", function () {
    const thumbs = JSON.parse(document.getElementById('thumbs-data').textContent);
    let currentIndex = 0;

    function updateImage() {
        const imageElement = document.getElementById('displayed-image');
        const nameElement = document.getElementById('image-name');
        if (thumbs.length > 0) {
            imageElement.src = thumbs[currentIndex].imagem;
            nameElement.innerText = thumbs[currentIndex].nome;
        }
    }

    document.getElementById('prev').addEventListener('click', function () {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : thumbs.length - 1;
        updateImage();
    });

    document.getElementById('next').addEventListener('click', function () {
        currentIndex = (currentIndex < thumbs.length - 1) ? currentIndex + 1 : 0;
        updateImage();
    });

    document.getElementById('displayed-image').addEventListener('click', function () {
        this.style.display = "none";
        document.getElementById('image-name').style.display = "none";
        document.getElementById('image-navbar').style.display = "none";
    });

    updateImage();
});
