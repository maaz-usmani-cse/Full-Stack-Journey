let user_info={
name:maaz,
contact:735415645,
age:20
}
localStorage.setItem('user',JSON.stringify(user_info))
let save=localStorage.getItem('user')
console.log(save)