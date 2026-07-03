const prompt = require("prompt-sync")()
const name = prompt("What is your name? ")
console.log("Hello",name, "Welcome to our game! ")

const shouldWePlay = prompt('Do you wanna play? ')

if (shouldWePlay.toLowerCase() === "yes") {
    console.log(`Okay lets play the game ${name}!`);
}