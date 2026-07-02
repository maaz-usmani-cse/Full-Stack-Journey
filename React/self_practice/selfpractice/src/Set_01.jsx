import { useState } from "react";

function Count(){
let[count,setCount] = useState(0)
function increment(){
    setCount(count+1)

}
function decrement(){
    if (count>0){
          setCount(count-1)
    }
  
}

    return (
        <>
        <h1>Counter Project</h1>
        <h2>{count}</h2>
        <button onClick={increment}>Increment+</button>
        <button onClick={decrement}>-Decrement-</button>
        </>
    )
}


export default Count