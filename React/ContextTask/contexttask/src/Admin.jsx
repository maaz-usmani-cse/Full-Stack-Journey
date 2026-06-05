import { useContext } from "react";
import { adminContext } from "./App"; 

function Admin() {
    
    let adminData = useContext(adminContext);

    return (
        <>
            <center >
                <h1 style={{ color: "red" }}>Admin Dashboard (Secret Area)</h1>
                <hr />
                <h2>Role: {adminData.role}</h2>
                <h2>Secret Code: {adminData.secretCode}</h2>
                <h2>Status: {adminData.status}</h2>
            </center>
        </>
    );
}

export default Admin;