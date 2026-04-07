let button=document.getElementById("b");
let isDarkmode=false;
button.addEventListener("click",function(){
    if(isDarkmode===false){
        document.body.style.backgroundColor="black"
        document.body.color="white"
        button.innerText="Swich to light mode"
        isDarkmode=true;
    }
    else{
        document.body.style.backgroundColor="white"
        document.body.color="black"
        button.innerText="Swich to dark mode"
        isDarkmode=false
    }
}


);

alert("mmm")

