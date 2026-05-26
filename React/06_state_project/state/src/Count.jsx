import { useState } from "react";

function Count() {
    let [count, setCount] = useState(0);
    let [show, setShow] = useState(true); // Naam 'setShow' rakha taaki confusion na ho

    return (
        <>
            <h1>This is count page</h1>
            <h1>{count}</h1>
            
            {/* Plus Button */}
            <button onClick={() => setCount(count + 1)}>+</button>
            
            {/* Minus Button: Ternary Operator ko arrow function ke ANDAR daal diya */}
            <button onClick={() => { count > 0 ? setCount(count - 1) : null }}>-</button>

            <br /><br />
            
            {/* Ternary 1: Agar show true hai toh naam dikhao, nahi toh kuch nahi ('') */}
            {show ? <h1>maazusmani</h1> : ''}
           
            {/* Toggle Button */}
            <button onClick={() => setShow(!show)}>
                {/* Ternary 2: Agar show true hai toh button par 'Hide' likho, nahi toh 'Show' */}
                {show ? 'Hide' : 'Show'}
            </button>
        </>
    );
}

export default Count;