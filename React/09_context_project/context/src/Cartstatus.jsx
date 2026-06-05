import { useContext } from "react"
import { cartcontext } from "./App"
function Cartstatus(){
    let {product,quantity}=useContext(cartcontext)
    return (
        <>

        <h1>Cartstatus</h1>
        <h2>Cart item - {product} {quantity}</h2>

        </>
    )
}

export default Cartstatus