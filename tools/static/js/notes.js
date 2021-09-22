const newNote = document.querySelector(".addNewNote");
const form = document.getElementById("form");
const editBtns = document.querySelectorAll(".edit");
const deleteBtns = document.querySelector(".delete");
const editSave = document.querySelectorAll(".editSave")
var editable = false;

editBtns.forEach((btn)=>{
    btn.addEventListener("click",(e)=>{
       editable = true;
       e.path[1].childNodes[1].contentEditable = true;
       e.path[1].childNodes[3].contentEditable = true;
       e.path[1].childNodes[3].focus();
       console.log(e.path[1].childNodes)
       e.path[1].childNodes[7].style.display ="inline";
    })
})

editSave.forEach((btn)=>{
    btn.addEventListener("click",(e)=>{
        console.log(e.path[1]);
    })
})
newNote.addEventListener("click",()=>{
    if(form.style.display==="none"){
    form.style.display = "block";
    }
    else{
        form.style.display="none";
    }
})
