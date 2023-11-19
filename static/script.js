document.addEventListener('DOMContentLoaded', function () {

    document.getElementById('loading-spinner').style.display = 'block';


    window.addEventListener('load', function () {
        document.getElementById('loading-spinner').style.display = 'none';
    });

    setTimeout(function () {

        document.getElementById('loading-spinner').style.display = 'none';
    }, 8000);
    
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
