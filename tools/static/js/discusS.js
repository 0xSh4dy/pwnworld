const roomName = "discussions";
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);
let timerStart = 10;

const chatLog = document.getElementById("chat-log");
let sentMessages = 0;
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
document.querySelector('#chat-log').innerHTML += (`<div><span class="username">${data.user}:<span> <span class="message">${data.message}</span></div>`);
chatLog.scrollTop = chatLog.scrollHeight;
if(sentMessages===5){
    timerStart=10;
    setInterval(()=>{
        timerStart--;
    },1000);
    setTimeout(()=>{
        sentMessages=0;
    },10000);
}
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = String(messageInputDom.value);
    if(sentMessages==5){
        alert(`Please wait for ${timerStart} seconds to send a new message`);
        
    }
    else{
    if(message.length > 150){
        alert("The message length is limited to 150 characters");
    }
    else{
    chatSocket.send(JSON.stringify({
        'message': message,
        'user':user
    }));
    messageInputDom.value = '';
    sentMessages++;
    
}
    }
};
