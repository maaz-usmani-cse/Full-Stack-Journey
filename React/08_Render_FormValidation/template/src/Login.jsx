import { useState } from "react"
function Login() {
    let[loginform,setloginform]=useState({})
    function Store(e){
        let{name,value}=e.target
        setloginform({...loginform,[name]:value})
    }


    function submit(e){
        e.preventDefault()
        console.log(loginform)
        let localdata=JSON.parse(localStorage.getItem('signdata'))

       
    }


    return (
        <>
            <h1>THIS IS LOGIN PAGE</h1>

            <form action="" onSubmit={submit}>
                <label htmlFor="">Email</label>
                <input type="text" name="email" onChange={Store}/>
                <label htmlFor="">password</label>
                <input type="text" name="password" onChange={Store} />

                <input type="submit" />

            </form>
        </>
    )
}


export default Login