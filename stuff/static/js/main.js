const login = document.getElementById("signin")
const register = document.getElementById("register")
login.addEventListener("click",()=>{
    // window.location.replace("http://127.0.0.1:8000/signin");
    window.location.href = "http://127.0.0.1:8000/signin";

})
register.addEventListener("click",()=>{
    window.location.href = "http://127.0.0.1:8000/register";

})
