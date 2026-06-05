import Child_1 from "./Child_1";
import { createContext } from "react";
export const dataobj = createContext();
export const laptopcontext = createContext();
export const studentcontext = createContext();
export const cartcontext = createContext();
import Collage from "./Collage";
import Shop from "./Shop";
import Navbar from "./Navbar";
function App(){
    let person = {
        name: "Aaru",
        age: 21
    };

    let laptop = {
        brand: "HP",
        price: 65000,
        ram: "16GB"
    };

    let cartItem = { product: "iPhone 15", quantity: 2 };

    let student=["Python", "Django", "React", "SQL"]
    return(
        <>
        <dataobj.Provider value={person}>

                <Child_1/>

        </dataobj.Provider>
        <hr />
            <laptopcontext.Provider value={laptop}>

                <Shop/>

              </laptopcontext.Provider>
         <hr />


         <studentcontext.Provider value={student}>
                <Collage/>
            
             </studentcontext.Provider>



             <hr />

             
         <cartcontext.Provider value={cartItem}>
                <Navbar/>
            
             </cartcontext.Provider>

        </>
    )
}

export default App
