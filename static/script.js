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

    // Create a new audio element and play the audio
    var audio = new Audio(url);
    audio.play();

    // Update the currently playing audio
    currentlyPlayingAudio = audio;
}