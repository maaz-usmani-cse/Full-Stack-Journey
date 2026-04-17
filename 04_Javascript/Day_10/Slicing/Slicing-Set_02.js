/*
Slicing-->> range of element ko select krne k liye use krte h slicing 

spilice-- removing the element and adding the element

*/


//slicing

// let ar=['maaz','usmani',12,'rits']
// let b=ar.slice(0,2)
// document.write(b)






//splice


// let ar=['maaz','usmani',12,'rits']
// let b=ar.splice(0,2)
// document.write(ar)





//wap to create an array and take 5 inpus from the user and print it then two element at last indexing then update the third element and also add 1 element at 4 indexing


let ar=[]
for(let a=0; a<5;a++){
    ar[a]=parseInt(prompt("enter a number"))
    

}
ar.push('maaz')
ar.push('usmani')
ar[3]='updqate'
ar.splice(4,0,'splice')

document.write(ar)
