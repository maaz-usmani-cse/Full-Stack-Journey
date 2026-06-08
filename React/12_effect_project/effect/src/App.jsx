import { useEffect, useState } from "react"

function App(){
  let [changestate, setstate] = useState(0)
  

  let [color, setcolor] = useState("") 

  useEffect(() => alert('working'), [changestate])
  

  return (
    <>
      <h1 style={{ backgroundColor: color }}>{changestate}</h1>
      
      <button onClick={() => setstate(changestate + 1)}>+</button> <br /><br />
      
      <button onClick={() => setcolor('red')}>red</button> 

    </>
  )
}

export default App


