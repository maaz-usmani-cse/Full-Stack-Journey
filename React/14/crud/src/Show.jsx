import axios from "axios"
import { useEffect } from "react"

function Show(){

    useEffect(()=>{

        axios.get('http://localhost:3000/userdata')
        .then((res)=> console.log(res.data))
    }

    )
    return(
        <>
        <h1>Show data</h1>


        </>
    )
}
export default Show