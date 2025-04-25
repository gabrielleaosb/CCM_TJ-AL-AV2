document.addEventListener("DOMContentLoaded", function () {
    const slider = document.getElementById('videoContainer');
    const next = document.getElementById('nextVideoButton');
    const prev = document.getElementById('prevVideoButton');
  
    if (slider && next && prev) {
      next.addEventListener('click', () => {
        slider.scrollBy({ left: slider.clientWidth, behavior: 'smooth' });
      });
  
      prev.addEventListener('click', () => {
        slider.scrollBy({ left: -slider.clientWidth, behavior: 'smooth' });
      });
    }
  });
  