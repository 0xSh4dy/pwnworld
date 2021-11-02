const container = document.getElementById("container");
const scoreSocket = new WebSocket(
    `ws://${window.location.host}/ws/pwn/leaderboard/`
)
let currentPage = 1;
const maxCount = 5;
let globalCounter = 1;
let allResults = [];
function activatePageCounter(){
    let pageCounter = document.querySelectorAll(".pageCounter");
    pageCounter.forEach((pc)=>{
        pc.addEventListener("click",(e)=>{
            let num = parseInt(e.target.innerHTML);
            currentPage = num;
            let upperValue = currentPage*maxCount;
            let lowerValue = upperValue - maxCount;
            upperValue = upperValue-1;
            let res = allResults.filter((val,index)=>{
                return (index>=lowerValue&&index<=upperValue)
            })
            let init = 1;
            // container.innerHTML = "<th>td>Place</td><td>User</td><td>Score</td></th>";
            container.innerHTML = "";
            globalCounter = lowerValue+1;
            res.forEach((r)=>{
                container.innerHTML += `<tr><td class="first">${globalCounter}</td><td class="second">${r[0]}</td><td class="third">${r[1]}</td></tr>`
                globalCounter++;
            })
        })
    })
}

scoreSocket.onclose = (e)=>{
    console.error("Web socket close unexpectedly");
}

scoreSocket.onmessage = (e)=>{
    let message = JSON.parse(e.data)
    let result = message.message;
    console.log(result.length)
    allResults = result;
    let count = 1;
    let requiredButtons = Math.ceil(result.length/maxCount);
    document.querySelector(".pages").innerHTML = "";
    for(let i=1;i<=requiredButtons;i++){
        let btn = document.createElement("button");
        btn.className = "pageCounter";
        btn.innerHTML = i;
        document.querySelector(".pages").appendChild(btn);
    }
    activatePageCounter();
    let res1 = result.filter((val,index)=>{
        return index<maxCount;
    })
    container.innerHTML = "";

    res1.forEach((res)=>{
        const row = document.createElement("tr");
        row.className = "oneRow";
        row.innerHTML = `<td class="first">${count++}</td><td class="second">${res[0]}</td><td class="third">${res[1]}</td>`
        container.appendChild(row);
    })
}