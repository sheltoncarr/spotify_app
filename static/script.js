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
var currentlyPlayingButton = null;

function playAudio(url) {
    
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

    // Update the currently playing audio and its associated button
    currentlyPlayingAudio = audio;
    currentlyPlayingButton = document.querySelector('.play-button[onclick*="' + url + '"]');
    togglePlayPauseIcon(currentlyPlayingButton.querySelector('.play-pause-icon'));
}

function togglePlayPauseIcon(icon) {
    icon.classList.toggle('fa-play');
    icon.classList.toggle('fa-pause');
}

function togglePlayPause(button, url) {
    var icon = button.querySelector('.play-pause-icon');

    // Clicked on the same button
    if (currentlyPlayingButton && currentlyPlayingButton === button) {
        if (currentlyPlayingAudio && !currentlyPlayingAudio.paused) {
            currentlyPlayingAudio.pause();
            togglePlayPauseIcon(icon);
        } else {
            currentlyPlayingAudio.play();
            togglePlayPauseIcon(icon);
        }
    } 

    // Clicked on a new button
    else {
        if (currentlyPlayingAudio && !currentlyPlayingAudio.paused){
            currentlyPlayingAudio.pause();
            togglePlayPauseIcon(currentlyPlayingButton.querySelector('.play-pause-icon'));
            playAudio(url)
        }
        else{
            playAudio(url);
        }

    }
}

document.addEventListener('DOMContentLoaded', function () {
    // Initial table load with default number of rows for each table
    var dropdowns = document.querySelectorAll('.row-dropdown');
    dropdowns.forEach(function (dropdown) {
        updateTable(dropdown);
        dropdown.addEventListener('change', function () {
            // Update the corresponding table with the selected number of rows
            updateTable(dropdown);
        });
    });
});

function updateTable(dropdown) {
    // Get the selected number of rows
    var selectedRows = parseInt(dropdown.value);

    // Update the corresponding table with the selected number of rows
    var table = dropdown.closest('.table-container').querySelector('.table');
    updateRows(selectedRows, table);
}

function updateRows(rows, table) {
    // Get all rows in the specified table
    var rowsToToggle = table.querySelectorAll('tbody tr');

    // Show the first 'rows' number of rows and hide the rest
    for (var i = 0; i < rowsToToggle.length; i++) {
        if (i < rows) {
            rowsToToggle[i].style.display = 'table-row';
        } else {
            if (rowsToToggle[i]) {
                rowsToToggle[i].style.display = 'none';
            }
        }
    }
}