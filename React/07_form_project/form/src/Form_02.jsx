import { useState } from "react";

function Form_02() {
    // 1. Python ki dictionary jaisa object. Keys hain: name, address, college
    let [formData, setFormData] = useState({
        name: "",
        address: "",
        college: ""
    });

    function handleChange(e) {
        let inputName = e.target.name;  // Pata chalega kis box me type hua
        let inputValue = e.target.value; // Pata chalega kya type hua

        // 2. Data update karne ka logic
        setFormData({
            ...formData,            // Purani dictionary copy ki
            [inputName]: inputValue // Dynamic key bazi!
        });
    }

    function handleSubmit(e) {
        e.preventDefault();
        console.log("Final Submitted Data:", formData);
    }

    return (
        <>
            <h2>Live View: {formData.name} | {formData.address} | {formData.college}</h2>
            
            <form onSubmit={handleSubmit}>
                <label>Name:</label>
                {/* ⚠️ name="name" bilkul useState ki key se match kar raha hai */}
                <input type="text" name="name" onChange={handleChange} />
                <br /><br />
                
                <label>Address:</label>
                {/* ⚠️ name="address" bilkul useState ki key se match kar raha hai */}
                <input type="text" name="address" onChange={handleChange} />
                <br /><br />
                
                <label>College:</label>
                {/* ⚠️ name="college" bilkul useState ki key se match kar raha hai */}
                <input type="text" name="college" onChange={handleChange} />
                <br /><br />
                
                <input type="submit" value="Submit Data" />
            </form>
        </>
    );
}

export default Form_02;