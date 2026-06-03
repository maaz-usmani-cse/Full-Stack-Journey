import { useState } from "react";
function Form_01(){

   let[setvariable,setfunction]=useState({})
   function Fun(e){
   let{name,value}=e.target
    setfunction({...setvariable,[name]:value})



   }

   function Submit(e){
    e.preventDefault()
       
   }
    return (
        
        <>
        
        <h1>form handling</h1>
        <h2>{setvariable.username}</h2>
        <h2>{setvariable.Contact}</h2>
        <form onSubmit={Submit}>

            <label htmlFor="">Name</label>
            <input type="text" name="username" placeholder="enter yiour name" onChange={Fun}/>

            <label htmlFor="">Contact</label>
            <input type="text" name="Contact" placeholder="enter your contact" onChange={Fun}/>
          <input type="submit" />

        </form>
        

        </>
    )
}

export default Form_01