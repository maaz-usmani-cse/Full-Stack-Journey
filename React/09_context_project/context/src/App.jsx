import Child_1 from "./Child_1";
import { createContext } from "react";
export const dataobj = createContext();
function App(){
    let person = {
        name: "Aaru",
        age: 21
    };
    return(
        <>
        <dataobj.Provider value={person}>

                <Child_1/>

        </dataobj.Provider>
        
        </>
    )
}

export default App
