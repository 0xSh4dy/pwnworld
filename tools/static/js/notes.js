const newNote = document.getElementById("addNewNote");
const form = document.getElementById("formMain");
const editBtns = document.querySelectorAll(".edit");
const deleteBtns = document.querySelectorAll(".delete");
const editSave = document.querySelectorAll(".editSave");
// const search = document.getElementById("search");
var editable = false;


editBtns.forEach((btn)=>{
    btn.addEventListener("click",(e)=>{
       editable = true;
       e.path[1].childNodes[3].contentEditable = true;
       e.path[1].childNodes[3].focus();
       e.path[1].childNodes[7].style.display ="inline";
    })
})

// Delete a note
deleteBtns.forEach((btn)=>{
    btn.addEventListener("click",(e)=>{
        let title = e.path[1].childNodes[1].innerHTML;
        e.path[1].remove()        
        let csrfToken = getCookie("csrftoken");
        fetch("/tools/notes",{
            method:"DELETE",
            headers:{
                "X-CSRFTOKEN":csrfToken,
                "Content-Type":"application/json"
            },
            body:JSON.stringify({"title":title})
        })
    })
})

// Edit a note  
editSave.forEach((btn)=>{
    btn.addEventListener("click",(e)=>{
        e.path[1].childNodes[3].contentEditable = false;
        let title = e.path[1].childNodes[1].innerHTML;
        let newDetails = e.path[1].childNodes[3].innerHTML;
        btn.style.display = "none";
        let csrfToken = getCookie("csrftoken");
        const modifiedData = {"title":title,"details":newDetails}
        fetch("/tools/notes",{
            method:"PATCH",
            headers:{
                "X-CSRFTOKEN":csrfToken,
                "Content-Type":"application/json"
            },
            body:JSON.stringify(modifiedData)
        }).then(response=>response.text())
    })
})

newNote.addEventListener("click",()=>{
    console.log("clicked");
    console.log(form.style.display)
    if(form.style.display==="block"){
    form.style.display = "none";
    }
    else{
        form.style.display="block";
    }
})

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

// search.addEventListener("keypress",(e)=>{
//     console.log(e)
// })
