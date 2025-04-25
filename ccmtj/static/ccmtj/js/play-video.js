function playVideo(element) {
    const videoId = element.getAttribute('data-video-id');
    const videoContainer = element.querySelector('.video-player-container');
    const thumbnail = element.querySelector('img');
    const playIcon = element.querySelector('.play-icon');

    // Mostrar o player e esconder a miniatura e o ícone de play
    videoContainer.classList.remove('hidden');
    thumbnail.classList.add('hidden');
    playIcon.classList.add('hidden');

    // Inserir o iframe com autoplay
    const iframe = videoContainer.querySelector('iframe');
    iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
  }