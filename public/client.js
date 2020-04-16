var server = new WebSocket("ws://localhost:8080");

const display = document.querySelector('#serverdata');


// send data
server.onopen = () => {
    console.log("connected to call.");
}
server.onmessage = message => {
    display.src = message.data;
}
