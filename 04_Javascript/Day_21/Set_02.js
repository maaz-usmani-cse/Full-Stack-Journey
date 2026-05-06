/*
setinterval syntax {document.write('working)}
*/

let v=0
let st
function start(){
    st=setInterval(()=>{
        document.getElementById('count').innerHTML=++v

    },500)
}

function stop(){
clearInterval(st)
}

function reset(){
    v=0
    document.getElementById('count').innerHTML=v
    clearInterval(st)
}







