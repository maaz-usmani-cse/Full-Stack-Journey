let numbers = [10, 50, 30, 90, 20];
    let maxNum = numbers[0]; 
    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] > maxNum) {
            maxNum = numbers[i]; 
        }
    }

    console.log("Maximum Number is: " + maxNum);