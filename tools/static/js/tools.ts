const calculateBtn = document.getElementById("calculate");
const outputSection = document.getElementById("outputValue");
const inputData = document.getElementById("inputData");
const hashBtn = document.querySelectorAll(".hashbtn");
const mode = document.getElementById("mode");
const clearBtn = document.getElementById("clear");
const converterBtn = document.querySelectorAll(".converterBtn");
const formData1 = document.getElementById("formData1");
const formData2 = document.getElementById("formData2");
let result: string;

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

 
async function calc(dataToModify:string,method:string){
    outputSection.innerHTML = "Calculating..."
    let body:object = {
        val1:dataToModify,
        val2:method
    }
    let response = "";
    response = await axios({
        method:"POST",
        url:"http://127.0.0.1:8000/tools/main",
        data:body
    })
    result = response.data;
    outputSection.innerHTML = result;

}
hashBtn.forEach((btn) => {
    btn.addEventListener("click", () => {
        mode.innerHTML = btn.innerHTML;
    })
})
converterBtn.forEach((btn) => {
    btn.addEventListener("click", () => {
        mode.innerHTML = btn.innerHTML;
    })
})
clearBtn.addEventListener("click", () => {
    outputSection.innerHTML = '';
    inputData.value = '';
})
calculateBtn.addEventListener("click", () => {
    let curMode: string = mode.innerHTML;
    let mainMode: string;
    let inputVal: string = inputData.value;
    // if (curMode === "md5" || curMode === "sha1" || curMode === "sha256" || curMode === "sha512") {
    //     mainMode = "hash";
    // }

    if (curMode === "md5") {
        result = md5(inputVal);
    }
    else if (curMode === "sha1") {
        result = sha1(inputVal);
    }
    else if (curMode === "sha256") {
        result = sha256(inputVal);
    }
    else if (curMode === "sha512") {
        result = sha512(inputVal);
    }
    else if(curMode==="base64 encode"){
        result = btoa(inputVal);
    }
    else if(curMode==="base64 decode"){
        try{
            result = atob(inputVal)
        }
        catch(e){
            result = "Invalid input"
        }
    }
    else if(curMode==="base32 encode"){
    calc(inputVal,"base32encode");
    }
    else if(curMode==="base32 decode"){
        calc(inputVal,"base32decode");
    }
    else if(curMode==="to hex"){
        calc(inputVal,"toHex");
    }
    else if(curMode==="hex decode"){
        calc(inputVal,"fromHex");
    }
    else if(curMode==="decode binary string"){
        calc(inputVal,"decodeBS")
    }
    else if(curMode==="to binary String"){
        calc(inputVal,"toBS")
    }
    outputSection.innerHTML = result;
    // let data = string(inputData.value);
    // switch(modes){
    //     case "md5"
    // }
})