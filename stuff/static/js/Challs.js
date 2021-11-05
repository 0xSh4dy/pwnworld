const likeBtn = document.querySelectorAll(".likeBtn");
const dislikeBtn = document.querySelectorAll(".dislikeBtn");
const submitFlag = document.querySelectorAll(".submitFlag");
const messageContainer = document.getElementById("messageContainer");
const likeCounter = document.getElementById("likeCounter");
const dislikeCounter = document.getElementById("dislikeCounter");
const checkBox = document.querySelectorAll(".check");
var challengeContainer = document.querySelectorAll(".challenge");
let roomName = readCookie("r1");
function evLisLike(){
    document.querySelectorAll(".likeBtn").forEach((btn)=>{
        btn.addEventListener("click",(e)=>{
            challenge_name = e.path[3].children[0].innerHTML;
            dataSocket.send(JSON.stringify({
                challenge_name:challenge_name,
                message:'like',
                user:readCookie("auth"),
                fi_id:readCookie("fi_id")
            }))        
            dataSocket.onmessage = function (event1) {
                const data = JSON.parse(event1.data);
                let funcn = data.function;
                let message = data.message;
                setMessage(message,funcn,e);
            };
        })
    })
}
function evLDislike(){
    document.querySelectorAll(".dislikeBtn").forEach((btn)=>{
        btn.addEventListener("click",(e)=>{
    
            challenge_name = e.path[3].children[0].innerHTML;
            dataSocket.send(JSON.stringify({
                challenge_name:challenge_name,
                message:'dislike',
                user:readCookie("auth"),
                fi_id:readCookie("fi_id")
            }));
            dataSocket.onmessage = function (event1) {
                const data = JSON.parse(event1.data);
                let message = data.message;
                let funcn = data.function;
               
                setMessage(message,funcn,e);
            };
        })
    })
}
function evLDissubmit(){
    document.querySelectorAll(".submitFlag").forEach((btn)=>{
        btn.addEventListener("click",(e)=>{
            challenge_name = e.path[1].children[0].innerHTML;
            userFlag = e.path[1].children[4].value;
            dataSocket.send(JSON.stringify({
               challenge_name:challenge_name,
               flag:userFlag,
               message:"submit_flag",
               user:readCookie("auth"),
               fi_id:readCookie("fi_id")
    
            }))
            dataSocket.onmessage = function (event1) {
                const data = JSON.parse(event1.data);
                let message = data.message;
                let funcn = data.function;
                setMessage(message,funcn,e);
            };
        })
    })
    
}
evLisLike();
evLDislike();
evLDissubmit();
roomName= "abcd";
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

function setMessage(msg,funcn,eve){
    
    messageContainer.style.color = "white";
    if(msg==="Already liked"){
        messageContainer.style.display="block";
        messageContainer.innerHTML= "You have already liked the challenge";
        messageContainer.style.backgroundColor = "yellow";
        messageContainer.style.color = "purple";
        
        
    }
    else if(msg==='Already disliked'){
        messageContainer.style.display="block";
        messageContainer.innerHTML= "You have already disliked the challenge";
        messageContainer.style.backgroundColor = "yellow";
        messageContainer.style.color = "purple";
        
    }
    else if(msg.like==="Liked a challenge"){
        eve.path[1].childNodes[1].innerText = parseInt(eve.path[1].childNodes[1].innerText)+1;
        
    }
    else if(msg.dislike==='Disliked a challenge'){
        eve.path[1].childNodes[1].innerText = parseInt(eve.path[1].childNodes[1].innerText)+1;
        
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
            fi_id:readCookie("fi_id"),
            message:'filter'
        }))
        dataSocket.onmessage = function(event1){
            const data = JSON.parse(event1.data);
            let message = data.message;
            challengeContainer.forEach((cont)=>{
                document.querySelector(".challenges").removeChild(document.querySelector(".challenge"))
            })
            challengeContainer.forEach((cont)=>{
                
            })
            for(let m of message){
                challenge_name = m[1];
                challenge_difficulty = m[7];
                challenge_description = m[8];
                challenge_link = m[9];
                challenge_points = m[10];
                challenge_solves = m[3];
                challenge_likes = m[4];
                challenge_dislikes = m[5];
                let fc1 = challenge_name+"aaaa";
                let fc2 = challenge_name+"bbbb";
                const div = document.createElement('div');
                div.className="challenge"
                div.innerHTML = `<p class="name">${challenge_name}</p><p class="description">${challenge_description}</p><p class="location"><a href="${challenge_link}">${challenge_link}</a> </p><div class="filterInfo"><p class="difficulty">${challenge_difficulty}</p><p class="likes"><i style="color: white;font-size:25px" class="fa fa-thumbs-up likeBtn ${challenge_name}"></i><span class="likeCounter">${challenge_likes}</span> </p><p class="dislikes"><i style="color: white;font-size:25px" class="fa fa-thumbs-down dislikeBtn ${fc1}"></i><span class="dislikeCounter">${challenge_dislikes}</span></p><p class="points">Points: ${challenge_points}</p><p class="solves">Solves: ${challenge_solves}</p></div><input type="text" class="flagSubmit" placeholder="flag{the_flag_you_get}"><button type="submit" class="submitFlag ${fc2}">Submit</button><p class="comments"><span>Comments</span><i id="commentsScroll" style="color:white; font-size:30px;position:relative;top:5px;" class="fa fa-angle-double-down"></i></p>`;
                let n = "."+challenge_name;
                let n1 = "."+fc1;
                let n2 = "."+fc2;
                
                document.querySelector(".challenges").appendChild(div);
                document.querySelector(n).addEventListener("click",(eve1)=>{
                    challenge_name = eve1.path[3].children[0].innerHTML;
                    dataSocket.send(JSON.stringify({
                    challenge_name:challenge_name,
                    message:'like',
                    user:readCookie("auth"),
                    fi_id:readCookie("fi_id")
                }))        
                dataSocket.onmessage = function (event1) {
                    const data = JSON.parse(event1.data);
                    let funcn = data.function;
                    let message = data.message;
                    setMessage(message,funcn,eve1);
                };
                });
                document.querySelector(n1).addEventListener("click",(eve2)=>{
    
                    challenge_name = eve2.path[3].children[0].innerHTML;
                    dataSocket.send(JSON.stringify({
                        challenge_name:challenge_name,
                        message:'dislike',
                        user:readCookie("auth"),
                        fi_id:readCookie("fi_id")
                    }));
                    dataSocket.onmessage = function (event11) {
                        const data = JSON.parse(event11.data);
                        let message = data.message;
                        let funcn = data.function;
                       
                        setMessage(message,funcn,eve2);
                    };
                });
                document.querySelector(n2).addEventListener("click",(eve3)=>{
                    challenge_name = eve3.path[1].children[0].innerHTML;
                    userFlag = eve3.path[1].children[4].value;
                    dataSocket.send(JSON.stringify({
                       challenge_name:challenge_name,
                       flag:userFlag,
                       message:"submit_flag",
                       user:readCookie("auth"),
                       fi_id:readCookie("fi_id")
            
                    }))
                    dataSocket.onmessage = function (event12) {
                        const data = JSON.parse(event12.data);
                        let message = data.message;
                        let funcn = data.function;
                        setMessage(message,funcn,eve3);
                    };
                })
            }
        }
    })
})


