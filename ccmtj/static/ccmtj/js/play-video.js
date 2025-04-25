function playVideo(element) {
    const videoId = element.getAttribute('data-video-id');
    const videoContainer = element.querySelector('.video-player-container');
    const thumbnail = element.querySelector('img');
    const playIcon = element.querySelector('.play-icon');

    videoContainer.classList.remove('hidden');
    thumbnail.classList.add('hidden');
    playIcon.classList.add('hidden');

    const iframe = videoContainer.querySelector('iframe');
    iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1`;
  }