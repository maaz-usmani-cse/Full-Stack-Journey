// 1. Elements ko professional tarike se select karna (Function ke bahar)
const counterElement = document.querySelector('#counter');
const statusElement = document.querySelector('#status');
const plusBtn = document.querySelector('#plusBtn');
const minusBtn = document.querySelector('#minusBtn');

// 2. Data variable
let count = 0; 


function updateDisplay() {
    // Screen par number update karo
    counterElement.textContent = count;

   
    if (count === 0) {
        statusElement.textContent = "Zero";
        statusElement.style.color = "black";
        counterElement.style.color = "black"; // Number ka color
    } else if (count % 2 === 0) {
        statusElement.textContent = "Even";
        statusElement.style.color = "green";
        counterElement.style.color = "green";
    } else {
        statusElement.textContent = "Odd";
        statusElement.style.color = "#d35400"; 
        counterElement.style.color = "#d35400";
    }
}

function increment() {
    count++; 
    updateDisplay(); 
}

function decrement() {
   
    if (count > 0) {
        count--; 
        updateDisplay(); 
    } else {
       
    }
}

plusBtn.addEventListener('click', increment);
minusBtn.addEventListener('click', decrement);

updateDisplay();