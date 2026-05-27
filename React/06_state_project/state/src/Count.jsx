import { useState } from "react";

function Count() {
    let [count, setCount] = useState(0);
    let [show, setShow] = useState(true); 
    return (
        <>
            <h1>This is count page</h1>
            <h1>{count}</h1>
            
           
            <button onClick={() => setCount(count + 1)}>+</button>
            
           
            <button onClick={() => { count > 0 ? setCount(count - 1) : null }}>-</button>

            <br /><br />
            
           
            {show ? <h1>maazusmani</h1> : ''}
           
           
            <button onClick={() => setShow(!show)}>
                
                {show ? 'Hide' : 'Show'}
            </button>
        </>
    );
}

export default Count;