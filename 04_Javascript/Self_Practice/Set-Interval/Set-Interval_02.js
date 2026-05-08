let v = 0; 
let st=null

window.onload = function() {
    start(); 
};


function start(){
    clearInterval(st)
    st=setInterval(function(){
        v=v+1
        document.getElementById('count').innerHTML=v



    },1000)
}

function stop() {
    clearInterval(st);
    console.log("Timer ruk gaya!");
}

function reset() {
    clearInterval(st);
    v = 0;
    document.getElementById('count').innerHTML = v;
    start(); 
}