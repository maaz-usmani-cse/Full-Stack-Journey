import { useContext } from "react"
import { dataobj } from "./App"

function Child_2(){
    let { name, age } = useContext(dataobj);
    return(
        <>
        <h1>Child 2 - {name}{age}</h1>
        
        </>
    )
}

export default Child_2