import Home from "./Home"

function App(){
  function fun(Name){
    alert('working...'+Name)
  }
  return(
    <>
    <h1>Maaz-Usmani-Cse</h1>
    <button onClick={fun}>Click here</button>   
    <button onMouseEnter={fun}>Hover</button>
    <button onClick={()=>fun('maaz')}></button>
    <Home/>
    </>
  )
}

export default App


