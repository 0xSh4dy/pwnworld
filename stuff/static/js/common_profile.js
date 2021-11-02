var solvedContainer = document.querySelector(".solvedContainer");
var likeContainer = document.querySelector(".likeContainer");
var dislikeContainer = document.querySelector(".dislikeContainer");
var topContainer = document.querySelector(".topContainer");
var createdContainer = document.querySelector(".createdContainer");
function htmlDecode(input){
    var doc = new DOMParser().parseFromString(input,"text/html");
    return doc.documentElement.textContent;
}
var dec = htmlDecode(retObj)
dec = JSON.parse(dec);
var total_solves = dec.total_solves;
var chals_solved = dec.chals_solved;
var liked_chals = dec.liked_challenges;
var disliked_chals = dec.disliked_challenges;
var is_online = dec.is_online;
var username = dec.username;
var created_chals = dec.created_challenges;
var divSolved = document.createElement("div");
divSolved.className = "solved_names";
divSolved.innerHTML = "<div><h1>So</h1><span>Lv</span><h1>ed</h1>&nbsp;&nbsp;<h1>Ch</h1><span>Al</span><h1>le</h1><span>Ng</span><h1>es</h1></div>"
chals_solved.forEach((c)=>{
    divSolved.innerHTML+= `<div class="cSolved">${c}</div>`
})
solvedContainer.appendChild(divSolved);

var divLiked = document.createElement("div");
divLiked.className = "liked_names";
divLiked.innerHTML = "<div><h1>Li</h1><span>K</span><h1>ed</h1>&nbsp;&nbsp;<h1>Ch</h1><span>Al</span><h1>le</h1><span>Ng</span><h1>es</h1></div>";
liked_chals.forEach((c)=>{
    divLiked.innerHTML+=`<div class="cLiked">${c}</div>`
})
likeContainer.appendChild(divLiked);

var divDisliked = document.createElement("div");
divDisliked.className = "disliked_names";
divDisliked.innerHTML = "<div><h1>Di</h1><span>Sl</span><h1>ik</h1><span>Ed</span>&nbsp;&nbsp;<h1>Ch</h1><span>Al</span><h1>le</h1><span>Ng</span><h1>es</h1></div>";
disliked_chals.forEach((c)=>{
    divDisliked.innerHTML+=`<div class="cDisliked">${c}</div>`
})
dislikeContainer.appendChild(divDisliked);

var divCreated = document.createElement("div");
divCreated.className = "created_names";
divCreated.innerHTML = "<div><h1>Cr</h1><span>Ea</span><h1>te</h1><span>D</span>&nbsp;&nbsp;<h1>Ch</h1><span>Al</span><h1>le</h1><span>Ng</span><h1>es</h1></div>";
if(created_chals===0){
    divCreated.innerHTML+= `<div class="cCreated">${username} has not created any challenge yet</div>`
}
else{
    created_chals.forEach((c)=>{
        divCreated.innerHTML+=`<div class="cCreated">${c}</div>`
    })
}
createdContainer.appendChild(divCreated);

var divCont = document.createElement("div");
divCont.className = "tInner";
online_status = is_online===false?"Offline":"Online"
divCont.innerHTML = `<span id="username">${username}</span><span id="totalSolveCount">Total Solves: ${total_solves}</span ><span id="activityStatus">${online_status}</span>`
topContainer.appendChild(divCont);
is_online===false?document.getElementById("activityStatus").style.color="red":document.getElementById("activityStatus").style.color="rgb(61, 236, 38)";