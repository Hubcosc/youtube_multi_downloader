// script.js
document.getElementById('downloadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const videoUrl = document.getElementById('videoUrl').value;
    const statusDiv = document.getElementById('status');

    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: videoUrl }),
    })
    .then(response => response.json())
    .then(data => {
        statusDiv.textContent = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
        statusDiv.textContent = 'An error occurred. Please try again.';
    });
});