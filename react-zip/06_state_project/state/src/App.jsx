//let [variable,function]=usestate(initial state)

import { useState } from "react";
function App(){
    let[num,setNum]=useState(23)
    let[n,setN]=useState('code')
    let[color,setColor]=useState('yellow')
    function fun(){
        setNum(90)
    }
        
    return (
        <>
        <div style={{backgroundColor:color}} >
            <h1>my name is maaz usmani age is{num}</h1>
        <button onClick={fun}>change</button>
        <button onClick={()=>setN(78)}>change second time</button>
        <br /><br />
        <h1>i want to lean {n}</h1>
        <button onClick={()=>setN('React')}>click react</button>


        <button onClick={()=>setColor('red')}>Red</button>
        <button>blue</button>
        <button>geen</button>
        <button>orange</button>
     
        </div>
        </>
    )
  
}
export default App

