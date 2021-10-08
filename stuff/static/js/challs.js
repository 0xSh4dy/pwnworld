const roomName = "chal_mod";
const dataSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/pwn/'
    + roomName
    + '/'
);

dataSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log(data);
};

dataSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};


setTimeout(()=>{
    dataSocket.send(JSON.stringify({
        'message': "trasj data",
        'user':"mmmuser",
        'data':'useless data'
    }));
},5000)