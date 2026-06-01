import { useState } from "react"

function Form_handling(){
    let[setvariable,setfunction]=useState({})

    function fun(e){
        let[name,value]=e.target
        setfunction({...setfunction,[name]:value})

    }
    function Submit(e){
        e.preventDefault()
        console.log(setvariable)

    }
    
    return(

        <>
        <h1>input handling to one function</h1>
        <form onSubmit={Submit}>

            <label htmlFor="">name</label>
            <input type="text" name="username"/>
            <label htmlFor="">contact</label>
            <input type="text" name="contact"  />
            <input type="submit" />

        </form>
        
        </>
    )
}

export default Form_handling