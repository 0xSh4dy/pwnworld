function htmlDecode(input) {
    var doc = new DOMParser().parseFromString(input, "text/html");
    return doc.documentElement.textContent;
}
dataset = JSON.parse(htmlDecode(dataset));
dataset = Object.entries(dataset);
const canvas = document.getElementById("pieChart");
const dashboardContent = document.querySelector(".dashboardContent");
const dataSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/pwn/'
    + 'dashboard'
    + '/'
);
//  PIE Chart
var xVars = [];
var yVars = [];

dataset.forEach((ds)=>{
    xVars.push(ds[0]);
    yVars.push(ds[1]);
})

var barColors = ["#f54e42","#f5b642","#f57842","#bcf542","#57f542","#42f5ce","#4278f5","#8a42f5","#f542d1"];

new Chart("pieChart",{
    type:"pie",
    data:{
        labels:xVars,
        datasets:[{
            backgroundColor:barColors,
            data:yVars
        }]
    },
    options:{
        responsive:true,
        legend: {
            position: 'bottom',
            
          },
        title:{
            display:true,
            text:"Types of Challenges Solved",
            position:"right",
            fontSize:25,
            fontColor:"white"

        },
        
    
}
});

Chart.defaults.global.defaultFontColor = "purple";
Chart.defaults.global.defaultFontSize = "12";


// Bar Chart
diffData = JSON.parse(htmlDecode(diffData));
var xvals = ["Easy","Medium","Hard"];
var yvals = [diffData.easy,diffData.medium,diffData.hard];
var barColors = ["#34568B","lime","red"];
new Chart("barChart",{
    type:"bar",
    data:{
        labels:xvals,
        datasets:[{
            backgroundColor: barColors,
            data: yvals,
            categoryPercentage: 1,
            barPercentage: 0.5,
        }]},
        options: {
            legend: {display: false},
            title: {
              display: true,
              text: "Challenges Solved vs Difficulty",
              fontColor:"white",
              fontSize:20
            },
            scales: {

                xAxes: [{
                    
                    ticks:{
                        fontColor:"blue",
                        fontSize:20
                    }
                }],
                yAxes:[{
                    ticks:{
                        fontSize:15
                    }
                }]
            }
          }

})


dataSocket.onclose = function(e){
  console.error("Web socket closed unexpectedly");
}
dataSocket.onopen = function(e){
    dataSocket.send(JSON.stringify({
        req:"request"
    }))
}
dataSocket.onmessage = function(event1){
  data = JSON.parse(event1.data);
  data = data.data;
  data.forEach((dat)=>{
      let username = dat[1];
      let message = String(dat[3]);
      let msg1;
      let msg2;
      mIndex = message.indexOf("the challenge");
      if(mIndex!=-1){
        msg1 = message.substring(0,mIndex+14);
        msg2 = message.substring(mIndex+14,message.length+1);
        message1 = `<span class="messageContent1">${msg1} </span>`;
        message2 = `<span class="messageContent2">${msg2} </span>`;
        message = message1+message2;
      }
      else if(mIndex===-1){
          message = `<span class="messageContent1">${message}</span>`;
      }
      let date = `<span class="dateContent"> ${dat[2]} (UTC)</span>`;
      
      let div = document.createElement("div");
      div.className = "dashContent"
      div.innerHTML = date + message;
      dashboardContent.appendChild(div);
  })
}
