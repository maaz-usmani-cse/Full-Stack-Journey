import { Route, Routes } from "react-router-dom";
import Signup from "./signup"; 
import Login from "./login";   

function App() {
  return (
    <>
     
      <Routes>
        <Route index element={<Signup />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </>
  );
}

export default App;

