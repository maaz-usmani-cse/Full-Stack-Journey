let mybody=document.getElementById('mybody')
let red=document.getElementById('red')
let green=document.getElementById('green')
let yellow=document.getElementById('yellow')


red.addEventListener("click",function(){
    mybody.style.backgroundColor='red';
});

green.addEventListener("click",function(){
    mybody.style.backgroundColor='green';
});

yellow.addEventListener("click",function(){
    mybody.style.backgroundColor='yellow';
});