document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('loading-spinner').style.display = 'block';


    window.addEventListener('load', function () {
        document.getElementById('loading-spinner').style.display = 'none';
    });

    setTimeout(function () {

        document.getElementById('loading-spinner').style.display = 'none';
    }, 30000);
    
});document.addEventListener('DOMContentLoaded', function () {
    // Show loading spinner
    document.getElementById('loading-spinner').style.display = 'block';

    // Hide loading spinner when the page is fully loaded
    window.addEventListener('load', function () {
        document.getElementById('loading-spinner').style.display = 'none';
    });

    // Hide loading spinner before unloading (when navigating to a new page)
    window.addEventListener('beforeunload', function () {
        // Introduce a slight delay to ensure the spinner is shown briefly before unloading
        setTimeout(function () {
            document.getElementById('loading-spinner').style.display = 'block';
        }, 50); // Adjust the delay as needed
    });
});




var currentlyPlayingAudio = null;

function playAudio(url) {
    // Stop the currently playing audio, if any
    if (currentlyPlayingAudio !== null) {
        currentlyPlayingAudio.pause();
    }

    // Create or use the existing audio element
    var audio = document.getElementById('audioPlayer');
    if (!audio) {
        audio = document.createElement('audio');
        audio.id = 'audioPlayer';
        document.body.appendChild(audio);
    }

    // Set the audio source and play
    audio.src = url;
    audio.play();

    // Update the currently playing audio
    currentlyPlayingAudio = audio;

    // Change the play icon to pause when audio starts playing
    var icon = document.getElementById('playPauseIcon');
    if (icon) {
        icon.classList.remove('fa-play');
        icon.classList.add('fa-pause');
    }
}

function togglePlayPauseIcon(icon) {
    icon.classList.toggle('fa-play');
    icon.classList.toggle('fa-pause');
}

function togglePlayPause(button, url) {
    var icon = button.querySelector('.play-pause-icon');

    if (currentlyPlayingAudio && !currentlyPlayingAudio.paused) {
        currentlyPlayingAudio.pause();
        togglePlayPauseIcon(icon);
    } else {
        playAudio(url);
        togglePlayPauseIcon(icon);
    }
}