import { Link,Outlet } from "react-router-dom"
function Structure(){

    return(
        <>
        <nav>

            <h1>maaz usmani Cse</h1>
            <ul>
                <li><Link to='/'>Home</Link></li>
                <li><Link to="/About">About</Link></li>
               
            </ul>
        </nav>

        <Outlet/>
          <footer>
            <h1>Footer section</h1>
          </footer>

        </>
    )
}
export default Structure