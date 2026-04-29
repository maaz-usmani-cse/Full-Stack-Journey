/*

Counter-->> .mene ek counter banaya hai jisme user agr plus p click krey to wo bdhte rhe 
-->aur jab badhe to  counter ka color v bdlega green iska logic mene plus function k andr rkha hai


minus function-->> isme agr user - wale button p click krega to wo minus hote jayega aur color red hoga agr
-->> mene isme if ka use krek logic lagaya h ki agr number 1 se uper ho tabhi minus hoga 
-->> agr wo 1 se uper ho number tab minus ho agr wo logic na lagatey to 0 p v  minus krne p wo -1,-2 ayse chala jata





*/








let a=0
let counter=document.getElementById('counter')
function plus(){
    a=a+1
    counter.innerHTML=a
    if(a>0){
        counter.style.color='green'
        status.textcontent='Even'
    }
 
   

}



function minus(){
    if (a>0){
        a=a-1
        counter.innerHTML=a
        counter.style.color='red'
    }
    if (a==0){
        counter.style.color='black'
    }
}