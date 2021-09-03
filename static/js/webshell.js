var commands = ["ls", "mkdir", "rm", "rmdir", "echo", "grep", "cd"];
var defaultDirectory = "user";
var inputData = document.querySelector(".inputCommand");
var commandResult = document.querySelector(".commandResult");
var command;
window.addEventListener("keypress", function (event) {
    if (event.code === "Enter") {
        inputData.contentEditable = 'false';
        command = inputData.innerHTML;
        commandResult.innerHTML = "output";
        console.log(command);
    }
});
