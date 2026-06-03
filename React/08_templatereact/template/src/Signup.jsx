
import { useState } from "react"
import { useNavigate } from "react-router-dom" 

function Signup() {
    let [frmdata, Setfrmdata] = useState({})
    let navigator = useNavigate() 

    
    function signinput(i) {
        const { name, value } = i.target
        Setfrmdata({ ...frmdata, [name]: value })
    }

    function submit(e) {
        e.preventDefault()
        
        localStorage.setItem("signdata", JSON.stringify(frmdata))
        
        
        navigator('/login')
    }

    return (
        <>
            <center>
                <h1>Sign up page</h1>
                <form onSubmit={submit}>
                    <label>username</label>
                    <input type="text" name="username" onChange={signinput} /><br/><br/>

                    <label>email</label>
                    <input type="text" name="email" onChange={signinput} /><br/><br/>

                    <label>password</label>
                    <input type="text" name="password" onChange={signinput} /><br/><br/>

                    <input type="submit" value="Submit" />
                </form>
            </center>
        </>
    )
}

export default Signup