import Collage from "./Collage"
import { useContext } from "react"
import { studentcontext } from "./App"

function Student(){
    let student_data = useContext(studentcontext)
    return (

        <>
        <h1>student details</h1>
        <h2>Studen - {student_data[0]}{student_data[1]}</h2>
        </>
    )
}

export default Student