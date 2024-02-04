document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('loading-spinner').style.display = 'block';

    window.addEventListener('load', function () {
        document.getElementById('loading-spinner').style.display = 'none';
    });

    setTimeout(function () {

        document.getElementById('loading-spinner').style.display = 'none';
    }, 30000);
    
});document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('loading-spinner').style.display = 'block';

    window.addEventListener('load', function () {
        document.getElementById('loading-spinner').style.display = 'none';
    });

    window.addEventListener('beforeunload', function () {
        setTimeout(function () {
            document.getElementById('loading-spinner').style.display = 'block';
        }, 50);
    });
});



var currentlyPlayingAudio = null;
var currentlyPlayingButton = null;

function playAudio(url) {
    
    var audio = document.getElementById('audioPlayer');
    if (!audio) {
        audio = document.createElement('audio');
        audio.id = 'audioPlayer';
        document.body.appendChild(audio);
    }

    audio.src = url;
    audio.play();

    currentlyPlayingAudio = audio;

    audio.addEventListener('ended', function () {
        togglePlayPauseIcon(currentlyPlayingButton.querySelector('.play-pause-icon'));

        currentlyPlayingAudio = null;
        currentlyPlayingButton = null;
    });
        
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
        currentlyPlayingButton = button;
        togglePlayPauseIcon(currentlyPlayingButton.querySelector('.play-pause-icon'));
    }
}




document.addEventListener('DOMContentLoaded', function () {
    var dropdowns = document.querySelectorAll('.row-dropdown');
    dropdowns.forEach(function (dropdown) {
        updateTable(dropdown);
        dropdown.addEventListener('change', function () {
            updateTable(dropdown);
        });
    });
});

function updateTable(dropdown) {
    var selectedRows = parseInt(dropdown.value);

    var table = dropdown.closest('.table-container').querySelector('.table');
    updateRows(selectedRows, table);
}

function updateRows(rows, table) {
    var rowsToToggle = table.querySelectorAll('tbody tr');

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