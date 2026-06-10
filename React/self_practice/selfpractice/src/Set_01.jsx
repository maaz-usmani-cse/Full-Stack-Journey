import { useState } from "react";
function Set_01(){
    let[count, setCount]=useState(0)
    return (

        <>
        
        <h1>Use state screen </h1>
        <h2>{count}</h2>
        <button onClick={()=> setCount(count+1)}>Increment</button>
        <button onClick={()=> { if (count>0)  setCount(count-1)}}>Decrement</button>

        </>
    )


}

export default Set_01


