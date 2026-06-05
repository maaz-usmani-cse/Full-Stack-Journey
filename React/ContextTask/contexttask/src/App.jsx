import { createContext } from "react";
import { Routes, Route } from "react-router-dom"; 
import Home from "./Home";
import Admin from "./Admin";

export const adminContext = createContext();

function App() {
    
    let adminData = {
        role: "Administrator",
        secretCode: "MAAZ-2026-CSE",
        status: "Active"
    };

    return (
        <>
           
            <adminContext.Provider value={adminData}>
                
                
                <Routes>
                   
                    <Route path="/" element={<Home />} />
                    
                   
                    <Route path="/admin" element={<Admin />} />
                </Routes>

            </adminContext.Provider>
        </>
    );
}

export default App;

