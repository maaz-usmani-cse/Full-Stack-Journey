import { useNavigate } from "react-router-dom"; 

function Home() {
    let navigate = useNavigate(); 

    return (
        <>
            <center style={{ marginTop: "100px" }}>
                <h1>🏡 Welcome to Home Page</h1>
                <br />
                
               
                <button onClick={() => navigate("/admin")} >
                    Go to Admin Page
                </button>
            </center>
        </>
    );
}

export default Home;