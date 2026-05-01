
function store(){
let name=document.getElementById('name').value
let contact=document.getElementById('contact').value
let text=document.getElementById('text').value
document.getElementById('res').textContent=name+' '+contact+' '+text
return false

}