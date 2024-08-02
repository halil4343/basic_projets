"use strict";

const min = 1;
const max = 1;
const randomInt = Math.floor(Math.random() * (max - min + 1)) + min;
let counter = 100

document.getElementById("submitGuess").addEventListener("click", function() {
    const guess = document.querySelector("#guess")
    counter --
    //value entered
    if(guess.value){
        var feedback = document.querySelector("#feedback");
        //it equals
        if(guess.value == randomInt){
            feedback.textContent = `Congs! You won. The number was ${randomInt}`

            var button = document.querySelector("#submitGuess")

            button.remove()
            guess.remove()
            
            let button2 = document.createElement("button")
            let container = document.querySelector(".container")
            
            container.appendChild(button2)
            button2.textContent = "Play again"
            button2.addEventListener("click",function(){
                window.location.href = window.location.href;
                console.log("hi")
            })
            
            document.querySelector("button").style.background= "linear-gradient(135deg, #f7f3bd 0%, #bfff00 100%)"
            document.querySelector("#pHeader").remove()
            document.querySelector("body").style.background = "linear-gradient(135deg, #f7f3bd 0%, #bfff00 100%)"
            document.querySelector("h1").style.color = "#bfff00"
            
            let colorChange = document.querySelectorAll(".color-change")
            colorChange.forEach(function(element) {
                element.style.color = "#bfff00"// Change text color if needed
                element.style.borderColor = "#bfff01"
            });
    }
    //too low
    else if(guess.value <randomInt) {
        feedback.textContent = "Too low"
    }
    //too high
    else if(guess.value >randomInt) {
        feedback.textContent = "Too high"
    }
    
    document.querySelector("#score").textContent = `Score : ${counter}`
}
})
