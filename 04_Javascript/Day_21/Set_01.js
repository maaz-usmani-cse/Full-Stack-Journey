/*

*/


function store(){
    let name=document.getElementById('name')
    localStorage.setItem('username',name)
}
let person={
    name:'mohit',
    'age':23,
    'city':'bhopal',

}
localStorage.setItem('personinfo',JSON.stringify(person))
let v=JSON.parse(localStorage.getItem('personinfo'))
console.log(v)
