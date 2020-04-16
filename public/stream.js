var stream = new WebSocket("ws://localhost:8081");

const video = document.querySelector('#video');

// request access to webcam
navigator.mediaDevices.getUserMedia({video: {width: 360, height: 360}}).then((stream) => video.srcObject = stream);

const getFrame = () => {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    const data = canvas.toDataURL('image/jpeg');

    return data;
}

// send data
stream.onopen = () => {
    setInterval(() => {
        stream.send(getFrame());
        
    }, 100) // 15 fps
}