const likeBtn = document.querySelectorAll(".likeBtn");
const dislikeBtn = document.querySelectorAll(".dislikeBtn");
const submitFlag = document.querySelectorAll(".submitFlag");
const messageContainer = document.getElementById("messageContainer");
const likeCounter = document.getElementById("likeCounter");
const dislikeCounter = document.getElementById("dislikeCounter");
const checkBox = document.querySelectorAll(".check");
var challengeContainer = document.querySelectorAll(".challenge");
let roomName = readCookie("r1");
// roomName= "abcd";
const dataSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/pwn/'
    + roomName
    + '/'
);
const scoreSocket = new WebSocket(
    `ws://${window.location.host}/ws/pwn/leaderboard`
)
scoreSocket.onopen=function(e1){
    scoreSocket.send(JSON.stringify({
        "message":"Correct Flag"
    }))
}
scoreSocket.onclose = function(err){
    console.error("Score socket closed unexpectedly");
}
// const commonSocket = new WebSocket(
//     'ws://'
//     + window.location.host
//     + '/ws/pwn/'
//     + 'dashboard'
//     + '/'
// );
function setMessage(msg,funcn,eve){
    
    messageContainer.style.color = "white";
    if(msg==="Already liked"){
        messageContainer.style.display="block";
        messageContainer.innerHTML= "You have already liked the challenge";
        messageContainer.style.backgroundColor = "yellow";
        messageContainer.style.color = "purple";
        
        // // commonSocket.onopen = function(){
        //     // console.log("Socket opened") 
        //     commonSocket.send(JSON.stringify({
        //         user:readCookie("auth"),
        //         data:"Liked a challenge" 
        //     }))
        // // }
        
        
        
        // commonSocket.onclose = function(er){
        //     console.error('Chat socket closed unexpectedly');
        // }
    }
    else if(msg==='Already disliked'){
        messageContainer.style.display="block";
        messageContainer.innerHTML= "You have already disliked the challenge";
        messageContainer.style.backgroundColor = "yellow";
        messageContainer.style.color = "purple";
        
    }
    else if(msg.like==="Liked a challenge"){
        eve.path[1].childNodes[1].innerText = parseInt(eve.path[1].childNodes[1].innerText)+1;
        // commonSocket.send(JSON.stringify({
        //     user:readCookie("auth"),
        //     data:`${msg.username} liked the challenge ${msg.chal_name}`
        // }))
    }
    else if(msg.dislike==='Disliked a challenge'){
        eve.path[1].childNodes[1].innerText = parseInt(eve.path[1].childNodes[1].innerText)+1;
        // commonSocket.send(JSON.stringify({
        //     user:readCookie("auth"),
        //     data:`${msg.username} disliked the challenge ${msg.chal_name}`
        // }))
    }
    else if(msg.flag==="Correct flag"){
        messageContainer.style.display="block";
        messageContainer.style.backgroundColor = "greenyellow";
        messageContainer.style.color="blue";
        messageContainer.innerHTML = "Cheers! You have solved this challenge";
        const scoreSocket = new WebSocket(
            `ws://${window.location.host}/ws/pwn/leaderboard`
        )
        scoreSocket.onopen=function(e1){
            scoreSocket.send(JSON.stringify({
                "message":"Correct Flag"
            }))
        }
        // commonSocket.send(JSON.stringify({
        //     user:readCookie("auth"),
        //     data:`${msg.username} solved the challenge ${msg.chal_name}`
        // }))
    }
    else if(msg=="Incorrect flag"){
        messageContainer.style.display="block";
        messageContainer.style.backgroundColor = "red";
        messageContainer.innerHTML = "Oops, the flag you provided was incorrect.";
    }
    else{
        messageContainer.style.display = "block";
        messageContainer.style.backgroundColor = "red";
        messageContainer.style.color = "white";
        messageContainer.innerHTML = msg;
    }
    setTimeout(()=>{
        messageContainer.style.display = "none";
    },5000)
}
// Function to read the cookies
function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}



dataSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};


// setTimeout(()=>{
//     dataSocket.send(JSON.stringify({
//         'message': "trasj data",
//         'user':"mmmuser",
//         'data':'useless data'
//     }));
// },5000)

likeBtn.forEach((btn)=>{
    let user = readCookie("auth");
    btn.addEventListener("click",(e)=>{
        challenge_name = e.path[3].childNodes[1].innerHTML;
        dataSocket.send(JSON.stringify({
            challenge_name:challenge_name,
            message:'like',
            user:readCookie("auth")
        }))        
        dataSocket.onmessage = function (event1) {
            const data = JSON.parse(event1.data);
       
            let funcn = data.function;
            let message = data.message;
            setMessage(message,funcn,e);
        };
    })
})
dislikeBtn.forEach((btn)=>{
    btn.addEventListener("click",(e)=>{
        challenge_name = e.path[3].childNodes[1].innerHTML;
        dataSocket.send(JSON.stringify({
            challenge_name:challenge_name,
            message:'dislike',
            user:readCookie("auth")
        }));
        dataSocket.onmessage = function (event1) {
            const data = JSON.parse(event1.data);
            let message = data.message;
            let funcn = data.function;
           
            setMessage(message,funcn,e);
        };
    })
})
submitFlag.forEach((btn)=>{
    btn.addEventListener("click",(e)=>{
        userFlag = e.path[1].childNodes[9].value
        challenge_name = e.path[1].childNodes[1].innerHTML
        dataSocket.send(JSON.stringify({
           challenge_name:challenge_name,
           flag:userFlag,
           message:"submit_flag",
           user:readCookie("auth"),
        }))
        dataSocket.onmessage = function (event1) {
            const data = JSON.parse(event1.data);
            console.log(data)
            let message = data.message;
            let funcn = data.function;
            setMessage(message,funcn,e);
        };
    })
})

checkBox.forEach((box)=>{
    box.addEventListener("change",(e)=>{
        let filter = e.target.id;
        if(filter==='solves'){
            document.getElementById("points").checked = false
            document.getElementById("likes").checked = false
        }
        else if(filter==='points'){
            document.getElementById("likes").checked = false
            document.getElementById("solves").checked = false

        }
        else if(filter==='likes'){
            document.getElementById("points").checked = false
            document.getElementById("solves").checked = false

        }
        dataSocket.send(JSON.stringify({
            filter:filter,
            user:readCookie("auth"),
            message:'filter'
        }))
        dataSocket.onmessage = function(event1){
            const data = JSON.parse(event1.data);
            let message = data.message;
            console.log(message);
            challengeContainer.forEach((cont)=>{
                document.querySelector(".challenges").removeChild(document.querySelector(".challenge"))
            })
            // challengeContainer.forEach((cont)=>{
                
            // })
            for(let m of message){
                challenge_name = m[1];
                challenge_difficulty = m[7];
                challenge_description = m[8];
                challenge_link = m[9];
                challenge_points = m[10];
                challenge_solves = m[3];
                challenge_likes = m[4];
                challenge_dislikes = m[5];
                const div = document.createElement('div');
                div.className="challenge"
                div.innerHTML = `<p class="name">${challenge_name}</p><p class="description">${challenge_description}</p><p class="location"><a href="${challenge_link}">${challenge_link}</a> </p><div class="filterInfo"><p class="difficulty">${challenge_difficulty}</p><p class="likes"><i style="color: white;font-size:25px" class="fa fa-thumbs-up likeBtn"></i><span class="likeCounter">${challenge_likes}</span> </p><p class="dislikes"><i style="color: white;font-size:25px" class="fa fa-thumbs-down dislikeBtn"></i><span class="dislikeCounter">${challenge_dislikes}</span></p><p class="points">Points: ${challenge_points}</p><p class="solves">Solves: ${challenge_solves}</p></div><input type="text" class="flagSubmit" placeholder="flag{the_flag_you_get}"><button type="submit" class="submitFlag">Submit</button><p class="comments"><span>Comments</span><i id="commentsScroll" style="color:white; font-size:30px;position:relative;top:5px;" class="fa fa-angle-double-down"></i></p>`;
                document.querySelector(".challenges").appendChild(div);
            }
        }
    })
})