const prompt = require("prompt-sync")()
const name = prompt("What is your name? ")
console.log("Hello",name, "Welcome to our game! ")

const shouldWePlay = prompt('Do you wanna play? ')

const condition = shouldWePlay.toLowerCase === "yes"
console.log(condition)