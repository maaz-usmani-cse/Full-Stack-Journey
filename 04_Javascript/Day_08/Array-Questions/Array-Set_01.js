/*
#Array-->> array is a data type in which we can store multiple type of data in to a single variable 
-->> denote by square bracket
-->> ordered collection 

*/

// let person=['name','maaz','amjad','piyush']

// document.write(person[2])






//user s input lo aur array m 4th element print karao


// let myNumbers = []; 
// for (let a = 1; a <= 5; a++) {
//     let b = parseInt(prompt("Enter number " + a + ":"));
    
//     myNumbers.push(b);
// }


// document.write( myNumbers);










// user s input lena hai 1 se 10 tak aur usse print krna hai assending order m 

// let numbers = [];

// for (let i = 1; i <= 10; i++) {
//     let input = parseInt(prompt("Enter number " + i + " of 10:"));
//     numbers.push(input);
// }

// for (let i = 0; i < numbers.length; i++) {
//     for (let j = 0; j < numbers.length - 1; j++) {
//         if (numbers[j] > numbers[j + 1]) {
//             let temp = numbers[j];
//             numbers[j] = numbers[j + 1];
//             numbers[j + 1] = temp;
//         }
//     }
// }

// document.write(numbers);




//ek array h uske dusre index p kisi dusreelement ko rkhna hai 




// 5 input lo aur jo input aye uska sum print kro array m



let array=[]
let total=0
for (leta=1;a<=5;a++){
    let user=parseInt(prompt("enter a number"))
    array.push(user)

for (let j=0;j<array.length;j++){
    total=total+j[0]


}

}
document.write(total)


