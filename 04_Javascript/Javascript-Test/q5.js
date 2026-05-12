function reverseNumber(num) {
    let str = num.toString();
    let reversedStr = "";

    for (let i = str.length - 1; i >= 0; i--) {
        reversedStr += str[i];
    }

    return parseInt(reversedStr); 
}

let x = 32243;
console.log("Expected Output: " + reverseNumber(x)); 