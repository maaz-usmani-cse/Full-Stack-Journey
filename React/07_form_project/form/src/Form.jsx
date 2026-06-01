import { useState } from "react";

function Form() {
    let [frmdata, setFrmdata] = useState("");
    let [frmdata_2, setFrmdata_2] = useState("");
    let [frmdata_3, setFrmdata_3] = useState("");

    function data(e) {
        setFrmdata(e.target.value);  
    }  

    function Data_2(e) {
        setFrmdata_2(e.target.value);
    }
    
    function Data_3(e) {
        setFrmdata_3(e.target.value);
    }

    // 🔥 1. YAHAN TERE CODE ME CHANGE KIYA HAI
    function Formsubmit(e) {
        e.preventDefault(); // Page reload hone se rokega
        console.log("--- FINAL SUBMITTED DATA ---");
        console.log("Name:", frmdata);
        print("Address:", frmdata_2)
        console.log("Address:", frmdata_2);
        console.log("College:", frmdata_3);
    }

    return (
        <>
            {/* Live screen par thoda saaf dikhane ke liye spacing lagayi */}
            <h1>Live View: {frmdata} | {frmdata_2} | {frmdata_3}</h1>
            
            {/* 🔥 2. YAHAN TERE FORM ME ONSUBMIT JODA HAI */}
            <form onSubmit={Formsubmit}>
                <label>Name</label>
                <input type="text" onChange={data} />
                
                <label>Address</label>
                <input type="text" onChange={Data_2} />
                
                <label>College</label>
                <input type="text" onChange={Data_3} />
                
                <input type="submit" value="Submit Form" />
            </form>
        </>
    );
}


export default Form;