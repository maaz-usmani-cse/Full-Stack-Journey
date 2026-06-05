import { useContext } from "react"
import { laptopcontext } from "./App"

function Laptop(){
    let{brand,price,ram}=useContext(laptopcontext)
return (
    <>
    
    <h1>LAptop shop</h1>
    <h2>Laptop Details - {brand}{price}{ram}</h2>

    </>
)
}
export default Laptop