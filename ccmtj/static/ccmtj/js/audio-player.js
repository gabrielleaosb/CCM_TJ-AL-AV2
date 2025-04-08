document.addEventListener('DOMContentLoaded', function () {
    const players = document.querySelectorAll('.audio-player');

    let currentAudio = null;
    let currentIcon = null;

    players.forEach(player => {
        const audio = player.querySelector('.customAudio');
        const playBtn = player.querySelector('.playPauseBtn');
        const icon = player.querySelector('.playPauseIcon');
        const progress = player.querySelector('.progress');

        const playIcon = "/static/ccmtj/icons/play-button.svg";
        const pauseIcon = "/static/ccmtj/icons/pause-button.svg";

        let isSeeking = false;

        audio.addEventListener('timeupdate', () => {
            if (!isSeeking && audio.duration) {
                const percent = (audio.currentTime / audio.duration) * 100;
                progress.value = percent;
            }
        });
        progress.addEventListener('input', () => {
            isSeeking = true;
        });
        progress.addEventListener('change', () => {
            if (audio.duration) {
                const newTime = (progress.value / 100) * audio.duration;
                audio.currentTime = newTime;
            }
            isSeeking = false;
        });
        playBtn.addEventListener('click', () => {
            if (currentAudio && currentAudio !== audio) {
                currentAudio.pause();
                if (currentIcon) {
                    currentIcon.src = playIcon;
                }
            }
            if (audio.paused) {
                audio.play();
                icon.src = pauseIcon;
                currentAudio = audio;
                currentIcon = icon;
            } else {
                audio.pause();
                icon.src = playIcon;
                currentAudio = null;
                currentIcon = null;
            }
        });
        audio.addEventListener('ended', () => {
            icon.src = playIcon;
            if (currentAudio === audio) {
                currentAudio = null;
                currentIcon = null;
            }
        });
    });
});
