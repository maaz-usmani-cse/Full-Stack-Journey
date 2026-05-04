function store(){
    let name=document.getElementById('name').value
    let age=document.getElementById('age').value
    let contact=document.getElementById('contact').value
    
    if (name==''){
        alert('please fill your name')
        document.getElementById('name').focus()
        return false


    }
    else if(age==''){
        alert('please fill your age')
        document.getElementById('age').focus()
        return false
    }
    else if(isNaN(age)){
        alert('please enter age in number')
        document.getElementById('age').focus()
        return false

    }
    else if(contact==''){
        alert('please fill your contact')
        document.getElementById('contact').focus()
        return false
    }
    else if(isNaN(contact)){
        alert('please enter contact in number')
        document.getElementById('contact').focus()

    }
}