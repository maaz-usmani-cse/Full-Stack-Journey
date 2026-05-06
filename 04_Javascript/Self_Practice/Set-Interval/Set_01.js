let s=0
let timer=null
function start(){
timer=setInterval(function(){
    s=s+1
    document.getElementById('count').innerText=s




},1000)


}

function stop(){
    clearInterval(timer)
}

function reset(){
    clearInterval(timer)
    start=0
    document.getElementById('count').innerText=s
}