import axios from "axios"
import { useEffect, useState } from "react"

function App(){
  // 🚨 SUDHAAR 1: Andar khali array [] diya taaki shuru me map() error na de
  let [apidata, setApidata] = useState([])

  useEffect(() => {
    // 🚨 SUDHAAR 2: URL ko '/posts' se '/comments' kiya kyunki isme id, name, email, body sab hota hai
    axios.get('https://jsonplaceholder.typicode.com/comments')
    
    // 🚨 SUDHAAR 3: setconsole.log hatakar sahi se setApidata kiya
    .then((res) => setApidata(res.data)) 
    
  }, [])

  return (
    <>
      {/* Jaisa tumne table banaya tha, ditto wahi ekdum easy format */}
      <table border='1' cellPadding="10" style={{ margin: "20px auto", width: "90%" }}>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Body</th>
        </tr>

        {
          apidata.map((e) => (
            <tr key={e.id}>
              <td>{e.id}</td>
              <td>{e.name}</td>
              <td>{e.email}</td>
              <td>{e.body}</td>
            </tr>
          ))
        }
      </table>
    </>
  )
}

export default App