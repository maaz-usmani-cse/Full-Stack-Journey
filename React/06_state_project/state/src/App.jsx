//let [variable,function]=usestate(initial state)
import Count from "./Count";
import { useState } from "react";
function App(){
    let[num,setNum]=useState(23)
    let[n,setN]=useState('code')
    let[color,badlorang]=useState('yellow')
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


        <button onClick={()=>badlorang('red')}>Red</button>
        <button onClick={()=>badlorang('blue')}>blue</button>
        <button onClick={()=>badlorang('green')}>geen</button>
        <button onClick={()=>badlorang('orange')}>orange</button>
     
        </div>
        <br /><br />

        <Count/>
        </>
    )
  
}
export default App

