import { Routes,Route } from "react-router-dom"
import About from "./About"
import Home from "./Home"
import Structure from "./Structure"


function App(){
  return (
    <>
    <Routes>
      <Route path='/' element={<Structure/>}>
      <Route path='/' element={<Home/>}></Route>
      <Route path='/About' element={<About/>}></Route>
      </Route>

    </Routes>
    </>
  )
}
export default App