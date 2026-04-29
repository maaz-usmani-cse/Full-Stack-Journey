const tvbutton=document.getElementById("tvbutton")
const mobilebutton=document.getElementById("mobilebutton")
const laptopbutton=document.getElementById('laptopbutton')
const body = document.body; 
const displayImg = document.getElementById('displayImg');


function tv (){
displayImg.src = "https://static1.xdaimages.com/wordpress/wp-content/uploads/wm/2024/06/surface-laptop-7-34.jpg"; 
    body.style.backgroundColor = "skyblue";

}


function mobile(){
 body.style.backgroundColor = "red";
 displayImg.src='https://pluspng.com/img-png/cell-phones-png-hd--1024.png'
}



function laptop(){
 body.style.backgroundColor = "yellow";
 displayImg.src='https://tse1.mm.bing.net/th/id/OIP.Efwjc3cuOhV7Km4rAw-nEwHaE9?r=0&cb=thfvnext&pid=ImgDet&w=184&h=123&c=7&dpr=1.3&o=7&rm=3'
}


tvbutton.addEventListener('click',tv)
mobilebutton.addEventListener('click',mobile)
laptopbutton.addEventListener('click',laptop)





