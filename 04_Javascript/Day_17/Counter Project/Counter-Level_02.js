// 1. Elements ko professional tarike se select karna (Function ke bahar)
const counterElement = document.querySelector('#counter');
const statusElement = document.querySelector('#status');
const plusBtn = document.querySelector('#plusBtn');
const minusBtn = document.querySelector('#minusBtn');

// 2. Data variable
let count = 0; 

// 3. Logic Function (Ye decide karega ki status aur color kya hoga)
function updateDisplay() {
    // Screen par number update karo
    counterElement.textContent = count;

    // Logic: Zero, Even, ya Odd? Aur colors.
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
        statusElement.style.color = "#d35400"; // Thoda dark orange/red type color
        counterElement.style.color = "#d35400";
    }
}

// 4. Action Functions (Badhane aur ghatane ke liye)
function increment() {
    count++; // Value badhao
    updateDisplay(); // Display update karo
}

function decrement() {
    // Logic: 0 se niche nahi jana chahiye
    if (count > 0) {
        count--; // Value ghatao
        updateDisplay(); // Display update karo
    } else {
        // Option: Agar 0 pe minus dabaye toh alert de sakte hain
        // alert("Cannot go below zero!");
    }
}

// 5. Event Listeners (Professional tarika, HTML mein onclick likhne se behtar)
plusBtn.addEventListener('click', increment);
minusBtn.addEventListener('click', decrement);

// 6. Initial Call (Page load hote hi status sahi dikhane ke liye)
updateDisplay();