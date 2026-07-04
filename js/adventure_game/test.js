const prompt = require("prompt-sync")()
const name = prompt("What is your name? ")
console.log("Hello",name, "Welcome to our game! ")

const shouldWePlay = prompt('Do you wanna play? ')

if (shouldWePlay.toLowerCase() === "yes") {
    // Game logic
    const leftOrRight = prompt("You entered a maze, do you want to go left or right? ")
    if (leftOrRight.toLowerCase() === "left") {
        console.log("You go left and see a bridge..,")
        const cross = prompt("Do you wanna cross the bridge?")
        if (cross.toLowerCase()=== "yes" || cross.toLowerCase() === "y" || cross.toLowerCase() === "Okay" ) {
            console.log('You crossed, but the bridge was weak and broke and you fell. You lost little breh!')
        }else{
            console.log(`Good choice ${name}.. You won the game`)
        }
    }else{
        console.log("You go right and fall of a cliff... Game over buddy!")
    }
}else if(shouldWePlay.toLowerCase() == "no") {
    console.log(`Okay ${name} breh! (;`)
} 
else{
    console.log("Invalid input!..")
}

