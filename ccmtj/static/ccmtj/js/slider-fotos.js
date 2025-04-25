document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("contentContainer");
    const button = document.getElementById("toggleButton");
    const photoSlider = document.getElementById('photoContainer');
    const nextPhoto = document.getElementById('nextPhotoButton');
    const prevPhoto = document.getElementById('prevPhotoButton');
  
    let isExpanded = false;
  
    if (container && button) {
      function checkContentHeight() {
        const contentHeight = container.scrollHeight;
        const containerHeight = container.clientHeight;
  
        button.style.display = (contentHeight <= containerHeight + 1) ? 'none' : 'flex';
      }
  
      checkContentHeight();
      window.addEventListener('resize', checkContentHeight);
  
      button.addEventListener("click", function (e) {
        e.preventDefault();
        const fullHeight = container.scrollHeight;
  
        container.style.maxHeight = isExpanded ? '377px' : fullHeight + 'px';
        button.innerText = isExpanded ? "LER MAIS" : "LER MENOS";
        isExpanded = !isExpanded;
      });
    }
  
    // Slider Fotos
    if (photoSlider && nextPhoto && prevPhoto) {
      nextPhoto.addEventListener('click', () => {
        photoSlider.scrollBy({ left: photoSlider.clientWidth, behavior: 'smooth' });
      });
  
      prevPhoto.addEventListener('click', () => {
        photoSlider.scrollBy({ left: -photoSlider.clientWidth, behavior: 'smooth' });
      });
    }
  });
  